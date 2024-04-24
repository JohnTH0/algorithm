"""
바탕화면 정리
https://school.programmers.co.kr/learn/courses/30/lessons/161990
lv 1

"""
def solution(wallpaper):
    wallpaper_len = len(wallpaper)
    sort_list = list(zip(*wallpaper))
    sort_list_len = len(sort_list)
    # #의 위치 리스트
    path_list = []
    for i in range(wallpaper_len):
        for j in range(sort_list_len):
            if wallpaper[i][j] == "#":
                path_list.append([i,j])

    path_S_row = sorted(path_list, key=lambda x: x[1])[0][1]
    path_S_col = sorted(path_list, key=lambda x: x[0])[0][0]
    path_S = [path_S_col, path_S_row]
    
    path_E_row = sorted(path_list, key=lambda x: x[1],reverse=True)[0][1]+1
    path_E_col = sorted(path_list, key=lambda x: x[0],reverse=True)[0][0]+1
    path_E = [path_E_col, path_E_row]

    result = path_S + path_E

    return result

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]