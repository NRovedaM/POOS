#Peça ao usuário uma temperatura e use if para determinar se está "frio“(<20), "morno“(>20 e <26) ou "quente“(>27) com base em intervalos de valores.
temp = float(input("insira a temperatura atual em Celsius: "))

if temp < 20:
    print("está frio")
elif temp <= 26:
    print("está morno")
elif temp > 26:
    print("está quente")
else:
    print("valor invalido")