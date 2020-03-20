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





s1 = sys.argv[1]
s2 = sys.argv[2]
print(check_strings_map(s1,s2))
