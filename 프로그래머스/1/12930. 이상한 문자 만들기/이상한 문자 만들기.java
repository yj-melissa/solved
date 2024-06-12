class Solution {
    public String solution(String s) {
        String answer = "";
        boolean flag = true;       // true : 짝수번째 알파벳
        
        s = s.toLowerCase();        // 문자열 전체 소문자로 바꾸고 시작
        
        StringBuilder sb = new StringBuilder();
        
        for (char a : s.toCharArray()) {
            if (a == ' ') {         // 1. 공백 : 다음 글자는 0번째 인덱스이므로 flag 올림
                flag = true;
            } else if (!flag) {     // 2. 홀수 인덱스 : 소문자 그대로
                flag = true;
            } else {
                a = Character.toUpperCase(a);
                flag = false;
            }
            sb.append(a);
        }
        
        answer = sb.toString();
        
        return answer;
    }
}