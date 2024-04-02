str = input('Select an equation:')
if str == 'Quadratic':
 A = int(input('Enter the coefficient of x^2: '))
 B = int(input('Enter the coefficient of x: '))
 C = int(input('Enter the constant: '))
 r1 = (- B + ((B**2) - (4 * A * C))**0.5) / (2 * A)
 r2 = (- B - ((B**2) - (4 * A * C))**0.5) / (2 * A)
 print('The roots of the equation are', r1, r2)
elif str == 'Cubic':
  A = int(input('Enter the coefficient of x^3: '))
  B = int(input('Enter the coefficient of x^2: '))
  C = int(input('Enter the coefficient of x: '))
  D = int(input('Enter the constant: '))
  roots = []
  for x in range(-100, 100):
    e = (A * (x**3)) + (B * (x**2)) + (C * x) + D
    if e == 0:
        roots.append(x)
  print(roots)
elif str == 'Quartic':
   A = int(input('Enter the coefficient of x^4: '))
   B = int(input('Enter the coefficient of x^3: '))
   C = int(input('Enter the coefficient of x^2: '))
   D = int(input('Enter the coefficient of x: '))
   E = int(input('Enter the constant: '))
   roots = []
   for x in range(-100, 100):
    e = (A * (x**4)) + (B * (x**3)) + (C * (x**2)) + (D * x) + E
    if e == 0:
        roots.append(x)
   print(roots)