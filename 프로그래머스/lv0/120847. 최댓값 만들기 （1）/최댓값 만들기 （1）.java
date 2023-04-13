class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        for (int i = 0; i < numbers.length ; i++) {
            int x = numbers[i];
            for (int j = i+1; j < numbers.length ; j++) {
                int temp = x * numbers[j];
                if (answer < temp) {
                    answer = temp;
                }
            }
        }
        return answer;
    }
}