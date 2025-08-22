#Olá! Hoje iremos fazer o cálculo do desconto do INSS 2025.

#O cidadão informa para o programa quanto recebe de salário e como ele exerce sua atividade profissional.
salário = float(input("Informe seu salário:"))
vinculação = input("Informe como você exerce sua atividade profissional:")


if vinculação == "clt": #Se o cidadão trabalhar de carteira assinada, seu desconto INSS será calculado da seguinte forma:

    if salário <= 1518.00:
        inss = salário * 0.075

    elif salário > 1518.00 and salário <= 2793.88:
        inss = salário * 0.09 - 22.77

    elif salário > 2793.88 and salário <= 4190.83:
        inss = salário * 0.12 - 106.59
    
    elif salário > 4190.83 and salário <= 8157.41:
        inss = salário * 0.14 - 190.40

    elif salário > 8157.41:  
        inss = salário * 0.14 - 190.40 #Mesmo que o salário do cidadão passe de R$8.157,41, seu desconto INSS já atingiu o limite.
    



elif vinculação == "autônomo": #Se o cidadão for autônomo, seu desconto INSS será calculado da seguinte forma: 

    if salário <= 8157.41:
        inss = salário * 0.20
    else:
        inss = salário * 0.14 #Mesmo que o salário do cidadão passe de R$8.157,41, seu desconto INSS já atingiu o limite.
    

elif vinculação == "empresário": #Se o cidadão for empresário, seu desconto INSS será calculado da seguinte forma:
    
    if salário <= 8157.41:
        inss = salário * 0.11
    else:
        inss = salário * 0.14 #Mesmo que o salário do cidadão passe de R$8.157,41, seu desconto INSS já atingiu o limite.


print("Você pagará por mês R$", round(inss, 2), sep="", end=" ")
print("de INSS.")
#Por fim, o programa irá mostrar quanto o cidadão terá que pagar de INSS.
