import java.util.*;

class Solution {
    public String solution(String s) {
        String[] sArr = s.split("");
        
        Arrays.sort(sArr, Collections.reverseOrder());       
        
        String answer = String.join("", sArr);
        
        return answer;
    }
}