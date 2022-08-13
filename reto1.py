numero = int(input("Digite un numero entero: "))

resultado = numero%3
print(f'el resultado de {numero} es: {resultado}')

#Condicional Simple en python
if(resultado==0):
    print("es multiplo de 3")
else:
    print("no es multiplo de 3")    
    print("fin del programa")