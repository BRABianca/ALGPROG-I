while True:
    number = int(input("Informe um número de 1 a 12: "))
    if number == 1:
        mes = "January"
    elif number == 2:
        mes = "February"
    elif number == 3:
        mes = "March"
    elif number == 4:
        mes = "April"
    elif number == 5:
        mes = "May"
    elif number == 6:
        mes = "June"
    elif number == 7:
        mes = "July"
    elif number == 8:
        mes = "August"
    elif number == 9:
        mes = "September"
    elif number == 10:
        mes = "October"
    elif number == 11:
        mes = "November"
    elif number == 12:
        mes = "December"
    else:
        input("Por gentileza, informe apenas um número de 1 a 12: ")
    break
print(f"O mês correspondente é: {mes}")
