number = int(input("enter number: "))
counter = 0
while(counter <= 10):
  answer = counter*number
  print(str(number) + "*" + str(counter) + "=" + str(answer))
  counter = counter + 1