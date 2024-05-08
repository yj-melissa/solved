import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {      // 숫자가 한 개만 있으면 [-1] 반환
            int[] answer = {-1};
            return answer;
        }
        
        int[] answer = new int[arr.length - 1];
        int min = Arrays.stream(arr).min().getAsInt();      // 배열의 최솟값
        int i = 0;
        
        for (int num : arr) {
            if (num == min) {           // 최소 숫자는 제외
                continue;
            }
            answer[i] = num;
            i++;
        }
        
        return answer;
    }
}