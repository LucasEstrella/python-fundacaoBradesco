notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calcular media
mediaFinal = (notaA + notaB) / 2

#verificação
if mediaFinal >= 7.0:
    print("A Média: %.1f - APROVADO"%mediaFinal)
else:
    print("A média: %.1f - REPROVADO"%mediaFinal)