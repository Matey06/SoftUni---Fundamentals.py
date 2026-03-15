import re

text = input()
#With this pattern I create a group and so I don't print the underscore
pattern = r'\b_([a-z0-9]+)\b'

matches = re.findall(pattern, text, re.IGNORECASE)

print(','.join(matches))

#---> In this solution my pattern is r'\b_[a-z0-9]+\b' ---> At first I didn't know I can create the group (still works)

#no_underscore_matches = []

#if matches:
    #for match in matches:
        #no_underscore_matches.append(match[1:])

#print(','.join(no_underscore_matches))
