def calcular_valor_colecao_cds():
    
    quantidade_cds = int(input("Digite quantos CDs tem na coleção: "))

    
    valor_total = 0

    
    for i in range(quantidade_cds):
        valor_cd = float(input(f"Digite o valor do CD {i+1}: "))
        valor_total += valor_cd

    
    if quantidade_cds > 0:
        valor_medio_por_cd = valor_total / quantidade_cds
    else:
        valor_medio_por_cd = 0

    
    print(f"Valor total investido na coleção foi: R${valor_total:.2f}")
    print(f"Valor médio gasto em cada CD foi: R${valor_medio_por_cd:.2f}")

calcular_valor_colecao_cds() 