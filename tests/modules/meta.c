/*
Test detection of meta data
indicators.

________________________________
*/

#include <stdio.h>
#include <string.h>
#include <stdint.h>

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

    // fixme the buffer is to short for the
    // input
    char buf[1024];

    fgets(buf, 2024, stdin);

    // fixme this is a hack
    uint16_t port;
    scanf("%d", &port);  

    // bad should add a check to see if malloc failed
    meta_data_t *meta = (meta_data_t *) malloc(sizeof(meta_data_t));     
    
}


