def printing(guess,word,fails,wrong):
    print(guess)
    print('Length:',len(word))
    print('Fails left:', fails)
    print('Wrong letters used:',wrong)

def initial():
    fails=5 
    wrong=''
    play=True   

    return fails,wrong,play

def continue_playing(play, fails):
    question=input('\nDo you want to try another word? (y/n): ')

    if question=='n' or question=='N':
        play=False
    else:
        fails=5
    
    return play, fails    