#include <stdlib.h>

int main(int argc, char const *argv[])
{
    /* code */
    int *a = malloc(10);     
    int *b = malloc(10);    
    int *c = malloc(10);

    free(&a);
    free(&b); 
    free(&a);  

    return 0;
}
