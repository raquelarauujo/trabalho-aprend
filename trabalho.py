# Alunas:
# Naira Natasha Higa Miyahara 2314290030
# Bruna Mayumi Miyahara 2314290015
# Raquel Araujo Pereira da Silva 2314290103
# Láysla Maria Monteiro De Andrade 2314290036


def calcular_iof(dias):
    tabela_iof = {
        1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80, 7: 76, 8: 73, 9: 70, 10: 66,
        11: 63, 12: 60, 13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40, 19: 36, 20: 33,
        21: 30, 22: 26, 23: 23, 24: 20, 25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0
    }
    return tabela_iof.get(dias, 0)


def calcular_ir(dias):
    if dias <= 180:
        return 22.5
    elif dias <= 360:
        return 20.0
    elif dias <= 720:
        return 17.5
    else:
        return 15.0


def calcular_rendimento(valor_inicial, dias):
    taxa_anual = 0.1415
    taxa_diaria = (1 + taxa_anual) ** (1/365) - 1
    valor_final = valor_inicial * ((1 + taxa_diaria) ** dias)
    rendimento_bruto = valor_final - valor_inicial


    iof_percentual = calcular_iof(dias)
    desconto_iof = rendimento_bruto * (iof_percentual / 100) if dias <= 30 else 0


    ir_percentual = calcular_ir(dias)
    rendimento_pos_iof = rendimento_bruto - desconto_iof
    desconto_ir = rendimento_pos_iof * (ir_percentual / 100)


    rendimento_liquido = rendimento_pos_iof - desconto_ir
    valor_liquido_total = valor_inicial + rendimento_liquido


    return {
        "valor_bruto": round(valor_final, 2),
        "rendimento_bruto": round(rendimento_bruto, 2),
        "desconto_iof": round(desconto_iof, 2),
        "percentual_iof": iof_percentual,
        "desconto_ir": round(desconto_ir, 2),
        "percentual_ir": ir_percentual,
        "valor_liquido": round(valor_liquido_total, 2)
    }

try:
    valor = float(input("Digite o valor a ser investido: R$ "))
    dias = int(input("Digite o tempo do investimento (em dias): "))


    if valor <= 0 or dias <= 0:
        print("Valor e dias devem ser maiores que zero.")
    else:
        resultado = calcular_rendimento(valor, dias)


        print("\n===== RESULTADO DA SIMULAÇÃO =====")
        print(f"Valor Bruto Final     : R$ {resultado['valor_bruto']}")
        print(f"Rendimento Bruto      : R$ {resultado['rendimento_bruto']}")
        print(f"Desconto IOF ({resultado['percentual_iof']}%): R$ {resultado['desconto_iof']}")
        print(f"Desconto IR ({resultado['percentual_ir']}%): R$ {resultado['desconto_ir']}")
        print(f"Valor Líquido         : R$ {resultado['valor_liquido']}")
except ValueError:
    print("Entrada inválida! Certifique-se de digitar números válidos.")