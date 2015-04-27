##########################################
#              Crowd Sourced             #  
#   TRNG(True Random Number Generator)   #
#         Written by Unkillable          #  
#            Copyright 2015              #
##########################################
import praw 
import time
import re
class RNG():
	def __init__(self): 
		#Config variables
		self.SUB_NAME = "python" #this could be used if you want gen numbers using a specific sub reddit. NOT RECOMMENDED
		self.SCAN_LIMIT = 1000
		self.r = praw.Reddit(user_agent='my_reddit_app')
		self.random_string = ""

	def generate(self):
		#subreddit = r.get_subreddit(SUB_NAME) If you decide to use a sub reddit. (ILLEGAL)
		new_submissions =  self.r.get_new(limit = self.SCAN_LIMIT)
		for ID, submission in enumerate(new_submissions):
			first_timestamp = submission.created_utc
			second_timestamp = next(new_submissions).created_utc
			third_timestamp = next(new_submissions).created_utc
			fourth_timestamp = next(new_submissions).created_utc
			if(int(second_timestamp) - int(first_timestamp)) > (int(fourth_timestamp) - int(third_timestamp)):
				self.random_string += "0"
			elif(int(second_timestamp) - int(first_timestamp)) < (int(fourth_timestamp) - int(third_timestamp)):
				self.random_string += "1"
			else:
				pass
			#print self.random_string

	def xor(self):
		if self.random_string < self.SCAN_LIMIT:
			self.random_string = self.random_string + "0"
		#split = [self.random_string[i:i+2] for i in range(0, len(self.random_string), 2)]
		for pos, bit in enumerate(self.random_string):
			next_bit = self.random_string[pos+1]
			result = int(bit) ^ int(next_bit)
			self.random_string = self.insert(self.random_string, str(bit), pos+1)
		#self.random_string = random_string
		#print self.random_string

	def hex(self):
		self.random_string = ''.join(hex(int(a, 2))[2:] for a in self.random_string.split())

	def write(self):
		f = open("bits.txt", "w+")
		f.write(self.random_string)
		f.close()

	def append(self):
		f = open("bits.txt", "a+")
		f.write(self.random_string)
		f.close()

	def insert (self, source, insert, pos):
		return source[:pos]+insert+source[pos:]

	def getSelf(self):
		return self.random_string