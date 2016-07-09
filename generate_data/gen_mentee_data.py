import sys,csv,json,string,random
from numpy.random import choice as nmchoice
def name_generator(langs=False,size=10, chars=string.ascii_lowercase):
	first = ''.join(random.choice(chars) for _ in range(size))
	last = ''.join(random.choice(chars) for _ in range(size))
	name = (first + " " + last).title()
	if langs:
		return first
	return name
def email_generator(size=7, chars=string.ascii_lowercase):
	username = ''.join(random.choice(chars) for _ in range(size))
	domain = ''.join(random.choice(chars) for _ in range(size))
	return username + '@' + domain + '.com'
def mobile_generator(size=10, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
def gender_generator(prob):
	return nmchoice(["Male","Female"],1,p=[prob,(1-prob)])[0]
def department_generator():
	departments_list=[
		"Architecture",
		"Chemical",
		"CSE",
		"ECE",
		"ICE",
		"EEE",
		"Production",
		"Metallurgy",
		"Mechanical",
		"Civil"
	]
	probability_dist=[.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]
	return nmchoice(departments_list,1,p=probability_dist)[0]
def state_generator(size=10, chars=string.ascii_lowercase):
	states_list=[
		"AP/Telangana",
		"Tamil Nadu",
		"Kerala",
		"Bihar",
		"Maharashtra",
		"Arunachal Pradesh",
		"Assam",
		"Chhattisgarh",
		"Delhi",
		"Goa",
		"Gujarat",
		"Haryana",
		"Himachal Pradesh",
		"Jammu & Kashmir",
		"Jharkhand",
		"Karnataka",
		"Madhya Pradesh",
		"Manipur",
		"Meghalaya",
		"Mizoram",
		"Nagaland",
		"Odisha",
		"Punjab",
		"Rajasthan",
		"Sikkim",
		"Tripura",
		"Uttar Pradesh",
		"Uttarakhand",
		"West Bengal"]
	probability_dist=[
		.25,
		.35,
		.06,
		.05,
		.05,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01,
		.01]
	state = nmchoice(states_list,1,p=probability_dist)
	language = ""
	if state == "Tamil Nadu":
		language = nmchoice(["Tamil",""],1,p=[0.90,0.10])
	elif state == "AP/Telangana":
		language = nmchoice(["Telugu",""],1,p=[0.95,0.05])
	elif state == "Kerala":
		language = nmchoice(["Malayalam",""],1,p=[0.95,0.05])
	else:
		language = nmchoice(["Hindi",""],1,p=[0.90,0.10])
	if language == "":
		language = nmchoice(["Marathi","Bengali","Odiya"],1,p=[0.40,0.30,0.30])
	return (state[0],language[0])
def dasa_generator():
	return nmchoice(["yes","no"],1,p=[0.10,0.90])[0]
dataset=[]
for _ in range(850):
	name = name_generator()
	department = department_generator()
	roll_number = mobile_generator(9)
	email = email_generator()
	mobile = mobile_generator(10)
	state,language = state_generator()
	dasa = dasa_generator()
	other_langs = name_generator(True)
	probs=0.70
	if department=="Mechanical":
		probs=0.95
	gender = gender_generator(probs)
	row=[name,roll_number,gender,email,department,dasa,language,state,other_langs,mobile]
	dataset.append(row)
with open("sample_mentee_data.csv","wb") as f:
	writer = csv.writer(f)
	writer.writerows(dataset)