import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String args[]) throws IOException {
		String f = br.readLine();
		int N = Integer.parseInt(f.split(" ")[0]);
		int M = Integer.parseInt(f.split(" ")[1]);
		int[] buckets = new int[N];
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken()) - 1;
			int end = Integer.parseInt(st.nextToken()) - 1;
			int num = Integer.parseInt(st.nextToken());
			for (int j = start; j <= end; j++) {
				buckets[j] = num;
			}
		}
		
		for (int i = 0; i < N; i++) {
			sb.append(buckets[i]).append(" ");
		}
		System.out.print(sb.toString());
		
		br.close();		
	}
}
