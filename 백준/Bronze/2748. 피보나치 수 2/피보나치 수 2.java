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
	static ArrayList<Long> arr = new ArrayList<Long>();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		arr.add(0L);
		arr.add(1L);
		
		for (int i = 1; i < n; i++) {
			arr.add(arr.get(i) + arr.get(i-1));
		}
		
		sb.append(arr.get(n));
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}
	
}
