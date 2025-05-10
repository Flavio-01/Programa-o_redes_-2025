#Se o número IP pertence a rede 192.168.1.0./24
while True:

    ip = input("Digite o número ip: ")
    ip_inicial = "192.168.1.1"
    ip_final = "192.168.1.65"

    if ip_inicial <= ip <= ip_final:
        print("Ip válido!")

    else: 
        print("Ip inválido!")