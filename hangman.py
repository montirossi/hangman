def hangman(word):
    wrong = 0
    stages = ["",
             "__________      ",
             "|        |      ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
    	print("\n")
    	msg = "Guess a letter: " + "".join(board) + "  "
    	char = input(msg)
    	if char in rletters:
    		cind = rletters.index(char)
    		board[cind] = char
    		rletters[cind] = '$'
    	else:
    		wrong += 1

    	e = wrong + 1
    	print("\n".join(stages[0:e]))

    	if "_" not in board:
    		print("You win! It was: {}.".format(word))
    		win = True
    		break

    if not win:
    	print("\n".join(stages[0:e]))
    	print("You lose! It was: {}.".format(word))

hangman("breakfast")