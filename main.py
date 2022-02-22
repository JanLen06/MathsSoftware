import lib_functions

#Instructions
print("Beachten:")
print("beim Eingeben der Funktion werden")
print("Luecken zwischen Exponent und dem")
print("naechsten Vorzeichen gemacht!")
print("Außerdem bei einer einzelnen Zahl")
print("x^0 ergaenzen und bei einem einzelnen")
print("x bitte eine 1 ergaenzen!")
print("Desweiteren wird statt dem Komma")
print("ein Punkt verwendet!")
print("Ein Beispiel:")
print("+3x^4.0 -5x^2.0 +1x^1.0 -9.5x^0.0 \n")

#Input
func = input("f(x)= ")

#Transformation
func_bricks = list(func.split(" "))

for i in range(0, len(func_bricks)):
	func_bricks[i] = list(func_bricks[i].split("x^"))

func_bricks.sort(key=lambda tup: tup[1], reverse=True)

for i in range(0, len(func_bricks)):
	for j in range(0, 2):
		func_bricks[i][j] = float(func_bricks[i][j])


print(func_bricks)

#Run
print("\n")
print("Analysepunkte: \n")
print(lib_functions.symmetry(func_bricks))
print(lib_functions.pos_infinite(func_bricks))
print(lib_functions.neg_infinite(func_bricks))
print(lib_functions.derivative(func_bricks))
print(lib_functions.derivativeOfDerivative(func_bricks))
print(lib_functions.zero(func_bricks))
