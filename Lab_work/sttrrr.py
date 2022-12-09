
# reverse

str = 'nidhi'[::-1]
print(str)

# strip

str1 = '------h------e------ll-----o-------'
print(str1.strip('-'))
print(str1.lstrip('-'))
print(str1.rstrip('-'))

# replace

print(str1.replace('-',''))

# count

str2 = 'This is my long msg so that I count what I want. I know that its not long enough. '
print(str2.count('this'))
print(str2.count("i"))

# find

print(str2.find("I"))
print(str2.rfind("I"))
print(str2.index("I"))

# split

print(str2.split())

# join
# strip
# remove all vowel

x = ["a","e","i","o","u"]
for x in str2:
    str2.replace(x,'')
print(str2)