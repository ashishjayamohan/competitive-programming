import java.io.*;
import java.util.*;
import java.lang.Math;
public class wa6 {
     public static void Main(String[] args){
          Scanner sc = new Scanner(System.in);
          String[] line = sc.nextLine().split(" ");
          int n = Integer.parseInt(line[0]);
          int m = Integer.parseInt(line[1]);
          int answer = ((int)Math.pow(n,m-2)%m);
          System.out.println(answer);
     }
}
