from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
f1=open('data/data.txt','a')
f2=open('domain.txt','a')
s='{\n\t "rasa_nlu_data":{\n\t\t "common_examples": [\n'
f1.write(s)
f1.close()
s1='intents:'
s2='\nentities:'
f2.write(s1)
f2.write(s2)
f2.close()
@app.route('/_create_data')
def create_data():
	a = request.args.get('keyword', 0, type=str)
	intent = request.args.get('intent',0, type=str)
	intentbool = request.args.get('intentbool',0, type=str)
	entity = request.args.get('entity', 0, type=str)
	what = request.args.get('what', 0, type=str)
	how = request.args.get('how', 0, type=str)
	when = request.args.get('when', 0, type=str)
	howmany = request.args.get('howmany', 0, type=str)
	where = request.args.get('where', 0, type=str)
	#print(intent)
	#print(intentbool)
	if what=='true':
		create_data_what(a,intent,intentbool,entity)
	if how=='true':
		create_data_how(a,intent,intentbool,entity)
	if when=='true':
		create_data_when(a,intent,intentbool,entity)
	if howmany=='true':
		create_data_howmany(a,intent,intentbool,entity)
	if where=='true':
		create_data_where(a,intent,intentbool,entity)
	return jsonify(result=what)

def create_data_what(a,intent,intentbool,entity):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr=l1[0]
		for j in range(1,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	'''f2.open('domain.txt','a+')
	tillintent=f2.readline()
	while tillintent!='intent:':
		tillintent=f2.readline()
	strintent='\n  -'+intentstr
	f2.write(strintent)
	f2.close()'''
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+'?",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+' is",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		if i==len(quest3)-1:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'}\n'
		else:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

def create_data_how(a,intent,intentbool,entity):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr=l1[0]
		for j in range(1,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+'?",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+' is",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		if i==len(quest3)-1:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'}\n'
		else:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

def create_data_when(a,intent,intentbool,entity):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr=l1[0]
		for j in range(1,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+'?",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+' is",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		if i==len(quest3)-1:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'}\n'
		else:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

def create_data_howmany(a,intent,intentbool,entity):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr=l1[0]
		for j in range(1,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+'?",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+' is",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		if i==len(quest3)-1:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'}\n'
		else:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()
def create_data_where(a,intent,intentbool,entity):
	f1=open('data/data.txt','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr=l1[0]
		for j in range(1,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	quest1=['what is ','what do you mean by ','what is meant by ']
	quest2=['tell me what ','i want to know what ','explain what ','i would like to know what ','can you tell me about ', 'can you tell me something related to ']
	quest3=['tell me about','i want to know about ','i would like to know about ','tell me something related to ','give me something related to ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near']
	for i in range(len(quest1)):
		str1=quest1[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+'?",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		content='\t{\n\t\t'+'"text": '+'"' +str1+' is",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t}\n\t\t'
					else:
						str2+='\n\t\t\t{\n\t\t\t\t'+'"start":'+str(start)+',\n\t\t\t\t'+'"end":'+str(end)+',\n\t\t\t\t'+'"value":'+'"'+l1[j]+'",\n\t\t\t\t'+'"entity":'+'"'+l1[j]+'"\n\t\t\t},\n\t\t'
		else:
			str2=''
		if i==len(quest3)-1:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'}\n'
		else:
			content='\t{\n\t\t'+'"text": '+'"' +str1+'",'+'\n\t\t'+'"intent":'+'"'+intentstr+'",'+'\n\t\t'+'"entity":['+str2+']'+'\n\t'+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run()
