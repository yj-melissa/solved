import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int answer = 101;
        int distance = 101;
        
        for (int a : array) {
            if (Math.abs(a - n) < distance) {
                distance = Math.abs(a - n);
                    answer = a;
            } else if (Math.abs(a - n) == distance) {
                if (a < answer) {
                    answer = a;
                }
            }
        }
        
        return answer;
    }
}