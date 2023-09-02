
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = 4;
		for (int i = 0; i < n; i++) {
			int x, y, p, q;
			int xx, yy, pp, qq;
			x = sc.nextInt();
			y = sc.nextInt();
			p = sc.nextInt();
			q = sc.nextInt();

			xx = sc.nextInt();
			yy = sc.nextInt();
			pp = sc.nextInt();
			qq = sc.nextInt();
			if (xx > p || yy > q || pp < x || qq < y) {
				System.out.println("d");
			} else if ((x == pp && q == yy) || (x == pp && y == qq) || (p == xx && y == qq) || (p == xx && q == yy)) {
				System.out.println("c");
			} else if (p == xx || q == yy || pp == x || y == qq) {
				System.out.println("b");
			} else {
				System.out.println("a");
			}

		}
	}
}
