import sqlite3

def criaTabela():
    pass

def cadastrar(val):
    pass

def editar(val):
    pass

def main():
    if input("criar ...").upper()== 'Y':
        criaTabela()
    else:
        print("asdf")

    switcher = {
        'A': cadastrar,
        'B': editar
    }

    while True:
        print("a,b,c...")
        opcao = input("vai").upper()
        switcher.get(opcao,lambda:print("opcao invalida"))()