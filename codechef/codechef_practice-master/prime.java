import java.util.*;
class Prime{
    public static void main(String[] args){
        Scanner scr = new Scanner(System.in);
        int n = scr.nextInt();
        boolean isPrime = true;
        for(int i = 2; i<=n/2; i++){
            if(n%i==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime){
            System.out.println("PRIME");
        }else{
            System.out.println("COMPOSITE");
        }
    }
}
