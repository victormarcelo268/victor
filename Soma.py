def soma(a, b):
    return a + b

# Função para formatar sem .0
def formatar_resultado(valor):
    if valor == int(valor):
        return str(int(valor))
    else:
        return str(valor).replace('.', ',')

# Exemplo de uso
numero1 = float(input("Digite o primeiro número: ").replace(',', '.'))
numero2 = float(input("Digite o segundo número: ").replace(',', '.'))

resultado = soma(numero1, numero2)

print("Resultado da soma:", formatar_resultado(resultado))
