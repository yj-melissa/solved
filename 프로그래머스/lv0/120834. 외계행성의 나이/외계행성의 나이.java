class Solution {
    public String solution(int age) {
        String answer = "";
        int a = 'a';
        
        for (int i = age; i > 0; i /= 10) {
            int num = i % 10;
            char tmp = (char) (a + num);
            answer = tmp + answer;
        }
        
        return answer;
    }
}