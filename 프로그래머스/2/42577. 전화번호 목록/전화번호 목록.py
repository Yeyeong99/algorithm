def solution(phone_book):
    # 전화번호 목록을 정렬
    phone_book.sort()
    
    # 인접한 전화번호들 비교
    for i in range(len(phone_book) - 1):
        # 앞 번호가 뒤 번호의 접두사인지 확인
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    
    return True
