COUNT = 0
def recur_fibo(n):
  global COUNT
  COUNT += 1
  if n<= 1:
    return n
  else:
    return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("How many terms?: "))
if nterms <= 0:
  print("Please Enter Positive number")
else:
  print("Fibonacci Series:")
  for i in range(nterms):
    print(recur_fibo(i))
  print("Steps required using counter: ",COUNT)



COUNT = 0
x = int(input("How many Nos: "))
first = 0
sec = 1
c=0

if x <= 0:
  print("Enter a positive no.")
elif x==1:
  print("fibonacci series upto", x, "term is ", first)
else:
  while c < x:
    print(first)
    COUNT += 1
    nth = first + sec
    COUNT += 1
    first = sec
    COUNT += 1
    sec = nth
    COUNT += 1
    c += 1
    COUNT += 1

print("Steps required by counter: ", COUNT)
