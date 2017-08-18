import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.*;

public class Solution {

    static int solve(int n, int p){
        ArrayList<Integer> pages = new ArrayList<Integer>();
        for(int i = 0; i <= n; i++) {
            if(i % 2 == 0) { pages.add(i); } // only keep evens
        }

        if(p % 2 == 1) { p--; }
        int index = pages.indexOf(p);
            
        int result = Math.min(index, pages.size() - index - 1);
        return result;
          
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int p = in.nextInt();
        int result = solve(n, p);
        System.out.println(result);
    }
}
