ips = []
while True:
    ip = input("Digite ume endereço IP :")
    if ip.lower() == "fim":
       break 
    ips.append(ip)        


print("Endereços IP cadastrados:")
for ip in ips:
    print(ip)