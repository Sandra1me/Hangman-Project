def choose_word(word_list):
    from random import random
    index=int(random()*len(word_list))
    word=word_list[index]
    guess=['_']*len(word)

    return word,guess

def check_letter(letter,word,guess,correct_letter,wrong,correct_word,fails):
    if len(letter)==1:
        for i in range(len(word)):
            if letter.upper()==word[i]:
                print('You letter is correct!\n')
                guess[i]=letter.upper()
                correct_letter=True
        
        if correct_letter==False:
            print('Wrong letter...\n')
            wrong=wrong+letter.upper()+' '
            fails-=1
    elif len(letter)>1:
        if letter.upper()==word:
            correct_word=True
        else:
            print('Wrong word...\n')
            fails-=1    

    if correct_word==True:
        print('Congratulations! You guessed the word!')
        print(word)

    if fails<0:
        print('You failed at guessing the word... Keep on trying!')

    return guess, wrong, fails, correct_word

def lists(choose):
    while choose==False:
        lan=input('Choose a language for the words to guess:\n1-Spanish \n2-English\n ')    

        if lan=='1':
            word_list=['OPERACIONES','LASTIMA','AVERGONZAR','MINISTRO','HERMANO','GOLOSINAS','HOMBROS','OLAS','LUNAR','RALLAR']
            choose=True
        elif lan=='2':
            word_list=['LATE', 'THIGH', 'RESEARCHER', 'MASK', 'KING', 'LEAFLET', 'PROJECTION', 'AUTONOMY', 'PUBLICATION', 'COERCE']
            choose=True
        else:
            print('Enter a valid option...')
    
    return word_list

def remove_word(word_list, word):
    word_list.remove(word)
    return word_list