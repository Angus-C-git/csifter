import subprocess


def run_compiler_checks(file):
    """
    ‣ Run GCC to trigger its 
      source checks
    ‣ GCC will chuck an error if it
      picks up very trivial vulnerabilities 
    ‣ GCC has a surprisingly large amount of 
      source checks built into it
    """

    print(f'[>->] Running GCC compiler checks against {file}')
    try:
        gcc_res = subprocess.run([
            'gcc',
             # '-Wall',                       # drop wall to avoid unused variable warnings
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
        {Fore.LIGHTRED_EX} Check GCC installed, or perhaps the file
            cannot be compiled by GCC and all is well
        ''')
