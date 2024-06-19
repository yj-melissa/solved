class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for (char c : s.toCharArray()) {
            if (c == ' ') {
                answer += c;
            } else if ('A' <= c && c <= 'Z') {
                answer += (char)('A' + (c + n - 'A') % 26);
            } else {
                answer += (char)('a' + (c + n - 'a') % 26);
            }
            
        }
        
        return answer;
    }
}