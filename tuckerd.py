#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = raw_input("IP for Malcolm to listen on: ")
PORT = 23

s.bind((HOST, PORT))

print 'Malcolm awaits his prey'
s.listen(1)


while 1:
	conn, addr = s.accept()
	print 'Prey at: ', addr

	#the welcome
	conn.send("Come the fuck in, or fuck the fuck off.\n")
	conn.send("fucking username: ")
	preyuname = conn.recv(20)
	print "victim supplied: ", preyuname, " as username."
	conn.send("\nfucking password: ")
	preypasw = conn.recv(20)
	print "victim supplied: ", preypasw, " as password."
	
	conn.send("\nfucking wrong shitehead, try again.")
	conn.send("\nfucking password: ")
	preypasw1 = conn.recv(20)
	print "victim supplied: ", preypasw1, " as password."
	
	conn.send("\nstill fucking wrong shitehead, try again.")
	conn.send("\nfucking password: ")
	preypasw2 = conn.recv(20)
	print "victim supplied: ", preypasw2, " as password."

	conn.send("\nFUCK ME. Wrong again, I am so fucking surprised, try again.")
	conn.send("\nfucking password: ")
	preypasw3 = conn.recv(20)
	print "victim supplied: ", preypasw3, " as password."

	print "Administering a bollocking to", addr
	conn.send("\nYou have proven yourself to be as useful as a marzipan dildo.\nYou connect here again, you mincing fucking CUNT, and I will tear your fucking skin off, I will wear it to your mother's birthday party, and rub your nuts up and down her leg whilst whistling Bohemian fucking Rhapsody, right?\n\nNow get out of my fucking sight.\n")
	conn.close()
s.listen(1)
