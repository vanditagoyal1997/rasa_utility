
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
f1=open('data/data.txt','a')
s='{\n\t "rasa_nlu_data":{\n\t "common_examples": [\n'
f1.write(s)
f1.close()
@app.route('/_create_data')
def create_data():
	a = request.args.get('keyword', 0, type=str)
	what = request.args.get('what', 0, type=str)
	how = request.args.get('how', 0, type=str)
	when = request.args.get('when', 0, type=str)
	howmany = request.args.get('howmany', 0, type=str)
	#print(what)
	#print(how)
	if what=='true':
		create_data_what(a)
	elif how=='true':
		create_data_how(a)
	elif when=='true':
		create_data_when(a)
	elif howmany=='true':
		create_data_howmany(a)
	return jsonify(result=what)

def create_data_what(a):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	intentstr=l1[0]
	for j in range(1,len(l1)):
		intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+'?",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+' is",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		if i==len(quest3)-1:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'}\n'
		else:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

def create_data_how(a):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	intentstr=l1[0]
	for j in range(1,len(l1)):
		intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+'?",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+' is",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		if i==len(quest3)-1:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'}\n'
		else:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

def create_data_when(a):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	intentstr=l1[0]
	for j in range(1,len(l1)):
		intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+'?",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+' is",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		if i==len(quest3)-1:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'}\n'
		else:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

def create_data_howmany(a):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	intentstr=l1[0]
	for j in range(1,len(l1)):
		intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+'?",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		content='{\n\t'+'"text": '+'"' +str1+' is",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		for j in range(len(l1)):
			start=str1.find(l1[j])
			end=start+len(l1[j])
			if j==len(l1)-1:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t}\n\t'
			else:
				str2+='\n\t\t{\n\t\t\t'+'"start":'+str(start)+',\n\t\t\t'+'"end":'+str(end)+',\n\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t},\n\t'
		if i==len(quest3)-1:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'}\n'
		else:
			content='{\n\t'+'"text": '+'"' +str1+'",'+'\n\t'+'"intent":'+'"'+intentstr+'",'+'\n\t'+'"entity":['+str2+']'+'\n'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run()
