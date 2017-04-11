from flask import flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def main():
	return "Alllrigghtty then"

if __name__=='__main__':
	app.run(debug=true)