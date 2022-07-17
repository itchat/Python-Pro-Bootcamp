import random
from hangman_art import stages, logo
from hangman_words import word_list

# 打印 Hangman Logo
print(logo)

# 用于判断循环是否结束
game_is_finished = False

# Hangman 血量计数，0 开始，减一滴血
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

# 初始化 _ 列表
for _ in range(word_length):
    display += "_"

# 循环开始，设置死亡开关
while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    # 避免重复尝试检查是否已经改过了
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # 用 string.join function 让列表正常化显示
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        # if 的嵌套设计，改变开关参数
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    # not 在前在后都一样 if "_" not in display 
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
