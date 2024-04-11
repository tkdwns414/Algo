import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int num = Integer.parseInt(br.readLine());
		Stack<Integer> stk = new Stack<>();
		
		for (int i = 0; i < num; i++) {
			int n = Integer.parseInt(br.readLine());
			if (n == 0) stk.pop();
			else stk.push(n);
		}
		
		int sum = 0;
		for (int item : stk) {
			sum += item;
		}
		
		sb.append(sum);
		System.out.println(sb);
		return;
	}
}
