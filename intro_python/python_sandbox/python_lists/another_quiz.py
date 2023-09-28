##6
#def guest_list(guests):
#	for x, element in enumerate(guests):
#		name, age, job = guests[x]
#		print("{} is {} years old and works as {}".format(name, age, job))
#
#guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
#
##Click Run to submit code
#"""
#Output should match:
#Ken is 30 years old and works as Chef
#Pat is 35 years old and works as Lawyer
#Amanda is 25 years old and works as Engineer
#"""

##2
#def pig_latin(text):
#  say = ""
#  # Separate the text into words
#  words = text.split()
#  for word in words:
#    # Create the pig latin word and add it to the list
#    say += word[1:] + word[0:1]+ "ay" + " "
#    # Turn the list back into a phrase
#  return say
#		
#print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
#print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

#1

#filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
#newfilenames = []
## Generate newfilenames as a list containing the new filenames
## using as many lines of code as your chosen method requires.
#for x, i in enumerate(filenames):
#        if i.endswith(".hpp"):   
#            index = i.index(".")
#            newfilenames.append(i[:index] + ".h")
#
#        else:
#              newfilenames.append(i)         
#print(newfilenames) 
## Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def group_list(group, users):
  members =""
  for x in users:
    members += x + " , "
  return "{}: {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"