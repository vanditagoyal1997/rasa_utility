
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
f1=open('data/data.txt','w')


@app.route('/_create_data')
def create_data():
	a = request.args.get('keyword', 0, type=str)
	l1=a.split(" ")
	intentstr=l1[0]
	for j in range(1,len(l1)):
		intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	for i in quest1:
		content='{\n \t'+'"text": '+'"' +i+a+'?",'+'\n \t'+'"intent":'+'"'+intentstr+'",'+'\n \t'+'"entity":[]'+'\n'+'},\n'
		print(content)
		f1.write(content)
	for i in quest2:
		content='{\n \t'+'"text": '+'"' +i+a+' is",'+'\n \t'+'"intent":'+'"'+intentstr+'",'+'\n \t'+'"entity":[]'+'\n'+'},\n'
		print(content)
		f1.write(content)
	for i in quest3:
		content='{\n \t'+'"text": '+'"' +i+a+'",'+'\n \t'+'"intent":'+'"'+intentstr+'",'+'\n \t'+'"entity":[]'+'\n'+'},\n'
		print(content)
		f1.write(content)
	f1.close()
	return jsonify(result=content)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run()