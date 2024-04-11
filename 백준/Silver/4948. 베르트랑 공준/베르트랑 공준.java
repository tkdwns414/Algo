import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		int num;
		while ((num = Integer.parseInt(br.readLine())) != 0) {
			int top = 2 * num + 1;
			boolean[] arr = new boolean[top];
			Arrays.fill(arr, true);
			
			for (int i = 2; i <= (int)Math.sqrt(top); i++) {
				if (arr[i]) {
					for (int j = i*i; j < top; j+=i) arr[j] = false;
				}
			}
			
			int count = 0;
			for (int i = num + 1; i < top; i++) if (arr[i]) count += 1;
			sb.append(count).append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		return;
	}
}
