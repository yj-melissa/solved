class Solution {
    public long solution(long n) {
        long answer = -1;
        int i = 1;
        long value = 0;
        
        while (value < n) {
            value = (long)Math.pow(i, 2);
            i++;
            if (value == n) {
                answer = (long)Math.pow(i, 2);             
                break;
            }              
            
        }
        return answer;
    }
}