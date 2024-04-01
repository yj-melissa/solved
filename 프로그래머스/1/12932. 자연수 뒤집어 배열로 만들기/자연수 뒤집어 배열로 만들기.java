import java.util.List;

class Solution {
    public int[] solution(long n) {
        String s = n + "";
        int[] answer = new int[s.length()];
        int i = 0;
        while (n > 0) {
            answer[i++] = (int)(n % 10);
            n /= 10;
        }
        return answer;
    }
}