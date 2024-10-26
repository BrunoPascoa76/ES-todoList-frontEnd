import sys
from flask import Flask, make_response, redirect, render_template, request, url_for
from secret import API_URL, AWS_COGNITO_HOSTED_URL, PORT
import requests as http

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

@app.route("/")
def home_page():
    if "access_token" in request.cookies:
        return render_template("homePage.html")
    else:
        return redirect(AWS_COGNITO_HOSTED_URL)

@app.route("/redirect")
def callback():
    if "code" in request.args:
        resp=redirect("/")
        resp.set_cookie("access_token",request.args.get("code"),httponly=True,secure=True)
        return resp
    else:
        return "code not returned",400

@app.route("/logout")
def logout():
    #http.get(f"{API_URL}/sign_out")
    resp=redirect("/")
    resp.delete_cookie("access_token")
    return resp


if __name__ == '__main__':
    app.run(debug=True, port=PORT)

