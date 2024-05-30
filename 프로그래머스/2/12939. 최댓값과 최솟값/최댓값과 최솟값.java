class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split(" ");
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        
        for (String num : arr) {
            int n = Integer.parseInt(num);
            if (n > max) {
                max = n;
            }
            if (n < min) {
                min = n;
            }
        }
        answer = min + " " + max;
        return answer;
    }
}