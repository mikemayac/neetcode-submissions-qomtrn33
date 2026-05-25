from typing import List

def read_integers() -> List[int]:
    user_input = input()
    string_list = user_input.split(",")
    num_list = []
    for elem in string_list:
        num_list.append(int(elem))
    return num_list
    
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
