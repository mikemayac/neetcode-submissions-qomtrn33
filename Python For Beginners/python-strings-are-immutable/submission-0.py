def remove_fourth_character(word: str) -> str:
    str_p1 = word[:3]
    str_p2 = word[4:]

    return str_p1 + str_p2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
