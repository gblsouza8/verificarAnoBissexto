def verificarAno(ano):
    if ano < 2025 and ano % 4 == 0:
        print(ano,"foi um ano bissexto")
    elif ano > 2025 and ano % 4 == 0:
        print(ano,"será um ano bissexto")
    elif ano < 2025 and ano % 4 != 0:
        print(ano,"não foi um ano bissexto")
    elif ano > 2025 and ano % 4 != 0:
        print(ano,"não será um ano bissexto")
    else:
        print(ano,"não é um ano bissexto")

    
