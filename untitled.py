from flask import Flask, render_template, request, url_for, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
	result = request.form
	d = datetime.datetime.now()
	k = str(d.year)+str(d.day)+str(d.hour)+str(d.minute)+str(d.second)
	f = open(k+'.html', 'w')
	f.write(render_template("result.html", result = result).encode('utf-8'))
	return render_template("result.html", result = result)


if __name__ == '__main__':
  app.run(debug=True)
