import loading
l=loading.loading()

goto="Login"

while(goto!=None):
    nextgoto=None
    if goto=='Login':
        import Login
        l = login.login()
