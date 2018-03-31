#import

from flask import Flask, url_for,Response,request,json

# ////////////////////////////////////////////////////////
# load config


# ///////////////////////////////////////////////////////
# log


# ///////////////////////////////////////////////////////
# database


# ///////////////////////////////////////////////////////
# book


# ///////////////////////////////////////////////////////
# login


# ///////////////////////////////////////////////////////
# cancel


# ///////////////////////////////////////////////////////
# register


# ///////////////////////////////////////////////////////
# get room


# ///////////////////////////////////////////////////////
# Route

app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def api_login():
    
    if request.method =='POST':
       
            if request.headers['Content-Type'] == 'application/json':
                return "JSON Message: " + json.dumps(request.json)
            else:
                return "415 Unsupported Media Type ;)"
    else: return "fail_POST_LOGIN"

@app.route('/regis', methods = ['POST'])
def api_regis():
    
    if request.method =='POST':
       
            if request.headers['Content-Type'] == 'application/json':
                return "JSON Message: " + json.dumps(request.json)
            else:
                return "415 Unsupported Media Type ;)"
    else: return "fail_POST_REGIS"

@app.route('/book', methods = ['POST'])
def api_book():
    
    if request.method =='POST':
       
            if request.headers['Content-Type'] == 'application/json':
                return "JSON Message: " + json.dumps(request.json)
            else:
                return "415 Unsupported Media Type ;)"
    else: return "fail_POST_BOOK"

@app.route('/cancel', methods = ['POST'])
def api_cancel():
    
    if request.method =='POST':
       
            if request.headers['Content-Type'] == 'application/json':
                return "JSON Message: " + json.dumps(request.json)
            else:
                return "415 Unsupported Media Type ;)"
    else: return "fail_POST_CANCEL"
@app.route('/list', methods = ['GET'])
def api_list():
    
    if request.method =='GET': return "list of Room"      
    else: return "fail_POST_CANCEL"

       
if __name__ == '__main__':
    app.run()



# ///////////////////////////////////////////////////////
