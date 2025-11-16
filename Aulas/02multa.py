#%%
# pergunte a velocidade de um carro, 
# supondo um valor inteiro. Caso ultrapasse 
# 110km/h, exiba uma mensagem dizendo que o 
# usuario foi multado.Neste caso, exiba o valor damulta,
# cobrando R$ 5,00 por km acima de 110.

velocidade = int(input("Digite a velocidade do seu carro: "))

if velocidade > 60:
    multa = (velocidade - 60) * 5
    print(f"MULTADO! Valor da multa R$ {multa:.2f}")

else:
    print("Continue assim, não seja apressado. Respeite as leis de trânsito!")
