#!/usr/bin/env python3

import re

def rearrange_name(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)
	if result is None:
		return name 
	return "{} {}".format(result[2], result[1])

#print(rearrange_name("Peter, Kevin"))
#print(rearrange_name("Jovi, Bon"))
#print(rearrange_name("Kennedy, John F."))
