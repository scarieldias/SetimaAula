# Exemplo de string

texto = "Olá, mundo!"

# Fatiar do inicio até um indice especifico

print(texto[:5]) # saida: "Ola, "

# Fatiar a partir de um indice especifico ate o final

print(texto[5:]) # saida: "Mundo!"

# Fatiar do inicio ate o final, com um passo especifico

print(texto[::2]) # saida: "O    ,ud!"

# Fatiar com inicio e fim especificos

print(texto[4:9]) # saida: "Mund"

# Fatiar com passo negativo para inverter uma string

print(texto[::-1]) # saida: "!odnuM  ,álO"
