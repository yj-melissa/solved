import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            
            if ('a' <= c && c <= 'z') {
                System.out.print((char) (c - 32));
            } else {
                System.out.print((char) (c + 32));
            }
        }
        
        System.out.println();
        
    }
}