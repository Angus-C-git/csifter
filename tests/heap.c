#include <stdlib.h>

int main(int argc, char const *argv[])
{
    /* code */
    int *a = malloc(10);     // 0xa04010
    int *b = malloc(10);     // 0xa04030
    int *c = malloc(10);     // 0xa04050

    free(&a);
    free(&b); 
    free(&a);  

    return 0;
}
