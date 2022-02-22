"""
Libary for the function calculation program.
"""

import lib_func_crossX
from copy import deepcopy

def symmetry(func_values):		#bestimmt das Symmetrieverhalten

	even = 0
	odd = 0

	for i in func_values:
		if i[1] % 2 == 0:
			even += 1
		else:
			odd += 1

	if (even != 0) and (odd != 0):
		return "nicht symmetrisch!"
	elif (even == 0) and (odd != 0):
		return "punktsymmetrisch!"
	elif (even != 0) and (odd == 0):
		return "achsensymmetrisch!"


def pos_infinite(func_values):		#bestimmt das Verhalten gegen positiv Unendlich

	test = float(func_values[0][0]) * 10000 ** float(func_values[0][1])
	if test > 0:
		return "Für x gegen positiv unendlich geht y gegen positiv unendlich"
	elif test < 0:
		return "Für x gegen positiv unendlich geht y gegen negativ unendlich"
	else:
		return "Für x gegen positiv unendlich bleibt y = 0"


def neg_infinite(func_values):		#bestimmt das Verhalten gegen negativ Unendlich

	test = float(func_values[0][0]) * (-10000) ** float(func_values[0][1])
	if test > 0:
		return "Für x gegen negativ unendlich geht y gegen positiv unendlich"
	elif test < 0:
		return "Für x gegen negativ unendlich geht y gegen negativ unendlich"
	else:
		return "Für x gegen negativ unendlich bleibt y = 0"


def closeTo0(func_values):		#bestimmt das VErhalten nahe 0

	smallestPart = func_values[-1]

	small_func = str(smallestPart[0]) + "x^" + str(smallestPart[1])

	return "Das Verhalten nahe Null kann durch die Funktion {} beschrieben werden".format(small_func)


def derivative(func_values):

	func_values_2 = deepcopy(func_values)
	drvtv = ""

	for i in func_values_2:
		if i[1] >= 1:
			i[0] = i[0] * i[1]
			i[1] = i[1] - 1
		elif i[1] == 0:
			func_values_2.pop(func_values_2.index(i))

	for j in func_values_2:
		drvtv = drvtv + " +({})x^{}".format(j[0], j[1])

	drvtv = drvtv.replace("(", "")
	drvtv = drvtv.replace(")", "")
	drvtv = drvtv.replace("+-", "-")
	drvtv = drvtv.replace("x^0.0", "")
	drvtv = drvtv.replace("x^1.0", "x")

	if drvtv == "":
		drvtv = 0

	return "Die Ableitungsfunktion ist   {}".format(drvtv)


def derivativeOfDerivative(func_values):

	func_values_2 = deepcopy(func_values)
	drvtv = ""

	for i in func_values_2:
		if i[1] >= 1:
			i[0] = i[0] * i[1]
			i[1] = i[1] - 1
		elif i[1] == 0:
			func_values_2.pop(func_values_2.index(i))

	for j in func_values_2:
		if j[1] >= 1:
			j[0] = j[0] * j[1]
			j[1] = j[1] - 1
		elif j[1] == 0:
			func_values_2.pop(func_values_2.index(j))

	for k in func_values_2:
		drvtv = drvtv + " +({})x^{}".format(k[0], k[1])

	drvtv = drvtv.replace("(", "")
	drvtv = drvtv.replace(")", "")
	drvtv = drvtv.replace("+-", "-")
	drvtv = drvtv.replace("x^0.0", "")
	drvtv = drvtv.replace("x^1.0", "x")

	if drvtv == "":
		drvtv = 0

	return "Die zweite Ableitungsfunktion ist   {}".format(drvtv)


def zero(func_values):

	if func_values[0][1] == 0:

		if func_values[0][0] == 0:

			return "Nullstellen auf gesammter x-Achse"

		else:

			return "Keine Nullstellen"

	elif func_values[0][1] == 1:

		return lib_func_crossX.solveLinear(func_values)

	elif func_values[0][1] == 2:

		ys = lib_func_crossX.solveQuadratic(func_values)

		return "Die Nullstellen liegen bei {} und {}!".format(ys[0], ys[1])

	elif func_values[0][1] == 3:

		ys = lib_func_crossX.solveCubical(func_values)

		return "Die Nullstellen liegen bei: {}".format(ys)

	else:

		return "Yet an error!"




