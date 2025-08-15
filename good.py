import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
print(hour)
if (hour>0 and hour<12):
  print("Good morning sir")
elif (hour>=12 and hour<18):
  print("Good evening  sir")
elif(hour>=18 and hour<24):
  print("Good morning sir")
