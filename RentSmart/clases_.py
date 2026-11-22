'''
categorias de imóveis.

neste ocumento .py teremos varias clases necesarias para o funcionamento do programa

lista de clases e descripçao breve

    nome    -    descriopçao
 Inmovel        clase pai que tem os parametros bases e os metodos comuns que teran as clases filhas 
 Apartamento    clase filha que contem os atributos necesarios para o imovel de tipo apartamento
 Casa           clase filha que contem os atributos necesarios para o imovel de tipo casa
 Estudio        clase filha que contem os atributos e metodos necesarios para o imovel de tipo estudio

O apartamento de um quarto possui aluguel-base de R$ 700,00, a casa de um quarto possui
aluguel-base de R$ 900,00 e o estúdio possui aluguel-base de R$ 1.200,00
'''

class Imovel: #clase pai para os tipos de imovel a selecionar
    valor_base = 0.0
    extra_dois_qrtos = 0.0
    valor_vaga_garagem = 300.00

    def __init__(self, nome, dois_qrtos = False, vagas_garagem = False):
        self.nome = nome
        self.dois_qrtos   = dois_qrtos
        self.vagas_garagem = vagas_garagem

    def itens(self):
        lista = [(f"Tipo de imovel ({self.nome})", self.valor_base)]

        if self.dois_qrtos:
            lista.append(("Adicional 2 quartos", self.extra_dois_qrtos))
        if self.vagas_garagem:
            lista.append(("Vaga de garagem", self.valor_vaga_garagem))
        
        return lista

    def desc_crianca(self, sub_total, tem_criaca): #metodo especifico para calcular o desconto aplicavel se nao tem criaças
            return sub_total * 0.05 if not tem_criaca else 0.0

class Apartamento(Imovel): #objeto utilizado para especificar os atributos necesarios para as operaçoes de sua calse pai e tem um metodo especifico para ele mesmo

    #Atributos de clase
    valor_base = 700.00 #(valor especificado pelo cliente)
    extra_dois_qrtos = 200.00 #(valor especificado pelo cliente e so aplica se o usuario pedir dois quartos)

    def desc_crianca(self, sub_total, tem_criaca): #metodo especifico para calcular o desconto aplicavel se nao tem criaças
        return sub_total * 0.05 if not tem_criaca else 0.0


class Casa(Imovel): #objeto utilizado para especificar os atributos necesarios para as operaçoes de sua calse pai
    #Atributos de clase
    valor_base = 900.00 #(valor especificado pelo cliente)
    extra_dois_qrtos = 250.00 #(valor especificado pelo cliente e so aplica se o usuario pedir dois quartos)



class Estudio(Imovel):
    #----- (valor especificado pelo cliente) ----
    valor_base = 1200.00 
    pacotes_duas_vagas = 250.00
    vaga_extra = 60.00
    #---------------------------------------------
    nome = "Estudio"
    vagas_incluidas = 2 #atributo usado para calcular as vagas extras se tem 

    def __init__(self, total_vagas=0):
        self.total_vagas = total_vagas

    def itens(self): #debido a diferenças com as outras duas clases temos um metodo especifico para esta clase
        lista = [(f"Aluguel-base ({self.nome})", self.valor_base)] #iniciamos uma lista com os dados correspondentes a esta clase

        if self.total_vagas >= 2: #se o total de vagas de garagem é maior que 0 agrga o pacote (o cliente so epecifica que tera 2 no minimo)
            lista.append(("Pacote de 2 vagas", self.pacotes_duas_vagas))

        extras = self.total_vagas - self.vagas_incluidas #extras = vagas de garagems totais menos 2 (vagas incluidas)
        
        if extras > 0:
            lista.append((f"{extras} vaga(s) adicional(is) x R$ {self.vaga_extra:.2f}",extras * self.vaga_extra))
        
        return lista


#obj = Apartamento ou casa (primer parametro = tem ou nao dois quartos, segundo parametro = tem ou nao vagas de garagem? ) <---- exemplo de instanciar um objeto tipo apartamento ou casa
'''obj = Apartamento(True,False)

sub_total = sum(valor for _,valor in obj.itens())

print(f"sub_total: {sub_total}")

desconto = obj.desc_crianca(900.00,False)
print(f"desconto : {desconto}")'''