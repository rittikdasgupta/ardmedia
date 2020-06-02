from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("main/index.html")
@app.route("/wd")
def wdesign():
    return render_template("main/wb.html")

if __name__=="__main__":
    app.run()