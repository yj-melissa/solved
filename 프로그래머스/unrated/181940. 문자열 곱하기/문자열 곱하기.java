class Solution {
    public String solution(String my_string, int k) {
        String answer = "";
        for (int i = k; i > 0; i--) {
            answer += my_string;
        }
        return answer;
    }
}