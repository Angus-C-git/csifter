#include <stdio.h>


/**
Test basic vulnerability discovery
in a 'real' program.
    
    bof: gets()
    fmtstr: printf()

*/


int 
main(int argc, char const *argv[])
{
    /* code >> barely*/
    char spook[10];

    gets(spook);

    printf("Maybe this will spook ya: ");
    printf(spook);
    printf("\n");

    return 0;
}
