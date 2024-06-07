class Solution {
    public int[] solution(int n, int m) {
        int[] answer = {1, 1};
        
        // 최대공약수
        for (int i = 2; i < n * m; i++) {
            while ((n % i == 0) && (m % i == 0)) {
                n /= i;
                m /= i;
                answer[0] *= i;
            }
        }
        
        // 최소공배수 = 최대공약수 * n의 나머지 * m의 나머지        
        answer[1] = answer[0] * n * m;
        
        
        return answer;
    }
}