import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int num = Integer.parseInt(br.readLine());
		ArrayDeque<Integer> stk = new ArrayDeque<>();
		
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
