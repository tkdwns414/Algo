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
		int minVal = Integer.MAX_VALUE;
		int maxVal = Integer.MIN_VALUE;
		while(f.hasMoreTokens()) {
			int num = Integer.parseInt(f.nextToken());
			minVal = Math.min(minVal, num);
			maxVal = Math.max(maxVal, num);
		}
		
		System.out.println(minVal + " " + maxVal);
		
		br.close();		
	}
}
