class Solution {
    public long solution(long n) {
        long answer = 0;
        
        int[] cntList = new int[10];
        while (n > 0) {
            int i = (int)(n % 10);
            n /= 10;
            cntList[i]++;
        }
        
        String s = "";
        
        for (int i = 9; i > -1; i--) {
            while (cntList[i] > 0) {
                s += i + "";
                cntList[i]--;
            }
        }
        
        answer = Long.parseLong(s);
        
        
        return answer;
    }
}