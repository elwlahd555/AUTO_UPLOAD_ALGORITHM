import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int T=Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			StringTokenizer st=new StringTokenizer(br.readLine());
			int a=Integer.parseInt(st.nextToken());
			int b=Integer.parseInt(st.nextToken());
			int answer=1;
			for (int i = 0; i < b; i++) {
				answer=answer*a;
				if(answer>=10) {
					answer%=10;
				}
				if(answer==0) {
					answer=10;
					break;
				}
			}
			System.out.println(answer);
		}
	}
}
