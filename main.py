#-----------------------------------------------------------------------
#Trabalhando com Biblioteca
print
import math
print( math.factorial(6))





#--------------------------------------------------------------------
#Trabalhando com Dicionarios
classe = {"Murilo": 4.5,
          "bruna": 6.5,
          "gabi": 10.0,
          "daniel": 9.5}
notas = classe.values()
média = sum(notas)/5
print("A média da classe é",média)
print("\n")

dic = {"salgado": 4.50,"lanche": 6.50,"suco": 3.00,"refrigerante": 3.50,
      "doce": 1.00}
print(dic)
print("\n")


D = {"arroz": 17.30,"feijão": 12.50,"carne": 23.90,"alface": 3.40}
print(D)

D["carne"] = 25.0
D["tomate"] = 8.80
print(D)


#--------------------------------------------------------
#Trabalhando com Tuplas
T = (10,20,30,40,50)
a,b,c,d,e = T
print("a =",a,"b =",b)
print("d + e =",d+e)

#--------------------------------------------------------
#Praticando com Listas
L = [5, 7, 2, 9, 4, 1, 3]
print("lista = ", L)
print("O tamanho da lista é ",len(L))
print("O maior elemento da lista é ",max(L))
print("O menor elemento da lista é",min(L))
print(" a soma dos elementos da lista é ",sum(L))
L.sort()
print("lista em ordem crescente : ",L)
L.reverse()
print("lista em ordem decrescente: ", L)


