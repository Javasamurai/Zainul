from flask import Flask,render_template,request,redirect
import time
app=Flask(__name__)

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/ramadan_timer')
def timer():
	return render_template("ramadan_timer.html")

if __name__=='__main__':
	app.run(debug=True)