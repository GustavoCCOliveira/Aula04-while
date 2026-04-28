def veirifcar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota tem que estar entre 0 a 10 ")
        nota = float(input("Digite a nota novamente: "))
    return nota 
notaA = float(input("Digite a primeira nota:  "))
while notaA < 0 or notaA > 10:
    print("A nota tem que estar entre 0 a 10 ")
    notaA = float(input("Digite a nota novamente: "))
notaB = float(input("Digite a segunda nota:  "))
while notaB < 0 or notaB > 10:
    print("A nota tem que estar entre 0 a 10 ")
    notaB = float(input("Digite a nota novamente: "))

media= (notaB + notaA) / 2
print(media)