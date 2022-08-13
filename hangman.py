"""First version | needs to be modified"""

guess = "abcfa"
character_list = list(guess.replace(" ", ""))
crypto_character_list = []
guess_join = guess.replace(" ", "")

for character in range(len(character_list)):
    crypto_character_list.append("_")

print(guess)
print("character_list : ", character_list)
print("crypto_character_list : ", crypto_character_list)

print("character_list : ","".join(character_list))
print("crypto_character_list : ","".join(crypto_character_list))

print(len(character_list))
print(len(crypto_character_list))

i = 1
while True:
    shot = input("Podaj literę : ")
    if shot in character_list:
        print("i : ", i)
        shot = guess_join.index(shot)
        #print("shot : ", shot)
        print(crypto_character_list)
        crypto_character_list[shot] = character_list[shot]
        print(crypto_character_list)

    else:
        print("x | " * i)
        i += 1
        if i > 3:
            print("przegrałeś")
            break

"""Book example version"""


def hangman(word):
    wrong = 0
    stages = ["",
                "----------------"
                "|              ]",
                "|              |",
                "|              |",
                "|              o",
            r'"|            /|\"',
            r'"|            / \"',
              ]
    print(len(stages))
    characters = list(word)
    board = ["__"] * len(word)
    print("Gra w wisielca")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("Odgadnij literę: ")
        if char in characters:
            i = characters.index(char)
            print("indexs : ", i)
            board[i] = char
            print("board[indexs] : ", board[i])
            characters[i] = "$"
            print("characters[indexs] : ", characters[i])
            print(characters)
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Wygrałeś!")
            print(" ".join(board))
            break

hangman("abca")