import random

def hangman():
    word =random.choice(["pocket","ruin","injured","title","kettle","arc"])
    validletter = "abcdefghijklmnopqrstuvwxyz"
    turn = 10
    guessmade = ''
    while len(word)>0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("Hurrah!!")
            print("You Win")
            break
        print("Guess the word:", main)
        guess = input()

        if guess in validletter:
            guessmade = guessmade +guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            turn = turn - 1
            if turn == 9:
                print("9 turns left")
                print(" --------- ")
            if turn == 8:
                print("8 turns left")
                print(" ---------")
                print("     O      ")
            if turn == 7:
                print("7 turns left")
                print(" ---------")
                print("     O      ")
                print("     |      ")
            if turn == 6:
                print("6 turns left")
                print(" ----------")
                print("     O      ")
                print("     |      ")
                print("     /      ")
            if turn == 5:
                print("5 turns left")
                print(" ----------")
                print("     O      ")
                print("     |      ")
                print("     /\      ")
            if turn == 4:
                print("4 turns left")
                print(" ----------")
                print("  \ O      ")
                print("    |      ")
                print("    /\      ")
            if turn == 3:
                print("3 turns left")
                print(" ----------")
                print("  \ O /   ")
                print("    |      ")
                print("   /\      ")
            if turn == 2:
                print("2 turns left")
                print(" ----------")
                print("  \ O /|   ")
                print("    |      ")
                print("   /\      ")
            if turn == 1:
                print("1 turns left")
                print("Take care,you are close to death!")
                print(" ----------")
                print("  \ O_|/   ")
                print("    |      ")
                print("   /\      ")
            if turn ==0:
                print("You lose")
                print("Kind man Die")
                print(" ----------")
                print("    O_|   ")
                print("   /|\      ")
                print("   /\      ")
                break


name = input("Enter your name\n")
print("***********Welcome", name,"*********" )
print("--------------")
print("Try to guess the word in 10 attempts ")

hangman()
print()

