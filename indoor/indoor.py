def converter_para_minusculas(texto_maiusculo):
    # O método .lower() transforma todos os caracteres em minúsculos
    return texto_maiusculo.lower()

# Exemplo de uso:
entrada =  input()
resultado = converter_para_minusculas(entrada)

print(f"{resultado}")
