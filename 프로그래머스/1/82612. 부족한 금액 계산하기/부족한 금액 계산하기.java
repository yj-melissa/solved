class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long sum = 0;
        
        for (int i = 1; i <= count; i++) {
            // System.out.println("현재 : " + i + "번째 " + money + "원, 이용료 : " + i * price);
            sum += price * i;
            // System.out.println("차감 후 : " + money);
        }
        
        if (sum > money) {
            answer = sum - money;
        }

        return answer;
    }
}