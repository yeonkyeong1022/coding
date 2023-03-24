#include <stdio.h>
#include <time.h>
#define MAX_TERMS 501
#define MAX_COL 501

typedef struct
{
    int col;
    int row;
    int value;
} term;

term a[MAX_TERMS];
term b[MAX_TERMS];

void FAST_TRANS(term a[], term b[])
{
    int row_terms[MAX_COL];
    int starting_pos[MAX_COL];
    int i, j;
    int num_cols = b[0].row = a[0].col;
    int num_terms = b[0].value = a[0].value;
    b[0].col = a[0].row;

    if (num_terms > 0)
    {
        for (i = 0; i < num_cols; i++)
            row_terms[i] = 0;
        for (i = 1; i <= num_terms; i++)
            row_terms[a[i].col]++;
        starting_pos[0] = 1;
        for (i = 1; i < num_cols; i++)
            starting_pos[i] = starting_pos[i - 1] + row_terms[i - 1];
        for (i = 1; i <= num_terms; i++)
        {
            j = starting_pos[a[i].col]++;
            b[j].row = a[i].col;
            b[j].col = a[i].row;
            b[j].value = a[i].value;
        }
    }
}

void SIMPLE_TRANS(term a[], term b[])
{
    int n, i, j, currentb;
    n = a[0].value;
    b[0].row = a[0].col;
    b[0].col = a[0].row;
    b[0].value = n;
    if (n > 0)
    {
        currentb = 1;
        for (i = 0; i < a[0].col; i++)
            for (j = 1; j <= n; j++)
                if (a[j].col == i)
                {
                    b[currentb].row = a[j].col;
                    b[currentb].col = a[j].row;
                    b[currentb].value = a[j].value;
                    currentb++;
                }
    }
}

int main()
{

    int i;
    for (i = 0; i < MAX_COL; i++)
    {
        a[i].row = i;
        a[i].col = i;
        a[i].value = 1;
    }

    clock_t start = clock();
    for (i = 0; i < 1000; i++)
    {
        FAST_TRANS(a, b);
    }
    clock_t end = clock();

    clock_t start2 = clock();
    for (i = 0; i < 1000; i++)
    {
        SIMPLE_TRANS(a, b);
    }
    clock_t end2 = clock();

    printf("FAST_TRANS: %lf\n", (double)(end - start) / CLOCKS_PER_SEC);
    printf("SIMPLE_TRANS: %lf\n", (double)(end2 - start2) / CLOCKS_PER_SEC);
}
