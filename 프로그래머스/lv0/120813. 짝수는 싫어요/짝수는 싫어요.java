class Solution {
    public int[] solution(int n) {
        int len = (n % 2 == 0) ? (n / 2) : ((n / 2) + 1);
        int[] answer = new int[len];
        int i = 0;
        
        for (int num = 1; num <= n; num++) {
            if (num % 2 == 0) {
                continue;
            }
            answer[i++] = num;
        }
        
        return answer;
    }
}