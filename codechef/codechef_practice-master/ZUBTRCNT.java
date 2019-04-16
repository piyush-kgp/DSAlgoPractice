
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner scr = new Scanner(System.in);
        int t = scr.nextInt();
        int tr = t;
        while(t>0){
            int L = scr.nextInt();
            int K = scr.nextInt();
            int valTr = (L-K+1)*(L-K+2)/2;
            System.out.println("Case " + (tr-t+1) + ": " + valTr);
            t--;
        }
    }
}