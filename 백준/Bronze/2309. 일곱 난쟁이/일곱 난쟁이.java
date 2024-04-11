import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		ArrayList<Integer> arr = new ArrayList<>();
		int sum = 0;
		
		for (int i = 0; i < 9; i++) {
			int num = Integer.parseInt(br.readLine());
			arr.add(num);
			sum += num;
		}
		
		Collections.sort(arr);
		
		for (int i = 0; i < 9; i++) {
			for (int j = i + 1; j < 9; j++) {
				if (arr.get(i) + arr.get(j) == sum - 100) {
					for(int k = 0; k < 9; k++) {
						if (k != i && k != j)bw.write(arr.get(k).toString() + "\n");
					}
					bw.flush();
					bw.close();
					
					return;
				}
			}
		}
	}
}
