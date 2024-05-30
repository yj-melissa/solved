class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int top = -1;
        
        for (int i = 0; i < s.length(); i++) {
            char bracket = s.charAt(i);
            if (bracket == '(') {
                top++;
            } else {
                if (top < 0) {      // 닫는 괄호 나왔으나 여는 괄호 없는 경우
                    answer = false;
                    break;
                } else {
                    top--;
                }
            }
        }
        
        if (top > -1) {         // 문자열 끝났을 때 여는 괄호 남아있는 경우
            answer = false;
        }

        return answer;
    }
}