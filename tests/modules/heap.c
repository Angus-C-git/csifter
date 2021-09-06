#include <stdlib.h>

/*
Test heap vulnerability discovery.

Attempt to detect the following heap
vulnerabilities:
_________________________________

    + Heap overflow
    + Use-after-free
    + Double free

*/

typedef struct Structure {
    int a;
    char *buf;
} structure_t;


int main(int argc, char const *argv[])
{
    /* local */
    int *a = malloc(10);     
    int *b = malloc(10);    
    int *c = malloc(10);
    structure_t *s = malloc(sizeof(structure_t));

    /* Heap overflow */
    s->a = 1;
    s->buf = malloc(10);
    s->buf = "overflowwwwwwwwwwwwwwwwwwwww";

    /* UAF */
    free(a);
    *a = 42;

    /* double free */
    free(b); 
    free(a);  


    /* SAFE USAGE */
    free(s);

    a = malloc(10);
    b = malloc(10);
    c = malloc(10);
    s = malloc(sizeof(structure_t));

    s->a = 1;
    *b = 42;
    s->buf = malloc(15);
    s->buf = "safe usage";

    return 0;
}
