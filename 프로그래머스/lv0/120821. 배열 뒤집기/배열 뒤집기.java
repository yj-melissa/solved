class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        for (int i = num_list.length - 1, j=0; i > -1; i--)
            answer[j++] = num_list[i];
        return answer;
    }
}