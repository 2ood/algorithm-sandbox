import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
        StringTokenizer tk = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(tk.nextToken());
        int m = Integer.parseInt(tk.nextToken());
        
        k = new int[n][m];
        
        for(int i=0;i<n;i++) {
            tk = new StringTokenizer(br.readLine());
            for(int j=0;j<m;j++) {
                k[i][j]=Integer.parseInt(tk.nextToken());
            }
        }
        
        int maxSum=0;
        int tmpSum=0;
        
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {

               
            }
        }
        
        
    }
    
    
}