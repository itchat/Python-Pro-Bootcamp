import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

word_len = len(chosen_word)

display_list = []


def main() -> None:
    init()
    life = 0
    while not is_game_end():
        if life < len(hangman) - 1:
            print(hangman[life])
        else:
            print(hangman[-1])
            print("Game over.")
            break
        guess_letter = input("Guess a letter: ").lower()
        if guess_letter not in chosen_word:
            life = life + 1
        for i in range(word_len):
            if chosen_word[i] == guess_letter:
                display_list[i] = guess_letter
            else:
                pass
        print(display_list)
    print("Congratulations! You Win.")

# initialize an list full of "_"


def init() -> None:
    for _ in range(word_len):
        display_list.append("_")

# a game end checker


def is_game_end() -> bool:
    if "_" in display_list:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
