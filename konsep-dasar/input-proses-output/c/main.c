#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;

    printf("Nilai A: ");
    scanf("%d", &a);

    printf("Nilai B: ");
    scanf("%d", &b);

    int c = a + b;

    printf("Nilai A + B = %d\n", c);

    return 0;
}