import java.util.Arrays;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        int len = A.length;
        Arrays.sort(A);
        Arrays.sort(B);
        
        for (int i = 0; i < len; i++) {
            answer += (A[i] * B[len - i - 1]);        // 제일 큰 값 * 제일 작은 값
        }

        return answer;
    }
}