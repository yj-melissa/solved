class Solution {
    public int solution(int n, int k) {
        int lamb = 12000 * n;
        int drink = 2000 * (k - (n / 10));
        return lamb + drink;
    }
}