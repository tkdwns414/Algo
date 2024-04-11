import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
		int num = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < num; i++) {
			ArrayList<Integer> temp = new ArrayList<>();
			String[] s = br.readLine().split(" ");
			
			temp.add(Integer.parseInt(s[0]));
			temp.add(Integer.parseInt(s[1]));
			temp.add(1);
			
			arr.add(temp);
		}
		
		for (int i = 0; i < num; i++) {
			for (int j = 0; j < num; j++) {
				if (i != j) {
					if (arr.get(i).get(0) < arr.get(j).get(0) && arr.get(i).get(1) < arr.get(j).get(1)) {
						arr.get(i).set(2, arr.get(i).get(2) + 1);
					}
				}
			}
		}
		
		for (ArrayList<Integer> item : arr) {
			bw.write(item.get(2).toString() + " ");
		}
		
		bw.flush();
		bw.close();
		return;
	}
}
