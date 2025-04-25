a = 15 #the time they use by walking to the bus station
b = 75 #the time (in minutes) of bus ride
c = a + b #total time of the first way

d = 90 # the time (in minutes) of car ride
e = 5 #the time they use walking from parking lot to the company
f = d + e #total time of the second way

print(c,f)
'''
because c=90<f=95
the first way (bus) is faster than the second (drive)
'''

x = True
y = False
w = x and y
print("w:",w)
'''
Truth table for w (x and y)
| x     | y     | w (x and y) | x or y 
| True  | True  | True        | True
| True  | False | False       | True
| False | True  | False       | True
| False | False | False       | False
'''
