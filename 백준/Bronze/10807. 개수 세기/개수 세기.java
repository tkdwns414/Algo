import java.util.Scanner;

public class Main {
	
	public static void main(String args[]) {
		int answer = 0;
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[] nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}
		int target = sc.nextInt();
		
		for (int i = 0; i < N; i++) {
			if (nums[i] == target) answer +=1;
		}
		System.out.println(answer);
	}
}
