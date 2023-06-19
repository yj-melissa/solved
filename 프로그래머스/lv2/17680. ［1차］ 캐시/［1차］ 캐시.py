from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) == cacheSize:     # 캐시에 자리가 없는 경우
                cache.popleft()             # cache[0] 삭제
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
            
    
    return answer