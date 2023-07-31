class Solution {
    public int[][] solution(int[] num_list, int n) {
        int len = num_list.length / n;
        int[][] answer = new int[len][n];
        
        for (int i = 0; i < num_list.length; i++) {
            int a = i / n;
            int b = i % n;
            answer[a][b] = num_list[i];
        }
        
        return answer;
    }
}