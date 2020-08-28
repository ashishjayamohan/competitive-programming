import java.io.*;
import java.util.*;
public class balance {
     public static void main(String[] args){
          Scanner sc = new Scanner(System.in);
          int t = sc.nextInt();
          String[] answers = new String[t];
          int[][] answers2 = new int[t][t];
          for(int a = 0; a < t; a ++){
               int b = sc.nextInt();
               if(b % 4 == 0){
                    answers[a] = "NO";
               }
               else{
                    answers[a] = "YES\n" + generateList(b);
               }
          }
          for(int c = 0; c < answers.length; c ++){
               System.out.println(answers[c]);
          }
     }
     public static String generateList(int n){
          int[] answer = new int[n];
          for (int a = 0; a < n; a ++){
               if((a + 1) % 2 == 0){
                    answer[a + (n/2)] = a + 1;
               }
               else {
                    answer[a] = a + 1;
               }
          }
          answer[answer.length - 1] += (n/2);
          String final = "";
          for(int b = 0; b < answer.length; b ++){
               final += answer[b];
          }
          return final;
     }
}
