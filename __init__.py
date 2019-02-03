from flask import Flask, redirect, url_for, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():

	search = request.form['search']

	if search == "":
		return render_template('index.html')
	else:
		r = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&search='+search+'')
		json_object = r.json()
		title = []
		desc = []
		url_links = []
		if(json_object[1]):
			for i in range(len(json_object[1])):
				title.append(json_object[1][i])
				desc.append(json_object[2][i])
				url_links.append(json_object[3][i])


		return render_template('search.html',search=json_object[0],title=title,desc=desc,url_links = url_links, length=len(json_object[1]))




if __name__ == '__main__':
   app.run(debug = True)
