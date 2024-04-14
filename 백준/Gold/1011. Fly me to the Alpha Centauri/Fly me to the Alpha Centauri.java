import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < T; i++) {
			String[] s = br.readLine().split(" ");
			int x = Integer.parseInt(s[0]);
			int y = Integer.parseInt(s[1]);
			
			int dis = y - x;
			int n = (int)Math.sqrt(dis - 1);
			
			if (n*n < dis && dis <= n*(n+1)) 
				sb.append(2 * n).append("\n");
			else
				sb.append(2 * n + 1).append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		return;
	}
}
