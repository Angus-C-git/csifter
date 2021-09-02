#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <syslog.h>


/*
Database of vulnerable usage of 
format functions

GCC detection:

    + printf        [X]
    + fprintf       [X]
    + sprintf       [X]
    + snprintf      [X]
    + vsnprintf     [X]
    + vsprintf      [X]
    + vfprintf      [X]
    + vprintf       [X]

    + dprintf       [X]
    + syslog        [X]

    + vscanf        [X]
    + vsscanf       [X]
    + fscanf        [X]
    + scanf         [X]
*/


/* take in argv[1] directly */
int 
main(int argc, char const *argv[])
{   
    // suppress compiler warning
    char *tmp = "empty";
    
    /* printf family */
    printf(argv[1]);
    fprintf(stdout, 
            argv[1]
        );
    sprintf(tmp, argv[1]);
    snprintf(tmp, 0x100, argv[1]);
    vsnprintf(tmp, 0x100, argv[1], NULL);
    vsprintf(tmp, argv[1], NULL);
    vfprintf(stdout, argv[1], NULL);
    vprintf(argv[1], NULL);
    
    /* logging */
    dprintf(LOG_ERR, argv[1]);
    syslog(LOG_INFO, argv[1]);
    
    /* scan */
    scanf(argv[1]);
    fscanf(stdin, argv[1]);
    vscanf(argv[1], NULL);
    vsscanf(tmp, argv[1], NULL);
    

    return 0;
}
