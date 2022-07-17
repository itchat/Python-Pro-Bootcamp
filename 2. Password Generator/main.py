import random

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '+']


def pass_generator(i: int, j: int, k: int) -> list:
    return random.sample(alpha, i) + random.sample(numbers, j) + random.sample(symbols, k)


def main(i: int, j: int, k: int) -> list:
    result = ""
    pass_list = pass_generator(i, j, k)
    random.shuffle(pass_list)
    for i in pass_list:
        result = result + i
    return result


if __name__ == "__main__":
    print(main(4, 4, 4))
