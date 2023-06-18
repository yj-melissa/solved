def solution(wallpaper):
    len_col = len(wallpaper[0])
    lux = luy = 50      # 시작점(lux, luy)
    rdx = rdy = 0       # 끝점(rdx, rdy)
    
    for row in range(len(wallpaper)):
        for col in range(len_col):
            if wallpaper[row][col] == '#':
                if row < lux:       # 더 낮은 줄이라면 시작 세로점 변경
                    lux = row
                if row > rdx:       # 더 높은 줄이라면 끝 세로점 변경
                    rdx = row
                if col < luy:       # 더 왼쪽이라면 시작 가로점 변경
                    luy = col
                if col > rdy:       # 더 오른쪽이라면 끝 가로점 변경
                    rdy = col
    
    
    return [lux, luy, rdx + 1, rdy + 1]