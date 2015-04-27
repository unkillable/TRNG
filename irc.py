##########################################
#              Crowd Sourced             #  
#   TRNG(True Random Number Generator)   #
#         Written by Unkillable          #  
#            Copyright 2015              #
##########################################
import TRNG
import socket
import multiprocessing
import time
def irc(s):
	nick = "NICK RNG\r\n"
	user = "USER RNG RNG RNG :RNG\r\n"
	s.send(nick)
	s.send(user)
	connected = True
	while connected == True:
		data = s.recv(1024)
		print data
		if "PING " in data:
			s.send("PONG %s\r\n" % data.split(" ")[1])
		if " 396 " in data:
			s.send("JOIN #entropy\r\n")
def rng(s):
	while True:
		print "Generating random bits.."
		rng = TRNG.RNG()
		rng.generate()
		rng.xor()
		rng.hex()
		s.send("PRIVMSG #entropy :%s\r\n" % rng.getSelf())
		rng.append()
		print "Sleeping for two minutes.."
		time.sleep(1201)
if __name__ == "__main__":
	jobs = []
	s = socket.socket()
	s.connect(("irc.asia", 6667))
	i = multiprocessing.Process(target=irc, args=(s,))
	jobs.append(i)
	r = multiprocessing.Process(target=rng, args=(s,))
	jobs.append(r)
	for job in jobs:
		job.start()
