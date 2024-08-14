import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		String[] s = br.readLine().split(" ");
		long a = Long.parseLong(s[0]);
		long b = Long.parseLong(s[1]);
		sb.append(a * b / gcd(a,b)).append("\n");
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		return;
	}
	
	private static long gcd(long x, long y) {
		if (y == 0)
			return x;
		return gcd(y, x % y);
	}

}
