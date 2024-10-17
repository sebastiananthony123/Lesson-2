#Three cyclist are riding at the speed 10,20,30 kmph. Fing the average and compare which cyclist is riding slower than the average speed?
s1 = int(input("Enter your first speed : "))
s2 = int(input("Enter your second speed : "))
s3 = int(input("Enter your third speed : "))

average = (s1+ s2 + s3)/3
print("The average speed is : ",average)

if s1<average:
   print("Speed 1 is slower than  average with the distance of ", average-s1)

if s2<average:
   print("Speed 2 is slower than  average with the distance of ", average-s2)

if s3<average:
   print("Speed 3 is slower than  average with the distance of ", average-s3)