from itertools import product

def solution(word):
    vowels = ["A", "E", "I", "O", "U",""]
    number = 5
    product_list = list(product(vowels, repeat=5))
    
    word_list = sorted(list(set(map(lambda x: "".join(x), product_list))))
    for i, w in enumerate(word_list):
        if w == word:
            answer = i
    return answer