import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int t = in.nextInt();
        int a = in.nextInt();
        int b = in.nextInt();
        int m = in.nextInt();
        int n = in.nextInt();
        
        int[] app_d = new int[m];
        int[] ora_d = new int[n];
        
        int appCount = 0;
        int oraCount = 0;
        
        int[] apple = new int[m];
        for(int apple_i=0; apple_i < m; apple_i++){
            apple[apple_i] = in.nextInt();
            app_d[apple_i] = a + apple[apple_i]; 
        }
        int[] orange = new int[n];
        for(int orange_i=0; orange_i < n; orange_i++){
            orange[orange_i] = in.nextInt();
            ora_d[orange_i] = b + orange[orange_i]; 
        }
        
        for(int i = 0; i < m; i++) {
            if(app_d[i] >= s && app_d[i] <= t) appCount++;
        }
        for(int j = 0; j < n; j++) {
            if(ora_d[j] >= s && ora_d[j] <= t) oraCount++; 
        }       
        
        System.out.println(appCount);
        System.out.println(oraCount);  
    }
}
