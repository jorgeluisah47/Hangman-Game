
#
#   Hangman project
#

import functions

def run():

    word = functions.chooseWord()
    fragment = functions.fragmentingWord(word)
    lives= 7
    lostLife = False
    newFragment = fragment
    win = False
    err = 0

    while lives > 0:
        functions.clear() 
        print(f"\n\t Guess the character - Remaining lives: {lives}")
        print(f"\n\n\t{fragment}")

        if fragment != word:

            hangman = functions.draw(err)
            print(hangman)

            letra = input("\n\n\t Enter a letter:").lower()

            for item in range(0, len(word)):
                if word[item] == letra:
                    l = list(fragment)
                    l[item] = letra
                    fragment = "".join(l)
                    print(fragment)

            if fragment != newFragment:
                newFragment = fragment
                lostLife = False
            elif fragment == newFragment:
                lostLife = True
                err += 1

        else:
            win = True
            break

        if lostLife == True:
            lives -= 1
            lostLife = False

    functions.clear()
    if win:
        print(f"\n\n Congrats!!, you won!. The word was: {fragment} \n\n\n")
    else:
        print(functions.draw(7))
        print(f"\n\n You lost. The correct word was: '{word}' \n\n\n")
    
if __name__ == "__main__":
    run()
