import csv
import os

class Orcamento:
    MESES = 12

    def __init__(self, imovel, parcelas = 1, tem_crianca = False):
        self.imovel = imovel
        self.parcelas = parcelas
        self.tem_crianca = tem_crianca

        self.itens = imovel.itens()
        self.sub_total = sum(valor for _, valor in self.itens)
        self.desconto  = imovel.desc_crianca(self.sub_total,self.tem_crianca)
        self.valor_mensal = round(self.sub_total - self.desconto,2)
        self.taxa = 2000.00
        
        self.itens.append(("Sub-total",round(self.sub_total,2)))
        self.itens.append(("Desconto",round(self.desconto,2)))
        self.itens.append(("Valor mensal",round(self.valor_mensal,2)))
        
        self.itens.append(("Taxa contractual:",round(self.taxa,2)))
        self.itens.append(("Valor de parcela",round(self.taxa / self.parcelas,2)))
        self.itens.append(("Numero de parcelas", self.parcelas))
        self.itens.append(("Total 1ro ano:",round(self.valor_mensal * 12 + self.taxa ,2)))

    def imprimir_orcamento(self):
        os.system("cls")
        line = f"-"*60
        moeda = f"R$"

        print(line)
        print(f"{"Resumen de Orçamento":^60}")
        print(line)

        print(f"{"Iten/Descripçao":<{40}}{"Valor "+moeda:>{20}}")
        print(line)

        for i in self.itens:
        
            if i[0] == "Valor mensal": print(line)
            print(f"{i[0]:<{40}}{i[1]:>{20}}")
            if i[0] == "Valor mensal": print(line)

            if i[0] == "Numero de parcelas": print(line)

        print(line)

    def parcelas_da_taxa(self):
        valor = round(self.taxa/self.parcelas, 2)
        lista = [valor]*self.parcelas

        lista[-1]= round(self.taxa - valor * (self.parcelas - 1), 2)
        
        return lista


    def projecao_12meses(self):
        taxas = self.parcelas_da_taxa()
        linhas = []

        for mes in range(1,self.MESES +1):
            taxa = taxas[mes - 1] if mes <= self.parcelas else 0.0
            total_mes = round(self.valor_mensal + taxa, 2)
            linhas.append([mes, round(self.valor_mensal, 2), taxa, total_mes])

        return linhas


    def orcamento_csv(self, caminho="projecao_12_meses.csv"):
        
        cabecalho = ["mes", "aluguel", "parcela_taxa_contratual",
                     "total_do_mes"]
        try:
            with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
                escritor = csv.writer(arquivo, delimiter=";")
                escritor.writerow(cabecalho)
                for linha in self.projecao_12meses():
                    escritor.writerow([f"{v:.2f}".replace(".", ",") if i else v for i, v in enumerate(linha)])

        except OSError as erro:
            print(f"Não foi possível gerar o CSV: {erro}")
            return None
        return caminho





                
            



