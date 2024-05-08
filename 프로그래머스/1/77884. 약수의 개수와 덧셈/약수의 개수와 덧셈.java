class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        for (int i = left; i <= right; i++) {
            int cnt = 1;        // 1은 반드시 자기 자신의 약수
            
            for (int j = 2; j <= i; j++) {
                if (i % j == 0) {
                    cnt++;
                }
            }
            
            if (cnt % 2 == 0) {
                answer += i;
            } else {
                answer -= i;
            }
            
        }
        return answer;
    }
}