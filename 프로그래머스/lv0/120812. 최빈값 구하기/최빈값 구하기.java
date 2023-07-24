class Solution {
    public int solution(int[] array) {
        int[] cntList = new int[1000];      // 등장 횟수 셀 배열
        
        // 1. 숫자 등장 횟수 확인
        for (int a : array) {
            cntList[a] += 1;
        }
        
        // 2. 제일 높은 횟수 확인
        int maxFrequency = 0;           // 최대 빈도수
        int answer = 0;                 // 최빈값
        boolean isMultiple = false;                    // 빈도 등장 횟수
        
        for (int i = 0; i < cntList.length; i++) {
            if (cntList[i] > maxFrequency) {
                maxFrequency = cntList[i];
                answer = i;
                isMultiple = false;
            } else if (cntList[i] == maxFrequency) {
                isMultiple = true;
            } else {
                continue;
            }
        }
    
    return isMultiple == true? -1 : answer;
    }
}