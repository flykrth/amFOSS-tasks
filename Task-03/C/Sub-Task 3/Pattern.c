#include <stdio.h>

int main() {
    int n, i, j;
    printf("Enter a number: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        for (j = 0; j < n - i - 1; j++) printf(" ");
        for (j = 0; j < 2 * i + 1; j++) printf("*");
        printf("\n");
    }
    for (i = n - 2; i >= 0; i--) {
        for (j = 0; j < n - i - 1; j++) printf(" ");
        for (j = 0; j < 2 * i + 1; j++) printf("*");
        printf("\n");
    }

    return 0;
}
