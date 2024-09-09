import streamlit as st
import random

# Load words from your wordle.py file
from wordle import words as allwords

def initialize_game():
    if 'word' not in st.session_state:
        st.session_state.word = random.choice(allwords).upper()
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'guesses' not in st.session_state:
        st.session_state.guesses = []
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

def check_guess(guess):
    result = ""
    for i, letter in enumerate(guess):
        if letter == st.session_state.word[i]:
            result += letter + "* "
        elif letter in st.session_state.word:
            result += letter + "? "
        else:
            result += letter + "  "
    return result.strip()

def main():
    st.title("Wordle")
    
    initialize_game()
    
    if not st.session_state.game_over:
        guess = st.text_input("Enter your guess (5 letters):", max_chars=5).upper()
        
        if st.button("Submit Guess"):
            if len(guess) != 5 or guess.lower() not in allwords:
                st.error("Please enter a valid 5-letter word.")
            else:
                st.session_state.attempts += 1
                result = check_guess(guess)
                st.session_state.guesses.append(result)
                
                if guess == st.session_state.word:
                    st.success(f"Correct! You guessed the word in {st.session_state.attempts} attempts.")
                    st.session_state.game_over = True
                elif st.session_state.attempts >= 6:
                    st.error(f"Game over! The word was {st.session_state.word}")
                    st.session_state.game_over = True
    
    # Display guesses
    for guess in st.session_state.guesses:
        st.text(guess)
    
    # Display attempts left
    if not st.session_state.game_over:
        st.text(f"Attempts left: {6 - st.session_state.attempts}")
    
    if st.session_state.game_over:
        if st.button("Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.experimental_rerun()

if __name__ == "__main__":
    main()
