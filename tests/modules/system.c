/*
Test detection of usage
of system like functions
called with non constant 
arguments or calls with
shell arguments.

+ /bin/sh
+ /bin/bash
+ /bin/fish
+ /bin/ksh
+ /bin/tcsh
+ /bin/zsh


Should detect the following
calls:
_____________________________

    + execv
    + execve
    + system
    + execvp
    + execl
    + execlp
    + execle
    + execvpe

*/

void
test_system_calls()
{
    
}