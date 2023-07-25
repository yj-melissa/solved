class Solution {
    public int solution(int a, int b) {
        int ab = Integer.valueOf("" + a + b);
        int ba = Integer.valueOf("" + b + a);
        
        return ab >= ba ? ab : ba;
    }
}