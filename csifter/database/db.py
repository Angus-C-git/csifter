signatures = [

    {
        "name": "Format String",
        "description": "An variable is supplied directly to the format argument of the  function, if the variable is user controlled a format string exploit my be possible.",
        
        "rules": [
            #printf
            "printf[ ]*\([^\,\'\"]+\)\;",
            "fprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "sprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "vprintf[ ]*\([^\,\'\"]+\,[^\,]+\);",
            
            "snprintf[ ]*\([^\,]+\,[^\,]+\,[^\,\'\"]*\);",
            "vsprintf[ ]*\([^\,]+\,[^\,\'\"]+\,[^\,]+\);",
            "vfprintf[ ]*\([^\,]+\,[^\,\'\"]+\,[^\,]+\);",

            "vsnprintf[ ]*\([^\,]+\,[^\,]+\,[^\,\'\"]+\,[^\,]+\);",

            # logging 
            "dprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "syslog[ ]*\([^\,]+\,[^\,\'\"]*\);",

            # scanf
            "scanf[ ]*\([^\,\'\"]+\);",
            "fscanf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "vscanf[ ]*\([^\,\'\"]+\,[^\,]+\);",
            "vsscanf[ ]*\([^\,]+\,[^\,\'\"]+\,[^\,]+\);",
        ]
    },

    {
        "name": "Unsafe memset Usage",
        "description": "The memset is used to populate a memory region stipulated by the programmer with a supplied value. " + 
                       "When the argument order is **confused** and the value to set, the second argument, is provided as the 3rd " + 
                       "argument, and the size as the 2nd argument, the memory will not be cleared/set as expected. This typically results in" + 
                       "leaving behind stale data that can lead to unexpected behaviour.\n\n" +
                       "Correct usage of the function to zero out a memory region is: \n\n" +
                       "`memset(address, 0, size);`",
    
        "rules": [
            "memset[ ]*\([^\,]+\,[^\,]+\,[^\,|1-9]+\);",
        ]
    }

]   
