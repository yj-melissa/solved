class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        
        long pNum = Long.valueOf(p);      // p가 나타내는 수
        int pLen = p.length();
        
        for (int i = 0; i < t.length() - pLen + 1; i++) {
            String tPartial = t.substring(i, i + pLen);
            long tNum = Long.valueOf(tPartial);     // p의 최대 길이는 10,000
            
            if (tNum <= pNum) {
                answer++;
            }
        }
        
        
        return answer;
    }
}