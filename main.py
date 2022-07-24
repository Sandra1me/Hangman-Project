import time
from words import choose_word , check_letter, lists, remove_word
from checks import printing , initial , continue_playing


fails, wrong, play, correct, choose = initial()

print('Hello! Wellcome to the hangman game!')
print('Let us begin')

word_list=lists(choose)

while play==True:
    word, guess=choose_word(word_list)
    word_list=remove_word(word_list,word)

    print(' Your word has the following spaces:')

    while fails>=0:
        printing(guess,word,fails,wrong)

        letter=input('\nTry a letter or a word: ')
        correct_letter=False
        correct_word=False
        
        guess, wrong, fails, correct_word=check_letter(letter,word,guess,correct_letter,wrong,correct_word,fails)

        if correct_word== True:
            break
    
    play, fails = continue_playing(play, fails, correct, word_list)

print('\nThanks for playing!\n')
time.sleep(1)