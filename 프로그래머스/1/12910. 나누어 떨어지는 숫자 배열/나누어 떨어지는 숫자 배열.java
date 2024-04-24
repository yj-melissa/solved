import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> answer = new ArrayList<>();
        Arrays.sort(arr);
        
        for (int num : arr) {
            if (num % divisor == 0) {
                answer.add(num);
            }
        }
        
        if (answer.size() == 0) {
            answer.add(-1);
        }
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}