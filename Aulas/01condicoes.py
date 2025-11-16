# Ler dois valores inteiros e imprimir o maior deles.
# %%
a = int(input("Primeiro valor: "))
b= int(input("Segundo valor: "))

if a > b:
    print("O primeiro numero é o maior!")

elif b > a: 
    print("O Segundo numero é o maior!")

else:
    print("São numeros iguais!")
 
# %%

# descubra a idade de um carro

idade = int(input("Digite a idade do seu carro: "))

if idade <= 3:
    print("Seu carro é novo!")
    
else:
    print("Seu carro é velho!")