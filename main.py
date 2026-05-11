from turtle import *

def mostra_palvra(palavra):
    for i in range(len(palavra)):
        print(i, palavra[:len(palavra) - i, palavra[:len(palavra - i)]])

mostra_palvra("ola, tudo bem?")
 

def mostra_palavra_rec(palavra):
    if palavra == "":
        return
    print("antes da chamada rec:", palavra)
    mostra_palavra_rec(palavra)
    print("depois da chamada rec:", palavra)
    return


def mostra_palavra_for(palavra):
    for i in range(len(palavra)):
        print(palavra[:len](palavra) - i)

 
   
    
    
    
mostra_palavra_for("ola, tudo bem?")    
mostra_palavra_rec("ola, tudo bem?")