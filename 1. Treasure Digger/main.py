row_one = ['😅', '😅', '😅']
row_two = ['😅', '😅', '😅']
row_three = ['😅', '😅', '😅']


def treasure(i, j) -> None:
    # create a double list
    treasure_map = [row_one, row_two, row_three]
    treasure_map[i - 1][j - 1] = "👹"
    changed_map = f"{row_one}\n{row_two}\n{row_three}"
    print(changed_map)


if __name__ == '__main__':
    print(f"original map: \n{row_one}\n{row_two}\n{row_three}")
    answer = input("Where you want to put the treasure.\n")
    treasure(int(answer[0]), int(answer[1]))
