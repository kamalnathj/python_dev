# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
lives = 5
print("Enter the Guess word")
guess_word=input()
guessed_word=""
for i in range(len(guess_word)):
    guessed_word += "$"
while lives > 0:
    print("Guess the Letter")
    letter_to_guess=input()
    for i in guess_word:
        if i == letter_to_guess:
            print("you have guessed a letter")
        else:
            lives -= 1
    print("Lives Remaining: "+str(lives))
    print(guessed_word)