def soma_ate_n(n):
    if n==1:
        return 1
    else: 
        return n+soma_ate_n(n-1)

numero_usuario=int(input("Digite um numero para somar: "))

resultado=soma_ate_n(numero_usuario)
print(f"o resultado é: {resultado}")