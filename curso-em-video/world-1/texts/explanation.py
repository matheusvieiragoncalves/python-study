


phrase = 'Course in video python'

print(phrase[5]) # get character at position 5
print(phrase[3:12]) # get characters between 3 and 12
print(phrase[0:15:2]) # get characters between 0 and 15, of 2 in 2
print(phrase[:9]) # get characters between start and 9
print(phrase[10:]) # get characters between 10 and end
print(phrase[5::3]) # get characters between 10 and end, of 3 in 3
print(phrase[::3]) # get characters of the whole phrase, of 3 in 3

# analysis

print(f'This phrase has {len(phrase)} characters')
print(f'This phrase has {phrase.count("o")} letters "o"')
print(f'This phrase has {phrase.count("o", 0, 13)} letters "o" between 0 and 13')
print(f'This phrase has {phrase.find("deo")} starting at position "deo"')
print(f'This phrase has {phrase.find("android")} starting at position "android". (It returns -1 when not found)')
print(f'This phrase has "Course" in phrase? {"Course" in phrase} ')

# transformation
print(phrase.replace('python', 'android'))
print(phrase.upper())
print(phrase.lower())
print(phrase.capitalize())
print(phrase.title())

phrase2 = '   Learn Python  '

print(phrase2.strip()) # remove spaces at the beginning and at the end
print(phrase2.rstrip()) # remove spaces at the right
print(phrase2.lstrip()) # remove spaces at the left

# division
print(phrase.split()) # split the phrase into a list of words

# joining
print('-'.join(phrase)) # join the characters of the phrase with '-'
print('-'.join(phrase.split())) # join the words of the phrase with '-'

print(""" This is a long text
 that spans multiple lines.""")
