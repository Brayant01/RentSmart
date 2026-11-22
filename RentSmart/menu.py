import os
import msvcrt
import time

tipo_inmovel = [
    "inmovel tipo 1 : Apartamento.",
    "inmovel tipo 2 : Casa.",
    "inmovel tipo 3 : estudio."
]

sim_nao = ["SIM","NÃO"]

def ler_tecla():
        ch = msvcrt.getwch()
        
        if ch in ("\x00", "\xe0"):       # prefijo das teclas especiais 
            codigo = msvcrt.getwch()
            return {"H": "CIMA", "P": "BAIXO",
                    "K": "ESQUERDA", "M": "DIREITA"}.get(codigo)
        if ch == "\r":
            return "ENTER"
        else:
            pass
        

def menu_vertical(titulo, opcoes):
    indice = 0

    while True:
        if titulo == "Selecciona um tipo de imovel":
            print(f"-"*60)
            print(f"{"Bem-vido a RentSmart":^60}")
            print(f"-"*60)
            
        print(f"{titulo}\n")
        
        for i, opcao in enumerate(opcoes):
            marcador = ">" if i == indice else " "
            print(f"  {marcador} {opcao}")
        
        print("\n↑/↓ navegar  |  Enter confirmar")

        tecla = ler_tecla()

        if tecla == "CIMA":
            indice = (indice - 1) % len(opcoes)
        elif tecla == "BAIXO":
            indice = (indice + 1) % len(opcoes)
        elif tecla == "ENTER":
            os.system("cls")
            return indice + 1
        
        os.system("cls")

def opcoes_imovel_residencial(tipo): #(tipo) = "apartamento", "casa", "estudio"
    dois_quartos = False
    vaga_garagem = False

    if menu_vertical("Voce deseja ter dois quartos? :",sim_nao) == 1:
            dois_quartos = True

    if menu_vertical("Deseja ter uma vaga de garagem? :",sim_nao) == 1:
            vaga_garagem = True

    if tipo.lower() == "apartamento":
        if menu_vertical("Voce tera criaças no imovel? :",sim_nao) == 1:
            tem_crianca = True
        else: 
            tem_crianca = False

        return dois_quartos,vaga_garagem,tem_crianca

    return dois_quartos, vaga_garagem

def opcoes_estudio():

    if menu_vertical("Deseja ter acceso a vagas de garagem? ",sim_nao)== 1:
            
        print("ingrese a quantidade de vagas de garagems que deseja") 
            
        valor = int(input("Min 2 : "))

        if valor >= 2:
            return valor
        else:
            print("Valor invalido, 'ENTER' para continuar")
            input()
    else:
        return 0


def selecionar_parcelas():
    while True: 

        try:
            parcelas = int(input("\nSelecionar la cantidad de parcelas\n Numero maximo 5 : "))

            if parcelas > 0 and parcelas <= 5:
                return parcelas
            else:   
                input("quantidade invalida, ingresar um valor correto\n precione qualque tecla para continuar....")
        except:
            os.system("cls")
            input(("!Por favor só ingresar numeros\npresionar qualquer tecla para continuar...."))

def tela_espera(mgs):
    print(mgs)
    time.sleep(1)


