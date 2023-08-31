#18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
a = 0
b = 1
print("Los primeros 10 números de la sucesión de Fibonacci son:")
for i in range(10):
    print(a)
    a, b = b, a + b