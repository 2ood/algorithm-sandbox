import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
	StringTokenizer tk = new StringTokenizer(br.readLine());	
	int len = Integer.parseInt(tk.nextToken());
    StringBuilder sb = new StringBuilder();
    Arraylist nums[] = new ArrayList[len];
        
    for(int i=0;i<nums.length;i++) {
        tk = new StringTokenizer(br.readLine());
        while(tk.hasMoreTokens()) {
            nums[i].add(new Integer(tk.nextToken()));
        }
        nums[i].trimToSize();
    }
    
    for(int i=0;i<nums.length;i++) {
        sb.append(gcdSum(nums[i])).append("\n");
    }
        
    System.out.print(sb.toString());
        
    }
    
    public static int gcd (int mx, int mn) {
        if(mn>=1) return gcd(mn, mx%mn);
        else return mx;
    }
    
    public static int gcdSum(ArrayList<Integer> list) {
        int result=0;
        for(int i=0; i<list.size();i++) {
            for(int j=i; j<list.size();j++) {
                result+=gcd(Math.max(list.get(i),list.get(j)),Math.min(list.get(i),list.get(j)));
            }
        }
        
        return result;
    }
}