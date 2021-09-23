signatures = [

    # << Bad APIs >>
    {
        "name": "Format String",
        "type": "risk",
        "description": "An variable is supplied directly to the format argument of the  function, " +
                       "if the variable is user controlled a format string exploit my be possible.",
        
        "rules": [
            #printf
            "printf[ ]*\([^\,\'\"]+\);",
            "fprintf[ ]*\([^\,]+\,[^\,\'\"]+\);",
            "sprintf[ ]*\([^\,]+\,[^\,\'\"]+\);",
            "vprintf[ ]*\([^\,\'\"]+\,[^\,]+\);",
            
            "snprintf[ ]*\([^\,]+\,[^\,]+\,[^\,\'\"]+\);",
            "vsprintf[ ]*\([^\,]+\,[^\,\'\"]+\,[^\,]+\);",
            "vfprintf[ ]*\([^\,]+\,[^\,\'\"]+\,[^\,]+\);",

            "vsnprintf[ ]*\([^\,]+\,[^\,]+\,[^\,\'\"]+\,[^\,]+\);",

            # logging 
            "dprintf[ ]*\([^\,]+\,[^\,\'\"]+\);",
            "syslog[ ]*\([^\,]+\,[^\,\'\"]+\);",

            # scanf
            "scanf[ ]*\([^\,\'\"]+\);",
            "fscanf[ ]*\([^\,]+\,[^\,\'\"]+\);",
            "vscanf[ ]*\([^\,\'\"]+\,[^\,]+\);",
            "vsscanf[ ]*\([^\,]+\,[^\,\'\"]+\,[^\,]+\);",
        ]
    },

    {
        "name": "Unsafe memset Usage",
        "type": "risk",
        "description": "memset is used to populate a memory region stipulated by the programmer with a supplied value. "                        + 
                       "When the argument order is **confused** and the value to set, the second argument, is provided as the 3rd "             + 
                       "argument, and the size as the 2nd argument, the memory will not be cleared/set as expected. This typically results in"  + 
                       "leaving behind stale data that can lead to unexpected behaviour.\n\n" +
                       "Correct usage of the function to zero out a memory region is: \n\n" +
                       "`   memset(address, 0, size);`",    
        "rules": [
            "memset[ ]*\([^\,]+\,[^\,]+\,[^\,|1-9]+\);",
        ]

    },

    {
        # Currently acts as a warning of potential risk
        "name": "Potential Buffer Overflow",
        "type": "risk",
        "description": "strcpy is used to copy a non-static source string to a destination buffer. If the destination buffer has "             +    
                        "inadequate space allocated to store the incoming source string or the incoming data is improperly sanitised a "       +
                        "buffer overflow could occur leading to undefined behaviour. It is a better idea to user `strncpy` which allows for "  +
                        "the specification of a limit of bytes to read from source.",
        
        "rules": [
            "strcpy[ ]*\([^\,]+\,[^\,\'\"]+\);",
        ]
    },

    {
        "name": "Potentially Unsafe strncpy",
        "type": "risk",
        "description": "The strncpy function copies at most `size_t n` bytes from the source string to the destination buffer. If a terminating "+
                        "null byte **does not** lie within these **n bytes** the copied string will not be null terminated.\n\n If the copied "  +
                        "string is then blindly used with another function that reads/writes until a null byte the function will continue "      +
                        "reading/writing until a null byte is encountered leading to unexpected behaviour and potential security concerns.",

        "rules": [
            "strncpy[ ]*\([^\,]+\,[^\,\'\"]+\,[^\,]+\);",
        ]
    }, 
    
    {
        "name": "Potential Buffer Overflow",
        "type": "risk",
        "description": "strcat is used to copy a non-static source string to a destination buffer. If the destination buffer has "             +    
                        "inadequate space allocated to store the incoming source string or the incoming data is improperly sanitised a "       +
                        "buffer overflow could occur leading to undefined behaviour. It is a better idea to user `strncat` which allows for "  +
                        "the specification of a limit of bytes to read from source.",

        "rules": [
            "strcat[ ]*\([^\,]+\,[^\,\'\"]+\);",
        ]
    },

    {
        "name": "Potential Out of Bounds Read",
        "type": "risk",
        "description": "atoi is used to convert a potentially non-static argument to an integer which is then used directly as an array index. " +
                        "If the supplied argument is user controlled it is likely that an attacker can leverage this to cause and out of bounds "+
                        "read leading to unexpected behaviour and security concerns.",
        
        "rules": [
            "\[atoi[ ]*\([^\,\'\"]+\)\];",
        ]
    },


    {
        "name": "Buffer Overflow",
        "type": "risk",
        "description": "gets is a **deprecated** function due to its behaviour to continue reading from stdin until a newline, or EOF, is encountered. "+
                        "This behaviour can be exploited to cause a buffer overflow. Instead use `fgets` which allows for the specification of a "  +
                        "limit of bytes to read from stdin.",

        "rules": [
            "gets[ ]*\([^\,]+\);",
        ]
    },

    # TODO :: I don't think this is a good signature, it's a bit too broad
    # {
    #     "name": "Potentially Bad sizeof for Memory Allocation",
    #     "description": "sizeof is potentially called on a pointer instead of the datastructure being allocated. This means that the size of the pointer " +
    #                     "will be returned resulting in less memory being allocated/set than likely intended.",

    #     # TODO -> fix missed multiline syntax varianets
    #     "rules": [
    #         "malloc[ ]*\([ ]*sizeof[ ]*\([^\,\*]+\);",
    #         "realloc[ ]*\([^\,]+\,[ ]*sizeof[ ]*\([^\,\*]+\);",
    #     ]
    # },

    # << Warnings >> 
    {
        "name": "Meta Data Indicates Potential Risk",
        "type": "warning",
        "description": "Meta data in code such as TODOs and FIXMEs often indicate areas of a program " +
                        "that are not yet complete or are not yet safe to use. This kind of meta analysis " +
                        "has commonly been the source of vulnerability discovery. \nThese areas of the code " +
                        " should be carefully reviewed and resolved before distribution of the compiled binary.",

        # Detect until ; to get better context
        "rules": [
            "TODO[^\;]*",
            "todo[^\;]*",
            "FIXME[^\;]*",
            "fixme[^\;]*",
            "bad[^\;]*"
        ]
    }
]
