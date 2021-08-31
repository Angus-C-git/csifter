import subprocess

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