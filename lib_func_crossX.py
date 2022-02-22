
def solveLinear(func_values):

	y = 0
	y = y - float(func_values[-1][0])
	y = y / float(func_values[0][0])

	return y


def solveQuadratic(func_values):

	p = func_values[1][0] / func_values[0][0]
	q = func_values[2][0] / func_values[0][0]

	y_1 = -p/2 + ((p/2)**2 - q)**0.5
	y_2 = -p/2 - ((p/2)**2 - q)**0.5

	return [y_1, y_2]

def solveCubical(func_values):

	a = func_values[0][0]
	b = func_values[1][0]
	c = func_values[2][0]
	d = func_values[3][0]

	solutions = []

	if d == 0:
		solutions.append(0)
		solutions.append(solveQuadratic([[a, 2], [b, 1], [c, 0]])[0])
		solutions.append(solveQuadratic([[a, 2], [b, 1], [c, 0]])[1])
		return solutions
	else:
		pass
