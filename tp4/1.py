x = 0
while x < 30:
    print(str(x+1))
    x = x + 1
    if x == 15:
        print('La ejecucio  n del bucle se rompio cuando x era ' + str(x))
        break
    if x in [4, 6, 10]:
        print('El valor ' + str(x) + ' de x fue saltado')
        continue
