import TRNG
#Lets endlessly get some numbers
while True:
	print "Generating random bits.."
	rng = RNG()
	rng.generate()
	rng.xor()
	rng.hex()
	rng.append()
	print "Sleeping for two minutes.."
	time.sleep(120)