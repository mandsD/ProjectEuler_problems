""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """

def calculo():
	perimetro = 1000
	for a in range(1, perimetro + 1):
		for b in range(a + 1, perimetro + 1):
			c = perimetro - a - b
			if a * a + b * b == c * c:
				return str(a * b * c)

print(calculo())
