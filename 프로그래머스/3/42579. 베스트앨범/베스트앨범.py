def solution(genres, plays):
    genre_plays_list = []
    genre_plays_dict = {}

    for idx, item in enumerate(zip(genres, plays)):
        genre, play = item
        genre_plays_dict.setdefault(genre, 0)
        genre_plays_dict[genre] += play
        
    for idx, item in enumerate(zip(genres, plays)):
        genre, play = item
        genre_plays_list.append((idx, genre, play, genre_plays_dict[genre]))

    # 전체 플레이수 + 개별 플레이 수 순서로 내림차순(reverse) 정렬
    genre_plays_list.sort(key=lambda x:(x[3], x[2]), reverse=True)
    answer = []
    # 두 번 출력되었는지 세기 위한 딕셔너리
    answer_genre = {genre: 0 for genre in genres} 
    for music in genre_plays_list:
        genre = music[1]
        idx = music[0]
        if answer_genre[genre] == 2:
            continue
        answer.append(idx)
        answer_genre[genre] += 1
    
    return answer