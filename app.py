from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Successfully deployed on Heroku, but can Flutter access it?????'

if __name__ == "__main__":
	app.run()
