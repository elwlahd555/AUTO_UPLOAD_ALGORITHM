#include <stdio.h>

using namespace std;

int N, M;

int visited[8];
int result[8];

void dfs(int cnt) {
	if (cnt == M+1) {
		for (int i = 1; i <= M; i++)
		{
			printf("%d ", result[i]);
		}
		printf("\n");
		return;
	}
	for (int i = 1; i <= N; i++)
	{
		result[cnt] = i;
		dfs(cnt + 1);
	}
}
int main() {

	scanf("%d%d", &N, &M);
	dfs(1);

	return 0;
}