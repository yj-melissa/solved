class Solution {
    public int[] solution(int[] numbers, String direction) {
        int[] answer = new int[numbers.length];
        int length = numbers.length;
        
        if (direction.equals("right")) {
            answer[0] = numbers[length - 1];
            for (int i = 0; i < length - 1; i++) {
                answer[i + 1] = numbers[i];
            }
            
        } else {
            answer[length - 1] = numbers[0];
            for (int i = 1; i < length; i++) {
                answer[i - 1] = numbers[i];
            }
        }
        
        return answer;
    }
}