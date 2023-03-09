from django.shortcuts import render
import os
from django.http import HttpResponse
from twilio.rest import Client

def index(request):
	return render(request,'index.html')


def test(request):
	
	val1 = int(request.POST["NUMBER_FIELD"])
	print(val1)
	return render(request,"index.html")


def message():
	global message
	#link = "https://scmylsc.github.io/scmylsc"
	link = "https://rzp.io/l/mAsJjQ2ST"
	amount_id = "5000"
	order_id = "4000"
	message = "WELCOME TO SWEETCHOICE YOUR ORDER ID  : "+order_id+", AND YOUR AMOUNT : "+amount_id+", WANT TO MAKE PAYMENT IN ONLINE : "+ link

def twilio(request):
	main_number = int(request.POST["NUMBER_FIELD"])

	main_message = message
	account_sid = a
	auth_token = b
	client = Client(auth_token,account_sid)
	client.message.create(to = main_number,
		       from_ = "",
			   body = main_message)
	return render(request,"index.html")


class create_account:
	def __init__(user_name,pass_word):
		global username
		global password
		username = user_name
		password = pass_word
	def create_file():
		fi = open("username.txt",'w')
		fi.write(username)
		fi.close()
	def create_file2():
		fi = open("password.txt",'w')
		fi.write(password)
		fi.close()
	def read_data():
		global main_user
		global main_pass
		fi = open("username.txt",'r')
		main_user = fi.read()
		fi = open("password.txt",'r')
		main_pass = fi.read()
	def validate():
		a = "WRONG USERNAME"
		b = "WRONG PASSWORD"

		if(username == main_user):
			if( password == main_pass):
				return render(request,"user_panel.html")
			else:
				print(b)
		else:
			print(a)

		


if __name__ == "__main__":
	username = request.POST("username")
	password = request.POST("password")
	write_username.validate(username,password)
