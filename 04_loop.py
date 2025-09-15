#for loop
li = ["a", "b", "c"]
for i in li:
    print(i)
    
tup = ("a", "b", "c")
for i in tup:
    print(i)
    
s = "a"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)
    
#for-range
for x in range(2, 6):
  print(x) 
  
#while loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello World")

#nested loop
months = ["jan", "feb", "mar"]
days = ["sun", "mon", "tue"]
for x in months:
  for y in days:
    print(x, y)
    
#continue
for letter in 'sagar':
    if letter == 'g' :
        continue
    print('Current Letter :', letter)
    
#break
for letter in 'sagar':
    if letter == 'a':
        break
    print('Current Letter :', letter)
