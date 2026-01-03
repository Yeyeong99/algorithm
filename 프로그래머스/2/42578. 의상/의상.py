from itertools import product, combinations
def solution(clothes):
    clothes_dict = {}
    for name, category in clothes:
        clothes_dict.setdefault(category, 1)
        clothes_dict[category] += 1
    counter = 1
    for value in clothes_dict.values():
        counter *= value
        

    return counter - 1