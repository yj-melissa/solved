import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        char[] sArray = s.toCharArray();
        Arrays.sort(sArray);
        
        for (int i = 0; i < s.length(); i++) {
            int cnt = 0;
            
            for (int j = i + 1; j < s.length(); j++) {
                if (sArray[i] == sArray[j]) {
                    cnt++;
                } else {
                    break;
                }
            }
            
            if (cnt == 0) {
                answer += sArray[i];
            }
            
            i += cnt;
        }

        return answer;
    }
}