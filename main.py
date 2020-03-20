import sys


def check_strings_map(s1,s2):
	char_frequency1 = {}
	char_frequency2 = {}
	char_dict = {}
	if len(s1)!=len(s2):
		return "false"

	#create two dictionaries that keep track of the frequencies of each char in the strings
	for i in range(len(s1)):
		c1 = s1[i]
		c2 = s2[i] 
		if char_frequency1.get(c1) == None:
			char_frequency1[c1] = 1
		else:
			char_frequency1[c1] += 1

		if char_frequency2.get(c2) == None:
			char_frequency2[c2] = 1
		else:
			char_frequency2[c2] += 1

	#sort the frequencies of the first string in descending order
	char_frequency1 = sorted(char_frequency1.items(), key = lambda x: x[1],reverse = True)
	#check if the chars can match 1-1
	for max_freq_tuple_1 in char_frequency1:
		max_freq_c2 = max(char_frequency2, key=char_frequency2.get)
		#we compare the highest frequencies of chars in both strings (and check the nth highest frequencies each nth iteration)
		#this checks to see if a char in s1 maps to two different chars in s2 (making it not 1-1)
		if max_freq_tuple_1[1] > char_frequency2[max_freq_c2]:
			return "false"
		else:
			char_frequency2[max_freq_c2] -= max_freq_tuple_1[1] #For s2, cross out the chars that max_freq_tuple_1[0] map to
	return "true"



s1 = sys.argv[1]
s2 = sys.argv[2]
print(check_strings_map(s1,s2))




