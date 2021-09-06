#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <syslog.h>


/*
Test detection of vulnerable usage 
of format functions.

Should detect format string 
vulnerabilities for:
_____________________________

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
    fprintf(stdout, argv[1]);
    sprintf(tmp, argv[1]);
    vprintf(argv[1], NULL);
    snprintf(tmp, 0x100, argv[1]);
    vsprintf(tmp, argv[1], NULL);
    vfprintf(stdout, argv[1], NULL);
    vsnprintf(tmp, 0x100, argv[1], NULL);
    
    
    /* logging */
    dprintf(LOG_ERR, argv[1]);
    syslog(LOG_INFO, argv[1]);
    
    /* scan */
    scanf(argv[1]);
    fscanf(stdin, argv[1]);
    vscanf(argv[1], NULL);
    vsscanf(tmp, argv[1], NULL);
    
    //////////////////////////////////////

    /* ALTERED FORMATTING */
    printf(
            argv[1]
        );
    fprintf(
            stdout, 
            argv[1]
        );
    sprintf(
            tmp, 
            argv[1]
        );
    vprintf(
            argv[1], 
            NULL
        );
    snprintf(
            tmp, 
            0x100, 
            argv[1]
        );
    vsprintf(
            tmp, 
            argv[1], 
            NULL
        );
    vfprintf(
            stdout, 
            argv[1], 
            NULL
        );
    vsnprintf(
            tmp, 
            0x100, 
            argv[1], 
            NULL
        );
    
    
    /* logging */
    dprintf(
            LOG_ERR, 
            argv[1]
        );
    syslog(
            LOG_INFO, 
            argv[1]
        );
    
    /* scan */
    scanf(
            argv[1]
        );
    fscanf(
            stdin, 
            argv[1]
        );
    vscanf(
            argv[1], 
            NULL
        );
    vsscanf(
            tmp, 
            argv[1], 
            NULL
        );


    /* SAFE USAGE */
    printf("%s", argv[1]);
    fprintf(stdout, "%s", argv[1]);
    sprintf(tmp, "%s", argv[1]);
    vprintf("%s", NULL);
    snprintf(tmp, 0x100, "%s");
    vsprintf(tmp, "%s", NULL);
    vfprintf(stdout, "%s", NULL);
    vsnprintf(tmp, 0x100, "%s", NULL);
    
    dprintf(LOG_ERR, "%s", argv[1]);
    syslog(LOG_INFO, "%s", argv[1]);

    scanf("%s", tmp);
    fscanf(stdin, "%s", tmp);
    vscanf("%s", NULL);
    vsscanf(tmp, "%s", NULL);

    return 0;
}
