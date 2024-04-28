import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Queue;
import java.util.Stack;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static boolean[] visited;
	static int N;
	static int M;
	static ArrayDeque<Integer> result = new ArrayDeque<Integer>(); 
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] s = br.readLine().split(" ");
		N = Integer.parseInt(s[0]);
		M = Integer.parseInt(s[1]);
		
		visited = new boolean[N];
		solve(0, N, M);
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}
	
	private static void solve(int l, int n, int m) {
		if (l == m) {
			for(int item: result)
				sb.append(item).append(" ");
			sb.append("\n");
			return;
		}
		
		for (int i = 0; i < n; i++) {
			if (!visited[i]) {
				visited[i] = true;
				result.add(i + 1);
				solve(l+1, n, m);
				visited[i] = false;
				result.removeLast();
			}
		}
	}
}
