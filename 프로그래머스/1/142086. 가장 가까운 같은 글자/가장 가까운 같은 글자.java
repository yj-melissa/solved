import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        char[] characters = s.toCharArray();
        int[] latest = new int[26];     // 알파벳별 최신 인덱스 모음
        
        for (int i = 0; i < 26; i++) {
            latest[i] = -1;
        }
        
        for (int i = 0; i < s.length(); i++) {
            int idx = characters[i] - 'a';      // 해당 알파벳 인덱스 확인
            if (latest[idx] > -1) {
                answer[i] = i - latest[idx];            // 앞에 같은 글자 있을 경우             
            } else {
                answer[i] = -1;
            }
            latest[idx] = i;                    // 최신 인덱스 갱신
        }
        
        
        return answer;
    }
}