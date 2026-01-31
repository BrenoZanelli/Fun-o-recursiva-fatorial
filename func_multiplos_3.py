
#função para validar se a entrada inicial é verdadeira
def validar_numeros():
       while True:
           try:
               numeros=int(input("Digite a quantidade de números que você deseja adicionar à lista: "))
               return numeros
           except ValueError:
               print("Você digitou um valor invalido, por favor digite apenas numeros inteiros (ex: 1, 2, 3....): ")

numeros_validos=validar_numeros()

#função da operação inteira
def func(numeros_validos):

    #lista primaria para guardar os primeiros numeros inseridos pelo usuário
    lista=[]

    #lista para guardar os multiplos
    resultado=[]

    #variavel para decisão de qual multiplo será usado
    qual_multiplo=int(input("Digite o multiplo que você deseja usar: "))


    #laço for para adicionar os numeros na primeira lista
    for i in range(numeros_validos):

        question=int(input("Digite o numero que deseja adicionar:"))

        lista.append(question)

    #laço for para achar os multiplos e guarda-los
    for i in range(numeros_validos):
      
      if lista[i]%qual_multiplo==0:
         
         resultado.append(lista[i])

    return resultado

#variavel para salvar o resultado da função
mostrar=func(numeros_validos)
print(f"Sua lista final é: {mostrar}")
