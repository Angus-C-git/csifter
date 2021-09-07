/*
    Test all detection features of
    csifter in a 'real' C source file.
*/






#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>


/*
 ____    _   _   _  ____ _____         
/ ___|  / \ | | | |/ ___| ____|               
\___ \ / _ \| | | | |   |  _|            
 ___) / ___ \ |_| | |___| |___             
|____/_/   \_\___/ \____|_____|             

_______________________________________

Changelog:

    + 07-09-2016
        - Added banner
        - Started port binding logic

*/

void
print_banner(void)
{
    printf("\n");
    printf(" ____    _   _   _  ____ _____      \n");
    printf("/ ___|  / \\ | | | |/ ___| ____|    \n");               
    printf("\\___ \\ / _ \\| | | | |   |  _|    \n");           
    printf(" ___) / ___ \\ |_| | |___| |___   \n");
    printf("|____/_/   \\_\\___/ \\____|_____|  \n");           
    printf("\n");
}



uint16_t
get_port()
{
    uint16_t port;

    printf("Enter desired port\n");   
    // FIXME - whats the right format specifier
    //         for a uint16_t
    scanf("%d", &port);
}



/* Entrypoint */
int 
main(int argc, char const *argv[])
{
    
    // start main logic
    print_banner();
    return 0;
}

