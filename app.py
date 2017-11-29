from flask import Flask

app=Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
@app.route('/hello')
def hello():
	return "<h1>Hello world!</h1>"


@app.route('/test/<query>')
def search(query):
	return query


@app.route('/name/<name>')
def index(name):
	if name.lower() == "dhanu":
		return "<h1>hello, {}</h1>".format(name), 200
	else:
		return "Not found", 404

if __name__ == "__main__":
	app.run()