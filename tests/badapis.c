#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Test detection of general bad
API usage.

Format function usage dealt 
with separately see 
./fmtstrings.c

Should flag vulnerabilities 
caused by bad usage for
the following functions:
_____________________________

    + strcpy
    + strncpy
    + strcat
    + ?memcpy?
    + memset
    + atoi

*/


typedef struct testcase {
    char *str;
} testcase_t;


void
bad_api_usage(void)
{
    char *str = "Hello";
    char *str2 = "World";

    char buf[10];
    char *dummy_usr_input = "overflowwwwwwwwwwwwwwwwwwwwww";

    testcase_t *testcase = 0;

    /* UNSAFE */

    memset(str, 0x100, 0);
    strcpy(buf, dummy_usr_input);
    strncpy(buf, dummy_usr_input, 42);
    strcat(str, str2);
    // memcpy(buf, dummy_usr_input, 42);
    char character = str[atoi(dummy_usr_input)];
    gets(buf);

    testcase = (testcase_t *) malloc(sizeof(testcase));
    testcase = (testcase_t *) realloc(testcase, sizeof(testcase));


    /* ALT SYNTAX */
    
    memset(
            str, 
            0x100, 
            0
        );

    strcpy(
            buf,
            dummy_usr_input
        );

    strncpy(
            buf,
            dummy_usr_input,
            42
        );
    
    strcat(
            str,
            str2
        );

    gets(
            buf 
        );

    testcase = (testcase_t *) malloc(  
                                        sizeof(testcase));
    
    testcase = (testcase_t *) realloc(
                                        testcase, 
                                        sizeof(testcase)
                                    );
    /* SAFE */
    
    memset(str, 0, 1000);
    // safer
    strcpy(buf, "staticarg");
    strncpy(buf, "staticarg", 10);
    strcat(str, "staticarg");
    testcase = (testcase_t *) malloc(sizeof(*testcase));
    testcase = (testcase_t *) realloc(testcase, sizeof(*testcase));
}


int main(){return 0;}