#%%
# Considere a empresa de telefone Tchau.
# Abaixo de 200 minutos, a empresa cobra R$0,20 por minuto.
# Entre 200 e 400 minutos, o preço é R$0,18. Acima de 400 minutos,
# o preço por minuto é R$0,15. Calcule sua conta de telefone.
# Adicionar a promoção para mais de 800 minutos é R$0,08

minutos = int(input("Informe quantos minutos voce gastou: "))

if minutos < 200:
    preco = 0.2
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08

print(f"Sua conta tem o valor de {preco*minutos:.2f}")

# %%
