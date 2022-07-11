def printing(guess,word,fails,wrong):
    print(guess)
    print('Length:',len(word))
    print('Fails left:', fails)
    print('Wrong letters used:',wrong)

def initial():
    fails=5 
    wrong=''
    play=True   
    correct=False
    choose=False

    return fails,wrong,play, correct, choose

def continue_playing(play, fails, correct, word_list):
    while correct==False:
        if len(word_list)==0:
            print('\nCongratulations! You guessed all the words!\nThanks for playing!\n')
            quit()

        question=input('\nDo you want to try another word? (y/n): ')

        if question.lower()=='n':
            play=False
            correct=True
        elif question.lower()=='y':
            fails=5
            correct=True
        
        else:
            continue
        
        return play, fails    