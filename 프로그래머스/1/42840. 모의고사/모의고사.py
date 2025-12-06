def solution(answers):
    # 문제가 [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    first_student = [1, 2, 3, 4, 5]
    second_student = [2, 1, 2, 3, 2, 4, 2, 5]
    # print(second_student * 3)
    third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i, j in enumerate(answers):
        if j == first_student[i%len(first_student)]:
            score[0] += 1
        if j == second_student[i%len(second_student)]:
            score[1] += 1
        if j == third_student[i%len(third_student)]:
            score[2] += 1
        
    result = [idx+1 for idx, i in enumerate(score) if i == max(score)]
    result.sort()
    return result