#modulo para fazer contas

def media(lista):
    soma= 0
    for x in lista: 
        soma+=x
    resultado=soma/len(lista)
    return resultado

def maior(lista):
    maior=lista[0] #colocamos um elemento qualquer da lista como parametro, se for maior que ele (nesse caso)
    #substituimos a variavel maior 
    for x in lista:
        if x>maior:
            maior=x
    return maior

if __name__ == "__main__": #impedir que prints soltos no modulo sejam executados (para teste serem apenas no proprio arquivo)
    print(media([1,2,3,4,5])) #aqui se coloca os prints pra testa c a execução do programa ta ok
    
#exercicio 
def doarSangue(sexo,peso):
    if sexo=="feminino":
        if peso>=50:
            return True
        else: 
            return False
    if sexo=="masculino":
        if peso>=60:
            return True
        else:
            return False

#charles
def DoarSangue(sexo,peso):
    if (sexo=="feminino" and peso>=50) or (sexo=="masculino" and peso>=60):
        return True
    else:
        return False
    
#exercicio

from ex1_calculo import doarSangue

print(doarSangue("feminino",55))
print(doarSangue("feminino",49))
print(doarSangue("masculino",60))
print(doarSangue("masculino",59))

#charles

from ex1_calculo import DoarSangue

sexo=input("Digite seu sexo: ")
peso=int(input("Digite seu peso: "))

if DoarSangue(sexo,peso)==True:
    print("Esta apto a doar sangue")
else:
    print("Não está apto a doar sangue")
    
#exercicio

import math

def hip(cat1,cat2):
    hipo=math.sqrt(cat1**2+cat2**2)
    return hipo

#exercicio

from ex2_calculo import hip

print(hip(3,4))

#exercicio

def tamanho(senha):
    if len(senha)>=8:
        return True
    else:
        return False

def maiuscula(senha):
    for x in senha:
        if x.isupper() == True:
            return True
    return False


def minuscula(senha):
    for x in senha:
        if x.islower() == True:
            return True
    return False


def numero(senha):
    for x in senha:
        if x.isdigit() == True:
            return True
    return False

def tamanho(senha):
    if len(senha)>=8:
        return True
    else:
        return False

def maiusculo(senha):
    for x in senha:
        if x :
            return True
            break
def minusculo(senha):
    for x in senha:
        if x :
            return True
            break
def detectaNumero(senha):
    for x in range(len(senha)): #pega o indice 
        if senha[x].isdigit() == True:
            return True
            break
    return False
   
def validaSenha ():
    return 0
  
#exercicio

from calculo import media,maior

numeros = [1,2,3,4,5,6,7,8,9,10]
n1=[23,5,66,23,1]
print('MÉDIA: ',media(n1))
print('MAIOR: ',maior(n1))  