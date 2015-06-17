##########################################
#              Crowd Sourced             #  
#   TRNG(True Random Number Generator)   #
#         Written by Unkillable          #  
#            Copyright 2015              #
##########################################
import TRNG
import time
if __name__ == "__main__":
  while True:
    try:
        print "Generating random string.." #State what is going to happen
        rng = TRNG.RNG() #Start up a TRNG instance
        rng.generate() #Generate some fresh data
        rng.xor() #Xor the data
        rng.randomize() #Multiply by time stamp in micro seconds
        rng.xor() #Xor the data again
        rng.hex() #Convert to hex
        rng.hexToChars() #Convert printable hex values to chars
        rng.shift() #Split data in half and combine data while shifting pos by 1
        rng.append() #Append to bits.txt
        print rng.getSelf() #Show the resulting string
        print "Sleeping for 120 seconds..." #State we are ready to sleep
        time.sleep(120) #Sleep for two minutes for more entropy
    except Exception as e:
        print "Error: " + str(e)
        print "Something went wrong. Retrying.."
