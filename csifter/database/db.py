signatures = [

    {
        "name": "Format String Vulnerability",
        "description": "An variable is supplied directly to the format argument of the  function, if the variable is user controlled a format string exploit my be possible.",
        
        "rules": [
            #printf
            "printf[ ]*\([^\,\'\"]+\)\;",
            "fprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "sprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "vprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "vprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",

            # TODO :: 3 argument printf family

            # logging 
            "dprintf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "syslog[ ]*\([^\,]+\,[^\,\'\"]*\);",

            # scanf
            "scanf[ ]*\([^\,\'\"]+\);",
            "fscanf[ ]*\([^\,]+\,[^\,\'\"]*\);",
            "vscanf[ ]*\([^\,]+\,[^\,\'\"]*\);",

            # TODO :: vsscanf
        ]
    }

]   
