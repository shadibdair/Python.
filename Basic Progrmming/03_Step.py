# importing libraries into a script

import re 

string = "'I AM SHADI', and i am The Best."
print(string)

new = re.sub('[a-z]','',string)
print(new)

new1 = re.sub('[.,\']','',string)
print(new1)

string  = string +"5 6232-244"
print(string)


# 'I AM SHADI', and i am The Best.
# 'I AM SHADI',    T B.
# I AM SHADI and i am The Best
# 'I AM SHADI', and i am The Best.5 6232-244