import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        double avg = Arrays.stream(numbers).average().orElse(0);
        return avg;
    }
}