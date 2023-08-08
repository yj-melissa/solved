class Solution {
    public int solution(int n) {
        int answer = n > 3 ? (n / 2) - 1 : 0; // 2를 제외한 짝수는 다 합성수
        
        if (n >= 9) {
            for (int i = 9; i <= n;) {
                for (int j = i - 1; j > 2; j--) {
                    if ((i % j) == 0) {
                        answer++;
                        break;
                    }
                }
                i += 2;
            }
            
        }
        
        return answer;
    }
}