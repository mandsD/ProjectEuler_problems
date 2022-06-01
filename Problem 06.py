""" The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """

soma = 0
quadrado_soma = 0

for x in range(101):
    soma = soma + (x**2)
for x in range(101):
    quadrado_soma += x
quadrado_soma = quadrado_soma**2

print(quadrado_soma - soma)
