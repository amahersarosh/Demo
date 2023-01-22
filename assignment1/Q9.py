x=int(input("Enter number of student's weight to be calculated"))
weights_in_lbs=[]
weights_in_kg=[]
#appending the elements into the list
for i in range(x):
    weights_in_lbs.append(int(input("weight {} \n".format(i+1))))
print(weights_in_lbs)
#converting lbs to kilogram with exactly 2 decimal places
for i in range(len(weights_in_lbs)):
    y=0.45359237 #1lbs= 0.45359237kg
    temp=round(weights_in_lbs[i]*y,2)
    weights_in_kg.append(temp)
    temp=0
print(weights_in_kg)