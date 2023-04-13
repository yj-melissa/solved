import java.util.*;
class Solution {
    public int[] solution(int[] num_list) {
        int odd = (int) Arrays.stream(num_list).filter(n -> n%2 == 1).count();
        int[] answer = {num_list.length-odd, odd};
        return answer;
    }
}