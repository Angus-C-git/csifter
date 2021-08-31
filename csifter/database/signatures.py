signatures = [

    {
        "name": "Format String Vulnerability",
        "description": "An variable is supplied directly to the format function, if the variable is user controlled a format string exploit my be possible",
        
        "rules": [
            "^\s*printf\([^'\"].*\);$"
        ]
    }

]   
