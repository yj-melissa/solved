import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        Stack<Integer> stack = new Stack<>();
        for (int a : arr) {
            if (!stack.empty() && stack.peek() == a) {
                
            } else {
                stack.push(a);
            }
        }
        
        int size = stack.size();
        
        int[] answer = new int[size];
        
        for (int i = 0; i < size; i++) {
            answer[size - i - 1] = stack.pop();
        }
        

        return answer;
    }
}