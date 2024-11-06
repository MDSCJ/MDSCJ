print("This code is for 3 variable simultaneous equations...")
print("....................................................")
print(": as Ax+By+Cz = L and Dx+Ey+Fz = M and Gx+Hy+Iz= N ")
print("..........................")

while True:
    A = float(input('Enter A= '))
    B = float(input('Enter B= '))
    C = float(input('Enter C= '))
    L = float(input('Enter L= '))
    D = float(input('Enter D= '))
    E = float(input('Enter E= '))
    F = float(input('Enter F= '))
    M = float(input('Enter M= '))
    G = float(input('Enter G= '))
    H = float(input('Enter H= '))
    I = float(input('Enter I= '))
    N = float(input('Enter N= '))

    k = A*(E*I - H*F) - B*(D*I - G*F) + C*(D*H - G*E)

    if k == 0:
        print("Can't find an answer using this method (determinant is 0)")
    else:
        answerx = (L*(E*I - H*F) + M*(H*C - B*I) + N*(B*F - E*C)) / k
        answery = (L*(G*F - D*I) + M*(A*I - G*C) + N*(D*C - A*F)) / k
        answerz = (L*(D*H - G*E) + M*(G*B - A*H) + N*(A*E - B*D)) / k
        print(f"x = {answerx}")
        print(f"y = {answery}")
        print(f"z = {answerz}")
        print("....................................................")
        print('HAVE FUN')
    z = input('Type "1" to redo the code or anything else to exit: ')
    if z != "1":
        print("HAVE A NICE DAY...")
        break
