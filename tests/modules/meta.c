/*
Test detection of meta data
indicators.

________________________________
*/

#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>


/*
    Date: 2013-07-31
    Name: Michael Gogins
    

    This file is part of Metagen, a generator of metatiles for pixel-art games.
    I have no idea what I'm saying github copilot is just going nuts. This file
    tests detection of meta comments like:

    TODO (1) fix all the bugs
*/


typedef struct meta_data {
    char *name;
} meta_data_t; 


void
test_meta_c()
{

    // fixme the buffer is to short for the input
    char buf[1024];
    char secondary_input[1024];
    int c;

    fgets(buf, 2024, stdin);

    // FIXME this is a hack
    uint16_t port;
    scanf("%d", &port);  

    // bad should add a check to see if malloc failed
    meta_data_t *meta = (meta_data_t *) malloc(sizeof(meta_data_t));     
    
    int buffer_count;
    // patch this logic to be safer
    while (c = fgetc(stdin) != '\n') {
        secondary_input[buffer_count] = c;
    }
}


void
main()
{
    test_meta_c();
}