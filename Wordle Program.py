'''
Enter valid 5 letter word. The game should tell you how close you are to guessing the Wordle ("secret 5 letter word").
A "*" symbol next to the letter(s) in the guess hints that the letter is in the correct position and
a "?" hints that the letter(s) is in the Wordle but in the incorrect position.
If the letter(s) in the guess is not in Wordle, then simply print it out.
'''


import wordle
import random

#generate word
allwords = wordle.words



#create list to for each character of the word or to track highscores
list2= []




#begin wordle

#set up accumulator variables that need to be outside of the 1st loop
win= 0
lost= 0
attempts1= 0
attempts2= 0
tries= 0
highscore= 0

#parent while loop
while True:
    tries += 1

    word= random.choice (allwords)
    word= word.upper()
    list1= []

    for a in word:
        list1 += [a]

    #print ("The Wordle is", word)
    #print ()
    
    print(format ("WORDLE", ">17s")   )       
    print ("------------------------------")


#set up accumulator variables that need to be outside of the 2nd loop
    accumulator= 0
    history= ""
    history1= ""

    while accumulator < 6:
        forword= word
        counter1= 0
        counter= 0

        if accumulator >=1 and len(guess)== 5 and (guess.lower() in allwords):

            print (history1, end="")


        guess= input ("Guess the word: ")
        guess= guess.upper()



        if len(guess)!= 5:

            print ("You must enter a 5 letter word.")

            continue



        elif guess.lower() not in allwords:

            print ("Invalid word.")

            continue

        else:
      
            print ()
            
            for i in guess:

                for x in forword:

                    if i !=x and i in list1:

                        if counter1 != 4:

                            forword= forword[counter+1:]

                            newcharacter= i +"? "
                            
                            history1 += newcharacter

                            counter1 += 1

                            break 
                        
                        else:


                            newcharacter= i +"?\n"
                            
                            history1 += newcharacter

                            counter1 += 1

                            break
                    
                    elif i != x:

                        if counter1 != 4:


                            forword= forword[counter+1:]

                            newcharacter= i +"  "
                            
                            history1 += newcharacter

                            counter1 += 1

                            break                        


                        else:

                            newcharacter= i +"\n"
                            
                            history1 += newcharacter

                            counter1 += 1

                            break


                           

                    elif i == x:

                        if counter1 != 4:

                            forword= forword[counter+1:]

                            newcharacter= i +"* "
                            
                            history1 += newcharacter

                            counter1 += 1

                            break                        

                        else:

                            newcharacter= i +"*\n"
                            
                            history1 += newcharacter

                            counter1 += 1

                            break


                        
        history += history1
        accumulator += 1
                    

        if guess == word:
            print (history1, end="")
            print()
            print("Correct! The Wordle is", word)
            print ("You guessed the Wordle in", accumulator,"tries")
            win += 1
            attempts1 += accumulator
            attempts2 += accumulator
            list2 += [attempts2]

            for i in list2:

                if attempts2 < i:
                    highscore= attempts2
                    continue
                    

                elif i < attempts2:
                    highscore = i
                    continue

                elif attempts2 == i:
                    highscore= attempts2
                    continue

            attempts2= 0

            break

        elif accumulator == 6 and guess != word:    
            print (history1, end="")
            print()
            print("Sorry, you did not guess the Wordle. The Wordle is", word)
            lost += 1
            attempts1 += 0
            attempts2 += accumulator
            list2 += [attempts2]

            for i in list2:

                if attempts2 < i:
                    highscore= attempts2
                    continue
                    

                elif i < attempts2:
                    highscore = i
                    continue

                elif attempts2 == i:
                    continue

            attempts2= 0


    print ()
    
    while guess == word or (accumulator == 6 and guess != word):
        choice= input ("Do you want to play again? (Y) or (N) ")
        choice= choice.upper()

        if choice == "Y":
            break

        elif choice == "N":
            break
            
        else:
            print ("Invalid response.")
            continue


    if choice == "Y":
        print ()
        continue

    if choice == "N":
        break



print ("High Score:", highscore)
print ("Average Score:", format(attempts1/tries, ".2f"))
print ("Number of lost games:", lost)
















