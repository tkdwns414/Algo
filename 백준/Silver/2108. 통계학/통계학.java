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
		
		int num = Integer.parseInt(br.readLine());
		int[] arr = new int[8001]; // -4000 ~ 4000
		Arrays.fill(arr, 0);
		
		double sum = 0;
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		
		for (int i = 0; i < num; i++) {
			int n = Integer.parseInt(br.readLine());
			arr[n + 4000] += 1;
			
			sum += n;
			if (max < n) max = n;
			if (min > n) min = n;
		}
		int median = 0;
		int mode = 0;
		int count = 0;
		int mode_max = 0;
		boolean flag = false;	 
		
		for(int i = min + 4000; i <= max + 4000; i++) {
			if(arr[i] > 0) {
				if(count < (num + 1) / 2) {
					count += arr[i];
					median = i - 4000;
				}
				
				if(mode_max < arr[i]) {
					mode_max = arr[i];
					mode = i - 4000;
					flag = true;
				}
				else if(mode_max == arr[i] && flag == true) {
					mode = i - 4000;
					flag = false;					
				}
			}
		}
		sb.append(Math.round(sum/num)).append("\n");
		sb.append(median).append("\n");
		sb.append(mode).append("\n");
		sb.append(max - min).append("\n");
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		return;
	}
}
