import os
import menu
import clases_
import orcamento


def montar_inmovel():
    tipo_inmovel = menu.menu_vertical("Selecciona um tipo de imovel", menu.tipo_inmovel)
    tem_crianca = True

    if tipo_inmovel == 1:
        dois_quartos, vaga_garagem, tem_crianca = menu.opcoes_imovel_residencial("Apartamento")
        imovel = clases_.Apartamento("Apartamento",dois_quartos,vaga_garagem) #clases_ = Apartamento(tem ou nao 2 quartos, tem ou nao vagas de garagem? ) <---- exemplo de intanciar um objeto 
    
    if tipo_inmovel == 2:
        dois_quartos, vaga_garagem = menu.opcoes_imovel_residencial("Casa")
        imovel = clases_.Casa("Casa",dois_quartos,vaga_garagem)    #clases_ = Apartamento(tem ou nao 2 quartos, tem ou nao vagas de garagem? ) <---- exemplo de intanciar um objeto 

    if tipo_inmovel == 3:
                
        vaga_garagem = menu.opcoes_estudio()
        imovel = clases_.Estudio(vaga_garagem)   #clases_ = Apartamento(quantas vagas tem, ou nao tem? ) <---- exemplo de intanciar um objeto 
            
    parcelas = menu.selecionar_parcelas()
    orcamento_aux = orcamento.Orcamento(imovel, parcelas, tem_crianca)
    
    return orcamento_aux

def main():

    while True:
        os.system("cls")

        orcamento_aux = montar_inmovel()
        orcamento_aux.imprimir_orcamento()
        
        input()
        os.system("cls")
        
        orcamento_aux.orcamento_csv()
        
        if menu.menu_vertical("Deseja realizar outro orçamento? ",menu.sim_nao)==2:
            print("Obrigado por usar nosso sistema, ate a proxima")
            break


if __name__ == "__main__":
    main()


    

