n = 0
while n < 4:
    n += 1
    print(n,end=" ") #print a space rather than a newline character
print("\n-------")
i = 10
while i > 0:
    i -= 3
    print("*")
    if i <= 3:
        break
else:
    print("*")
print("\n--------------")
# Example 1
print("Ex 1")
for i in range(1, 4, 2):
    print("i is "+ str(i))
    print("*")

# Example 2
print("Ex 2")
for i in range(1, 4, 2):
    print("*", end="")

# Example 3
print("Ex 3")
for i in range(1, 4, 2):
    print("*", end="**")

# Example 4
print("Ex 4")
for i in range(1, 4, 2):
    print("*", end="**")
print("***")
print()
x = "20"
y = "30"
print(x > y)
print()
s = "Hello, Python!"
print(s[-14:15])
print(len(s))
print()
lst = ["A", "B", "C", 2, 4]
del lst[0:-2]
print(lst)
print()
dict = { 'a': 1, 'b': 2, 'c': 3 }
print("here's the items in the dict")
for item in dict:
    print(item)
    print()
print("here are the keys in the dict")
x = dict.keys()
print(x)
print("here are the values in the dict")
y=dict.values()
print(y)
print()
print('question 16')
s = 'python'
print("s is originally "+s)
for i in range(len(s)):
    i = s[i].upper()
print(s, end="")

