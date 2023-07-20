class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        
        for (int i = 0; i < my_string.length(); i++) {
            if (i == s) {       // overwirte_string으로 대체
                answer += overwrite_string;
                i += overwrite_string.length() - 1;     // 첫 글자는 이미 for문에서 더해짐
                continue;
            }
            answer += my_string.charAt(i);
        }
        return answer;
    }
}