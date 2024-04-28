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
	static StringBuilder sb;
	static long[] arr;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		arr = new long[2*n];
		
		arr[0] = 1; arr[1] = 2;
		
		for (int i = 2; i < n; i++) {
			arr[i] = (arr[i-1] + arr[i-2]) % 10007;
		}
		
		sb.append(arr[n-1]);
		
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}
}
