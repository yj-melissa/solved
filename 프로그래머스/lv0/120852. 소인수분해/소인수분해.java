import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> answer = new ArrayList<Integer>();
        int num = 2;
        
        while (n > 1) {
            if (n % num == 0) {
                answer.add(num);
                while (n % num == 0) {
                    n /= num;    
                }                
            }
            num++;
        }
        
        int[] answerArr = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            answerArr[i] = answer.get(i);
        }
        
        return answerArr;
    }
}