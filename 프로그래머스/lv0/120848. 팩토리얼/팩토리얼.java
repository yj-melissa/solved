class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] factorials = new int[11];
        factorials[0] = 1;
        
        for (int i = 2; factorials[i-2] <= n; i++) {
            answer++;
            factorials[i - 1] = i * factorials[i - 2];
        }
        
        
        
        return answer;
    }
}