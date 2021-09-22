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



typedef struct HOST {
    char *hostname;
    char *ip;
} host_t;



uint16_t
get_port()
{
    uint16_t port;

    printf("Enter desired port\n");   
    // FIXME - whats the right format specifier
    //         for a uint16_t leaving as int for
    //         now
    scanf("%d", &port);

    return port;
}


char *
get_host_address()
{
    char *host_ip_address;

    printf("Enter host IP address\n");
    fgets(host_ip_address, sizeof(host_ip_address), stdin);

    printf("Received remote IP => ");
    printf(host_ip_address);
    printf("\n");    
}


void
configure_host() {
    char *host_ip_address;
    uint16_t port;

    host_ip_address = get_host_address();
    port = get_port();

    // remove stale entries
    host_t *host = malloc(sizeof(host_t));
    memset(host->hostname, sizeof(host->hostname), 0);
}


/* Entrypoint */
int 
main(int argc, char const *argv[])
{
    
    // start main logic
    
    return 0;
}

/*
    - DEV NOTES -

    + 07-09-2016 - check if file can
                    read outside the parent
                    directory
*/