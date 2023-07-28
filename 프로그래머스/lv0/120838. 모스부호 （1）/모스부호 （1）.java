import java.util.*;

class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] codes = letter.split(" ");
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        List<String> morseList = Arrays.asList(morse);
        
        for (int i = 0; i < codes.length; i++) {
            answer += (char) ('a' + morseList.indexOf(codes[i]));
        }
        return answer;
    }
}