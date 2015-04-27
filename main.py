##########################################
#              Crowd Sourced             #  
#   TRNG(True Random Number Generator)   #
#         Written by Unkillable          #  
#            Copyright 2015              #
##########################################
import TRNG
if __name__ == "__main___":
	while True:
		#Lets endlessly get some numbers
		print "Generating random bits.."
		rng = RNG()
		rng.generate()
		rng.xor()
		rng.hex()
		rng.append()
		print "Sleeping for two minutes.."
		time.sleep(120)