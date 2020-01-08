Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hangman(word):
    wrong=0
    stages=['',
            '--------          ',
            '|       |         ',
            '|       |         ',
            '|       0         ',
            '|      /|/        ',
            '|      //         ',
            '|                 '
           ]
    rletters=list(word)
    board=['--']*len(word)
    win=False
    print('Welcome to Hangman')
    while wrong<len(stages)-1:
        print('\n')
        msg="Guess a letter"
        char=input(msg)
        
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong+=1
        print((''.join(board)))
        print('\n'.join(stages[0:wrong+1]))
        if'--'not in board:
            print('you win! It was:')
            print(' '.join(board))
            win=True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('you lose! It was {}'.format(word))
        
hangman('cat')
#안녕이라고 써볼게
print('hello')
