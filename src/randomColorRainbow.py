import random
import numpy as np

def random_color():
	num = random.randint(0, 2) #which color is full on
	
	color = np.array((0, 0, 0)) #create color array
	color[num] = 255 #set full color

	#create Choice Array
	choiceArray = np.array(np.zeros(2))
	j = 0
	for i in range(3):
		if(i != num):
			choiceArray[j] = i
			j += 1

	#pick and set other color
	pos = random.choice(choiceArray) #pick other color
	color[int(pos)] = random.randint(0, 255)


	return color

print(random_color())