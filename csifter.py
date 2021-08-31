#!/usr/bin/python3

"""

  ____ ____ ___ _____ _____ _____ ____  
 / ___/ ___|_ _|  ___|_   _| ____|  _ \ 
| |   \___ \| || |_    | | |  _| | |_) |
| |___ ___) | ||  _|   | | | |___|  _ < 
 \____|____/___|_|     |_| |_____|_| \_\

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

 ‣ A poormans static analyser for C source
   audits
 ‣ Written badly in python  
 ‣ Do not trust this tool beyond identifying
   the most basic of potential vulnerabilities
"""

import sys
import argparse
import subprocess
from colorama import Fore, Style


'''
‣ Run GCC to trigger its 
  source checks
‣ GCC will chuck a spaz if it
  picks up very trivial vulns 
‣ GCC has a surprisingly large amount of 
  source checks built into it
'''
def run_compiler_checks(file):
    print(f'[>->] Running GCC against {file}')
    try:
        gcc_res = subprocess.run([
            'gcc',
            '-Wall', 
            '-Wformat-security',              # Format strings 
            '-Wduplicated-cond',              # Logic bugs
            '-Wfloat-equal',                  # Comparison bugs (floats)
            '-Wshadow',                       # Shadowed variables
            '-Wconversion',                   # Type conversion mistakes (integer overflow)
            '-Wjump-misses-init',             # Skip variable initialization
            '-Wlogical-not-parentheses',      # Potential bugs cause by imbalanced parentheses
            '-Wnull-dereference',             # Potential bugs cause by null pointer dereferencing       
            '-Wstringop-overflow',            # String operations overflow  
            file, 
            '-o',
            '/tmp/sifter'
        ])
    except Exception as e:
        print(f'''
        {Fore.LIGHTRED_EX} Is GCC installed, or perhaps the file
            cannot be compiled by GCC and all is well
        ''')

   

def main(args):
    print(f'[>->] Sifting sauce for {Fore.LIGHTGREEN_EX} {args.files[0]} {Style.RESET_ALL}')
    for file in args.files:
        run_compiler_checks(file)

    print(f'[>->] Hunting for hanging format functions')


def print_banner():
    print(Fore.LIGHTRED_EX + '''
  ____ ____ ___ _____ _____ _____ ____      
 / ___/ ___|_ _|  ___|_   _| ____|  _ \     
| |   \___ \| || |_    | | |  _| | |_) |    
| |___ ___) | ||  _|   | | | |___|  _ <     
 \____|____/___|_|     |_| |_____|_| \_\    

 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                          
                              
    ''')
    print(Style.RESET_ALL)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=print_banner(), 
        epilog=">> Should Have gone to stacksavers ?"
    )

    parser.add_argument('-files',
                        nargs='+',
                        dest='files',
                        help = 'file(s) to sift',
                        )
 

    args = parser.parse_args()

    if (len(sys.argv) == 1): parser.print_help()
    else: main(args)

