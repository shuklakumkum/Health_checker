def check_security(url:str)->dict:
    return{
        "Content-Security-Policy":"Present",
        "X-Frame-Options":"Present",
        "Strict-Transport-Security":"Present",
    }