class Solution {
    public String solution(String rsp) {
        String answer = "";
        
        for (int i = 0; i < rsp.length(); i++) {
            char c = rsp.charAt(i);
            String r = String.valueOf(c);
            
            if (r.equals("2"))
                answer += "0";
            else if (r.equals("0"))
                answer += "5";
            else
                answer += "2";
        }
        return answer;
    }
}