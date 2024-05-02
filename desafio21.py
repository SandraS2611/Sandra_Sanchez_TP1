def fibonacci(numero):
    a, b = 0, 1
while a < numero:
 print(a, end=" ")
 
a, b = b, a + b + 2
print()

if __name__ == "__main__":
 # el módulo se ejecuta como programa principal
    # invoca a la función definida:
    fibonacci(10)