import java.util.*;
 
class Ordteams{
 
    public static boolean checker(int[] arr1, int[] arr2){
        int arr1sum, arr2sum;
        arr1sum = arr2sum = 0;
        boolean g1[] = new boolean[3];
        boolean g2[] = new boolean[3];
        for(int i=0; i<=2; i++){
            arr1sum+=arr1[i];
            arr2sum+=arr2[i];
            g1[i] = arr1[i]>=arr2[i];
            g2[i] = arr2[i]>=arr1[i];
        }
        if(arr1sum>arr2sum && g1[0]==true && g1[1]==true && g1[2]==true){
            return(true);
        }
        if(arr2sum>arr1sum && g2[0]==true && g2[1]==true && g2[2]==true){
            return(true);
        }
        return(false);
    }
 
    public static void main(String[] args){
        Scanner scr = new Scanner(System.in);
        int t = scr.nextInt();
        while(t>0){
                int[] st1 = new int[3]; int[] st2 = new int[3]; int[] st3 = new int[3];
	        for(int i = 0; i<=2; i++){
	            st1[i] = scr.nextInt();
	        }
	        for(int i = 0; i<=2; i++){
	             st2[i] = scr.nextInt();
	        }
	        for(int i = 0; i<=2; i++){
	            st3[i] = scr.nextInt();
	        }
	        
	        boolean a = checker(st1, st2);
	        boolean b = checker(st2, st3);
	        boolean c = checker(st3, st1);
	        
	        if(a==true && b==true && c==true){
	            System.out.println("yes");
	        }else{
	            System.out.println("no");
	        }
	 
	        t--;
        }
    }
} 
