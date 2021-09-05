#include <stdio.h>
#include <stdlib.h>

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
    + strncat
    + memcpy
    + memset

*/

void
bad_api_usage(void)
{
    char *str = "Hello";
    char *str2 = "World";
    char *str3 = "!";

    memset(str, 5, 0);
}