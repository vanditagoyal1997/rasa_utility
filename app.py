from flask import Flask, jsonify, render_template, request,Response
app = Flask(__name__)
f1=open('data/data.json','a')
#f2=open('domain.txt','a')
s='{\n  "rasa_nlu_data":{\n    "common_examples": [\n'
f1.write(s)
f1.close()
'''s1='intents:'
s2='\nentities:'
f2.write(s1)
f2.write(s2)
f2.close()'''
@app.route('/_create_data')
def create_data():
	#f1=open('data/data.json','a')
	a = request.args.get('keyword', 0, type=str)
	intent = request.args.get('intent',0, type=str)
	intentbool = request.args.get('intentbool',0, type=str)
	entity = request.args.get('entity', 0, type=str)
	what = request.args.get('what', 0, type=str)
	how = request.args.get('how', 0, type=str)
	when = request.args.get('when', 0, type=str)
	after = request.args.get('after', 0, type=str)
	before = request.args.get('before', 0, type=str)
	howmany = request.args.get('howmany', 0, type=str)
	whereproc = request.args.get('whereproc', 0, type=str)
	whereobj = request.args.get('whereobj', 0, type=str)
	quit = request.args.get('quit', 0, type=str)
	#print(intent)
	#print(intentbool)
	if what=='true':
		print("what")
		create_data_what(a,intent,intentbool,entity,quit)
		#resultques={'lst':l}
    
	if how=='true':
		#print("how")
		create_data_how_process(a,intent,intentbool,entity)
	if when=='true':
		create_data_when_present(a,intent,intentbool,entity)
	if after=='true':
		create_data_when_after(a,intent,intentbool,entity)
	if before=='true':
		create_data_when_before(a,intent,intentbool,entity)
	if howmany=='true':
		create_data_howmany(a,intent,intentbool,entity)
	if whereproc=='true':
		create_data_where_process(a,intent,intentbool,entity)
	if whereobj=='true':
		create_data_where_obj(a,intent,intentbool,entity)
	if quit=='true':
		close_data()
	return jsonify(result=what)

def create_data_what(a,intent,intentbool,entity,quit):
	f1=open('data/data.json','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr='what'
		for j in range(0,len(l1)):
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
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+'?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' is",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		if quit=='true':
			if i==len(quest3)-1:
				content='      {\n        '+'"text": '+'"' +str1+'",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'}\n'
			else:
				content='      {\n        '+'"text": '+'"' +str1+'",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		else:
			content='      {\n        '+'"text": '+'"' +str1+'",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	f1.close()

def create_data_how_process(a,intent,intentbool,entity):
	f1=open('data/data.json','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr='how'
		for j in range(0,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	'''f2.open('domain.txt','a+')
	tillintent=f2.readline()
	while tillintent!='intent:':
		tillintent=f2.readline()
	strintent='\n  -'+intentstr
	f2.write(strintent)
	f2.close()'''
	quest1=['how is ','tell me how is ','explain how ']
	quest2=['what is the process of ','can you tell me about the process of ', 'can you tell me something related to the process of ']
	quest3=['i want to know what is the process of ','explain what is the process of  ','i would like to know what is the process of ']
	quest4=['what happens when ','can you tell me what happens when ']
	quest5=['tell me when ','i want to know what happens when ','explain what happens when  ','i would like to know what happens when ']
	quest6=['how does ','explain how  ','i would like to know how ','tell me something related to how ','i want to know how ','tell me how ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		if i==0:
			content='      {\n        '+'"text": '+'"' +str1+' done?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		elif i==1:
			content='      {\n        '+'"text": '+'"' +str1+' done",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		elif i==2:
			content='      {\n        '+'"text": '+'"' +str1+' is done",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+'?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+'",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest4)):
		str1=quest4[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' takes place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' occurs?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	for i in range(len(quest5)):
		str1=quest5[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' takes place",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		f1.write(content)
		
		content1='      {\n        '+'"text": '+'"' +str1+' occurs",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		f1.write(content1)
		#print(content)
	for i in range(len(quest6)):
		str1=quest6[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		if quit=='true':
			if i==len(quest3)-1:
				content='      {\n        '+'"text": '+'"' +str1+'work",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'}\n'
			else:
				content='      {\n        '+'"text": '+'"' +str1+'work",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		else:
			content='      {\n        '+'"text": '+'"' +str1+'work",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	f1.close()
def create_data_when_present(a,intent,intentbool,entity):
	f1=open('data/data.json','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr='when'
		for j in range(0,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	'''f2.open('domain.txt','a+')
	tillintent=f2.readline()
	while tillintent!='intent:':
		tillintent=f2.readline()
	strintent='\n  -'+intentstr
	f2.write(strintent)
	f2.close()'''
	
	quest2=['when does ','at what point does ']
	
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' takes place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' occurs?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' take place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' occur?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	
	f1.close()
def create_data_howmany(a,intent,intentbool,entity):
	f1=open('data/data.json','a')
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
	quest1=['how many ','what is the number of ']
	quest2=['tell me how many ','i want to know how many ','i would like to know how many ','can you tell me how many ','tell me what is the number of ','i want to know what is the number of ','i would like to know what is the number of ','can you tell me what is the number of ', ]
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+'?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		if quit=='true':
			if i==len(quest2)-1:
				content='      {\n        '+'"text": '+'"' +str1+'",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'}\n'
			else:
				content='      {\n        '+'"text": '+'"' +str1+'",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		else:
			content='      {\n        '+'"text": '+'"' +str1+'",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	f1.close()
def create_data_when_after(a,intent,intentbool,entity,quit):
	f1=open('data/data.json','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr='after'
		for j in range(0,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	'''f2.open('domain.txt','a+')
	tillintent=f2.readline()
	while tillintent!='intent:':
		tillintent=f2.readline()
	strintent='\n  -'+intentstr
	f2.write(strintent)
	f2.close()'''
	quest1=['what happens after ','can you tell me what happens after ','what is the process after ','can you tell me what is the process after ']
	quest3=['i want to know what happens after ','explain what happens after  ','i would like to know what happens after ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' takes place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' occurs?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	
	for i in range(len(quest3)):
		str1=quest3[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' takes place",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		f1.write(content)
		if quit=='true':
			if i==len(quest3)-1:
				content1='      {\n        '+'"text": '+'"' +str1+' occurs",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'}\n'
			else:
				content1='      {\n        '+'"text": '+'"' +str1+' occurs",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		else:
			content1='      {\n        '+'"text": '+'"' +str1+' occurs",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	f1.close()

def create_data_when_before(a,intent,intentbool,entity,quit):
	f1=open('data/data.json','a')
	l1=a.split(" ")
	if intentbool=='true':
		intentstr=intent
	else:
		intentstr='before'
		for j in range(0,len(l1)):
			intentstr=intentstr+'_'+l1[j]
	'''f2.open('domain.txt','a+')
	tillintent=f2.readline()
	while tillintent!='intent:':
		tillintent=f2.readline()
	strintent='\n  -'+intentstr
	f2.write(strintent)
	f2.close()'''
	quest1=['what happens before ','can you tell me what happens before ','what is the process before ','can you tell me what is the process before ']
	quest3=['i want to know what happens before  ','explain what happens before  ','i would like to know what happens before ','i want to know what is the process before  ','explain what is the process before  ','i would like to know what is the process before ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' takes place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' occurs?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	
	for i in range(len(quest3)):
		str1=quest3[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' takes place",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		f1.write(content)
		if quit=='true':
			if i==len(quest3)-1:
				content1='      {\n        '+'"text": '+'"' +str1+' occurs",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'}\n'
			else:
				content1='      {\n        '+'"text": '+'"' +str1+' occurs",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		else:
			content1='      {\n        '+'"text": '+'"' +str1+' occurs",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	f1.close()

def create_data_where_process(a,intent,intentbool,entity):
	f1=open('data/data.json','a')
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
	quest1=['where does ']
	quest2=['tell me where does ','i want to know where does ','explain where does ','i would like to know where does ',]
	quest3=['can you tell me where ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' take place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' occur?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' take place",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' occur",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' occurs?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		if quit=='true':
			if i==len(quest3)-1:
				content1='      {\n        '+'"text": '+'"' +str1+' takes place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'}\n'
			else:
				content='      {\n        '+'"text": '+'"' +str1+' takes place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		else:
			content='      {\n        '+'"text": '+'"' +str1+' takes place?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	f1.close()
def create_data_where_obj(a,intent,intentbool,entity):
	f1=open('data/data.json','a')
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
	quest1=['where is ' ]
	quest2=['tell me where  ','i want to know where ','explain where ','i would like to know where ','tell me about the place where ','i want to know the place where ',]
	quest3=['can you tell me where ']
	notentity=['in','at','for','on','about','with','from','into','during','until','against','among','throughout','despite','towards','upon','of','to','by','like','over','before','between','after','since','without','under','within','along','following','across','behind','beyond','plus','except','but','up','out','around','down','off','above','near','a','the','an']
	lquest=[]
	for i in range(len(quest1)):
		str1=quest1[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+'?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' located?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	for i in range(len(quest2)):
		str1=quest2[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' is",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		content1='      {\n        '+'"text": '+'"' +str1+' is located",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content1)
	for i in range(len(quest3)):
		str1=quest3[i]+a
		lquest.append(str1)
		str2=''
		if entity=='true':
			for j in range(len(l1)):
				if l1[j] not in notentity:
					start=str1.find(l1[j])
					end=start+len(l1[j])
					if j==len(l1)-1:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          }\n        '
					else:
						str2+='\n          {\n            '+'"start":'+str(start)+',\n            '+'"end":'+str(end)+',\n            '+'"value":'+'"'+l1[j]+'",\n            '+'"entity":'+'"'+l1[j]+'"\n          },\n        '
		else:
			str2=''
		content='      {\n        '+'"text": '+'"' +str1+' is located?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
		if quit=='true':
			if i==len(quest3)-1:
				content1='      {\n        '+'"text": '+'"' +str1+' is?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'}\n'
			else:
				content='      {\n        '+'"text": '+'"' +str1+' is?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		else:
			content='      {\n        '+'"text": '+'"' +str1+' is?",'+'\n        '+'"intent":'+'"'+intentstr+'",'+'\n        '+'"entity":['+str2+']'+'\n      '+'},\n'
		#print(content)
		f1.write(content)
	f1.close()
def close_data():
	f1=open('data/data.json','a')
	s='\n    ]\n  }\n}'
	f1.write(s)
	f1.close()
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run()
