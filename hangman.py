#!/usr/bin/env python

def vanna_white(the_word, guessed_letters):
    result = ""
    for letter in the_word:
        if letter in guessed_letters or \
           letter == ' ':
            result += letter
        else:
            result += "_"

        result += " "

    return result

import sys

print "Welcome to HANGMAN... type a word:"
the_word = sys.stdin.readline().strip()
print "the word you typed was:",
print the_word
print

print "Press <enter> to continue"
sys.stdin.readline()
for i in range(100):
    print

guessed_letters = []

# Automatically add punctuation marks
for letter in the_word:
    if not letter.isalpha() and letter not in guessed_letters:
        guessed_letters.append(letter)

points = 6
while True:
    print "-" * 30
    print "Guessed letters so far:",
    print ", ".join(guessed_letters)
    print "You have", points, "points left."
    print vanna_white(the_word, guessed_letters)

    print "Guess a letter:",
    the_letter = sys.stdin.readline().strip()
    print "You guessed", the_letter

    if len(the_letter) != 1:
        print "You didn't guess a letter."
        print "You idiot."
        continue

    if the_letter in guessed_letters:
        print "You already guessed that letter,",
        print "silly!"
        continue

    guessed_letters.append(the_letter)

    if the_letter not in the_word:
        print "Not awesome.  You lose a point."
        points = points - 1
        if points < 0:
            print "YOU LOSE!"
            print "the word was:", the_word
            sys.exit(1)
        continue

    # Otherwise the letter was in the word.
    print "Great!",
    vw = vanna_white(the_word, guessed_letters)
    print vw

    if '_' not in vw:
        print "-" * 30
        print
        print "A wiener is you!"
        print
        sys.exit(0)






