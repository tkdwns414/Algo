import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String args[]) throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] buckets = new int[N];
		for (int i = 0; i < N; i ++)
			buckets[i] = i+1;
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st2.nextToken());
			int b = Integer.parseInt(st2.nextToken());
			int temp;
			
			temp = buckets[a-1];
			buckets[a-1] = buckets[b-1];
			buckets[b-1] = temp;
		}
		
		for (int i = 0; i < N; i++) {
			sb.append(buckets[i]).append(" ");
		}
		System.out.print(sb.toString());
		
		br.close();		
	}
}
