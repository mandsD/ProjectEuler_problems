""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. """

c = 0
sum = 0
while c < 1000:
  if c%3 == 0:
    sum = sum + c
  elif c%5 == 0:
    sum = sum + c
  c = c + 1
print()
print(soma)
