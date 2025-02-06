peso = 65
altura = float(1.74)

imc = peso / (altura*altura)


print('seu imc é de {:.2f},e está normal'.format(imc))
if imc < 18.5:
    print('Magreza')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal')
elif imc == 25.0 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc <= 39.9:
    print('obesidade')
else:
    print('Obesidade grave')
