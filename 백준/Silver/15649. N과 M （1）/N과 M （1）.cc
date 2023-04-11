#include <stdio.h>

using namespace std;

int N, M;
int visited[9];
int result[9];
void dfs(int n, int cnt) {
	if (cnt == M+1) {
		for (int i = 1; i <= M; i++)
		{
			printf("%d ", result[i]);
		}
		printf("\n");
	}
	for (int i = 1; i <= N; i++)
	{
		if (visited[i] == 1) {
			continue;
		}
		visited[i] = 1;
		result[cnt] = i;
		dfs(n, cnt + 1);
		visited[i] = 0;
	}
}
int main() {
	scanf("%d%d", &N, &M);
	dfs(1, 1);
	return 0;
}