import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String f = br.readLine();
		int N = Integer.parseInt(f.split(" ")[0]);
		int X = Integer.parseInt(f.split(" ")[1]);
		String num = br.readLine();
		
		StringTokenizer st = new StringTokenizer(num);
		StringBuilder sb = new StringBuilder();
		while (st.hasMoreTokens()) {
			int n = Integer.parseInt(st.nextToken());
			if (n < X) sb.append(n).append(" ");
		}
		System.out.println(sb.toString());
		br.close();
		
	}
}
