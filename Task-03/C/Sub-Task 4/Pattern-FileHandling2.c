#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *infile = fopen("input.txt", "r");
    FILE *outfile = fopen("output.txt", "w");

    int n;
    fscanf(infile, "%d", &n);
    fclose(infile);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) fprintf(outfile, " ");
        for (int j = 0; j < 2 * i + 1; j++) fprintf(outfile, "*");
        fprintf(outfile, "\n");
    }
    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j < n - i - 1; j++) fprintf(outfile, " ");
        for (int j = 0; j < 2 * i + 1; j++) fprintf(outfile, "*");
        fprintf(outfile, "\n");
    }

    fclose(outfile);
    return 0;
}
