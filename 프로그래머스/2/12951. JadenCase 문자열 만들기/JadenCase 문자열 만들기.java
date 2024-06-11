class Solution {
    public String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        boolean flag = false;
        
        s = s.toLowerCase();
        
        for (char a : s.toCharArray()) {
            if (flag == false && a != ' ') {        // 첫 글자라면 대문자로 바꿔서 추가
                a = Character.toUpperCase(a);
                flag = true;
            } else {
                if (flag == true && a == ' ') {  // 어절 끝나면 flag 바꿈
                flag = false;
                }
            }
            sb.append(a);    
        }
        
        answer = sb.toString();
        
        return answer;
    }
}