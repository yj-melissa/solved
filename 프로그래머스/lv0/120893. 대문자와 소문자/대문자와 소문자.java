class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for (int i = 0; i < my_string.length(); i++) {
            char c = my_string.charAt(i);
            
            if ('a' <= c && c <= 'z') {
                int tmp = (int) c - 'a';
                answer += (char) (tmp + 'A');
            } else {
                int tmp = (int) c - 'A';
                answer += (char) (tmp + 'a');
            }
            
            
        }
        
        return answer;
    }
}