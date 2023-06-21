# What is a list?

#i = ["this", "is", "a", "test"] #create a list
#print(type(i)) #prints the type of data i is
#print(len(i)) #prints the length of elements in the list
#print ("is" in i) #checks to check if "is" is in the list
#print (i[1:3]) # prints items 1-2 in the list - 3 does not get printed

## Modifying the contents of a list

cars = ["honda", "ford", "nissan", "subaru"]
print (cars)
cars.append("toyota")
print (cars)

cars.insert(1, "ford sucks")
print(cars)
cars.insert(6, "batmobile")
print(cars)

cars.remove("ford")
print(cars)

cars.pop(0)
print(cars)

cars[1] = "motorcycle"
print(cars)

for x, element in enumerate(cars):
    print (x, element)
# This will add input into a list
message = ["Hello"]
n = 4

while n >=0:
    message.append(input("Enter in a message:"))
    n -= 1

print(message)

print()
userid = 10
accountnum = 314
x = [userid, accountnum]
print(x)
      
#lists & tuples
#lists are immutable (meaning they can not be changed)
def file_size(file_info):
    name, type, size= file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21



def skip_elements(elements):
	# code goes here
	new_list = []
	for x, element in enumerate(elements):
		if x % 2 ==0:
			new_list.append(elements[x])
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#list comprehension
x = 3

multiples = [x*3 for x in range(1, 11)]
print (multiples)
# instead of creating an empty list then running a for loop to append that list
# we can use list comprehension built into python to complete a sequence, we can 
# create a list based on a range

def odd_numbers(n):
	return ([x for x in range(1, n+1)if x % 2 != 0])

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []