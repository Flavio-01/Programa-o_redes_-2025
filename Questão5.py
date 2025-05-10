# Solicita ao usuário um número de porta
porta = int(input("Digite o número da porta: "))
# HTTP(80), HTTPS (443), SMIP(25) e SSH (22)
if porta => 80:
    print(" HTTP.")
elif porta == 443:
    print("HTTPS.")
elif porta == 25:
    print(" SMIP.")
elif porta == 22:
    print(" SSH.")
else:
    print("A porta desconhecida.")
