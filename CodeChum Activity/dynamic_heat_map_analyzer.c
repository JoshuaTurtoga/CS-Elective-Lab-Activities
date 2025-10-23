#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int n, t;
int grid[MAX][MAX];
int visited[MAX][MAX];

// Directions: up, down, left, right
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// Recursive DFS function
int dfs(int x, int y)
{
    visited[x][y] = 1;
    int size = 1; // current cell counts as 1

    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny])
        {
            if (abs(grid[nx][ny] - grid[x][y]) <= t)
            {
                size += dfs(nx, ny);
            }
        }
    }

    return size;
}

int main()
{
    printf("Enter n and t: ");
    scanf("%d %d", &n, &t);

    printf("Enter the grid:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &grid[i][j]);
        }
    }

    // Initialize visited array
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            visited[i][j] = 0;
        }
    }

    int largest_zone = 0;
    int start_row = 0, start_col = 0;

    // Explore all cells
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j])
            {
                int size = dfs(i, j);
                if (size > largest_zone)
                {
                    largest_zone = size;
                    start_row = i;
                    start_col = j;
                }
            }
        }
    }

    printf("Largest stable zone found at (%d, %d) with size: %d\n", start_row, start_col, largest_zone);
    return 0;
}