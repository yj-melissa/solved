import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < my_string.length(); i++) {
            int num = my_string.charAt(i) - '0';
            
            if (num < 10) {
                answer.add(num);
            }
        }
        
        Collections.sort(answer);
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}