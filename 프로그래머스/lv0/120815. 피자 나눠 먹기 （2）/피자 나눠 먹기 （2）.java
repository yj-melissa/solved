class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 6; i <= n * 6; i += 6) {
            if (i % n == 0) {
                answer = (int) (i / 6);
                break;
            }
        }
        return answer;
    }
}