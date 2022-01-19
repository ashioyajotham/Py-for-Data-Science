#The clearest difference between a list and a tuple is the syntax used to create them ie 
# tuples prefer to use paranthesis whereas lists like to see brackets,
# although it's also posiible to create a tuple from just a set of values separated by commas. 

tuple_1 = (1, 2, 3, 4, )
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

#It is possible to create an empty tuple - paranthesis are required then
empty_tuple = ()

#If you want to create a one-element tuple, you have to take into consideration 
# the fact that, due to syntax reasons 
# ( a tuple has to be distinguishable from an odinary, single value), 
# you must end the value in a comma:
one_element_tuple_1 = (1,)
one_element_tuple_2 = 1.,

#Removing any comma won't spoil the program in any syntactical case, but you will in stead
#get two single variables, not tuples
