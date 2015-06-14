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
		print "Generating random string.." #State what is going to happen
		rng = TRNG.RNG() #Start up a TRNG instance
		rng.generate() #Generate some fresh data
		rng.xor() #Xor the data
		rng.randomize() #Multiply by time stamp in micro seconds
		rng.xor() #Xor the data again
		rng.hex() #Convert to hex
		rng.hexToChars() #Convert printable hex values to chars
		rng.shift() #Split data in half and combine data while shifting pos by 1
		s.send("PRIVMSG #entropy :%s\r\n" % rng.getSelf())
		rng.append()
		print "Sleeping for two minutes.."
		time.sleep(120)
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
