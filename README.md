# RentSmart

# RentSmart — Sistema de Orçamento de Locação

Aplicação de terminal em **Python** que automatiza o cálculo de orçamentos de locação da imobiliária fictícia **R.M Imóveis**. O programa solicita as características do imóvel, aplica as regras comerciais, exibe um resumo detalhado do orçamento e gera um arquivo **CSV** com a projeção dos 12 primeiros meses de contrato.

Projeto desenvolvido para a disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming** (UniFECAF), aplicando pensamento algorítmico e fundamentos de Programação Orientada a Objetos.

## Funcionalidades

- Menus interativos no terminal, navegáveis com as setas do teclado.
- Três categorias de imóvel: apartamento, casa e estúdio.
- Cálculo automático de adicionais, desconto e taxa contratual.
- Validação das entradas (opções de menu, número de vagas e parcelas).
- Resumo detalhado do orçamento, com aluguel mensal e taxa contratual apresentados separadamente.
- Geração do arquivo `projecao_12_meses.csv` com a projeção dos 12 meses.
- Opção de realizar vários orçamentos na mesma execução.

## Regras de negócio

| Item | Regra | Valor |
|---|---|---|
| Aluguel-base | Apartamento de 1 quarto | R$ 700,00 |
| Aluguel-base | Casa de 1 quarto | R$ 900,00 |
| Aluguel-base | Estúdio | R$ 1.200,00 |
| Adicional de quartos | Apartamento com 2 quartos | + R$ 200,00 |
| Adicional de quartos | Casa com 2 quartos | + R$ 250,00 |
| Garagem | Casa ou apartamento (uma vaga) | + R$ 300,00 |
| Estacionamento do estúdio | Pacote inicial de 2 vagas | + R$ 250,00 |
| Estacionamento do estúdio | Cada vaga adicional | + R$ 60,00 |
| Desconto | Apartamento, cliente sem crianças | 5% sobre o aluguel, após os adicionais |
| Taxa contratual | Valor único, em até 5 parcelas | R$ 2.000,00 |

## Requisitos

- **Python 3.12 ou superior** (o código usa f-strings com aspas aninhadas).
- **Windows**: a leitura das setas do teclado usa o módulo `msvcrt` e a limpeza de tela usa o comando `cls`.
- Nenhuma biblioteca externa: apenas a biblioteca padrão do Python.

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
   ```

2. Execute o programa em um terminal (CMD ou PowerShell):

   ```bash
   python main.py
   ```

   > Execute em um terminal real. Em alguns editores (por exemplo, o console do IDLE), a leitura das setas do teclado não funciona.

## Como usar

1. Escolha o tipo de imóvel com **↑ / ↓** e confirme com **Enter**.
2. Responda às perguntas do imóvel escolhido:
   - **Apartamento:** dois quartos, vaga de garagem e se haverá crianças.
   - **Casa:** dois quartos e vaga de garagem.
   - **Estúdio:** total de vagas (0 se não desejar estacionamento, ou no mínimo 2).
3. Informe o número de parcelas da taxa contratual (de 1 a 5).
4. O resumo do orçamento é exibido na tela. Pressione **Enter** para continuar.
5. O arquivo `projecao_12_meses.csv` é gerado na pasta de execução.
6. Escolha se deseja realizar outro orçamento.

## Exemplo de saída

Apartamento de 2 quartos, com garagem, sem crianças, taxa em 3 parcelas:

```text
------------------------------------------------------------
                    Resumo do Orçamento                     
------------------------------------------------------------
Item / descrição                                  Valor (R$)
------------------------------------------------------------
Tipo de imóvel (Apartamento)                          700,00
Adicional 2 quartos                                   200,00
Vaga de garagem                                       300,00
------------------------------------------------------------
Subtotal                                            1.200,00
Desconto (5% sem crianças)                            -60,00
VALOR MENSAL                                        1.140,00
------------------------------------------------------------
             Taxa contratual (cobrada à parte)              
------------------------------------------------------------
Valor da taxa                                       2.000,00
Número de parcelas                                         3
Valor da parcela                                      666,67
------------------------------------------------------------
Total do 1º ano                                    15.680,00
------------------------------------------------------------
```

### Arquivo CSV gerado

O arquivo usa `;` como separador e vírgula como separador decimal, para abrir corretamente no Excel em português. A última parcela da taxa absorve a diferença de centavos do arredondamento, de modo que a soma seja sempre R$ 2.000,00.

```text
mes;aluguel;parcela_taxa_contratual;total_do_mes
1;1140,00;666,67;1806,67
2;1140,00;666,67;1806,67
3;1140,00;666,66;1806,66
4;1140,00;0,00;1140,00
...
12;1140,00;0,00;1140,00
```

## Estrutura do projeto

```text
.
├── main.py         # Fluxo principal: monta o imóvel, cria o orçamento e gera o CSV
├── obj.py          # Classes dos imóveis: Imovel, Apartamento, Casa e Estudio
├── orcamento.py    # Classe Orcamento: cálculos, resumo e exportação do CSV
├── menu.py         # Menus com setas e leitura validada das entradas
└── README.md
```

## Estrutura de classes

- **`Imovel`** (classe base): guarda as escolhas do cliente e monta a lista de itens do orçamento (`itens()`). Os valores comerciais são atributos de classe, sobrescritos por cada subclasse. O método `desc_crianca()` devolve 0 por padrão.
- **`Apartamento`**: valores do apartamento e sobrescrita de `desc_crianca()` com o desconto de 5% para clientes sem crianças.
- **`Casa`**: valores da casa; reaproveita os métodos da classe base.
- **`Estudio`**: sobrescreve `itens()` por ter uma regra própria de estacionamento (pacote de duas vagas e vagas extras).
- **`Orcamento`**: recebe um imóvel, calcula subtotal, desconto, aluguel mensal e parcelas da taxa, imprime o resumo e gera a projeção de 12 meses.

O polimorfismo permite que `Orcamento` use `imovel.itens()` e `imovel.desc_crianca()` sem verificar o tipo do imóvel. Para incluir uma nova categoria, basta criar uma nova subclasse de `Imovel`.

## Decisões e suposições

O enunciado deixa alguns pontos em aberto. As decisões adotadas foram:

- **Estúdio:** o cliente pode não querer estacionamento (0 vagas) ou contratar 2 ou mais vagas. A partir de 2 vagas, cobra-se o pacote de R$ 250,00 mais R$ 60,00 por vaga adicional.
- **Desconto de 5%:** calculado sobre o subtotal (aluguel-base, adicional de quartos e garagem) e aplicado somente a apartamentos de clientes sem crianças.
- **Taxa contratual na projeção:** as parcelas aparecem nos primeiros meses do CSV, conforme o número de parcelas escolhido, e valem zero nos demais.
- **Total do primeiro ano:** 12 aluguéis mensais mais a taxa contratual.

## Autor

Brayant Alexander Maita Martinez — 177281
UniFECAF
