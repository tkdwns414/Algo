import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String args[]) throws IOException {
		int N = Integer.parseInt(br.readLine());
		StringTokenizer f = new StringTokenizer(br.readLine());
		int len = f.countTokens();
		int max = Integer.MIN_VALUE;
		int sum = 0;
		
		while(f.hasMoreTokens()) {
			int num = Integer.parseInt(f.nextToken());
			max = Math.max(max, num);
			sum += num;
		}
		
		System.out.println((double)sum/max/len*100);
		
		br.close();		
	}
}
