def solution(a, b):
    week = {2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU", 0: "FRI", 1: "SAT"}
    month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = b - 1 
    for x in range(1, a):
        days += month[x]
    answer = week[days % 7]
    return answer