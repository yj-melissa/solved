class Solution {
    public String solution(String my_string) {
        String answer = "";
        String vowels = "aeiou";
        
        for (int i = 0; i < my_string.length(); i++) {
            String s = String.valueOf(my_string.charAt(i));
            if (vowels.contains(s)) {
                continue;
            }
            answer += s;
        }
        
        
        return answer;
    }
}