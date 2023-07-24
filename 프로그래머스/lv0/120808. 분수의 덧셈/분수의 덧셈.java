class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {0, 0};
        
        // 1. 공통 분모 구하기 
        // 1.1 denom1, 2 중 큰 값부터 차례로 탐색
        int denom = denom1 >= denom2 ? denom1 : denom2;
        for (int i = denom; i <= denom1 * denom2; i++) {
            // 1.2 둘의 공통 분모 구하면 answer[1] 업데이트
            if ((i % denom1 == 0) && (i % denom2 == 0)) {
                answer[1] = i;
                break;
            }            
        }
        
        // 2. 분자 구하기
        // 2.1 answer[0] += numer * (answer[1] / denom)
        answer[0] += numer1 * (answer[1] / denom1);
        answer[0] += numer2 * (answer[1] / denom2);
        
        // 3. 기약분수화
        int t = answer[0] >= answer[1] ? answer[0] : answer[1];
        for (int i = t; i >= 2; i--) {
            if ((answer[0] % i == 0) && (answer[1] % i == 0)) {
                answer[0] /= i;
                answer[1] /= i;
            }
        }
        
        return answer;
    }
}