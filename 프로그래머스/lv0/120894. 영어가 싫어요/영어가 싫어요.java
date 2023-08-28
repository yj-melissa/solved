import java.util.*;

class Solution {
    public long solution(String numbers) {
        String answer = "";
        
        Map<String, Integer> numMap = new HashMap<>();
        String[] numWords = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
        for (int i = 0; i < 10; i++) {
            numMap.put(numWords[i], i);
        }
        
        String word = "";
        
        for (int i = 0; i < numbers.length(); i++) {
            word += numbers.charAt(i);
            if (numMap.containsKey(word)) {
                answer += numMap.get(word);
                word = "";
            }
        }
        
        
        
        
        return Long.parseLong(answer);
    }
}