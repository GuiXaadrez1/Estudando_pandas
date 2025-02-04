import pandas as pd

# Descomente o que for necessário
'''
    LEIA A ANOTAÇÃO A_importância_do_type().txt
    LEIA A ANOTAÇÃO LOC_VS_ILOC.txt
    LEIA A ANOTAÇÃO Manipulando_Colunas_DataFrame.txt
    LEIA A ANOTAÇÃO Usando_e_entendendo_Vetores_Lógicos.txt
    LEIA A ANOTAÇÃO Funções_de_Agregação e Agrupamento.txt

    Em Códigos_exemplos VEJA! Operadores_Votores_lógicos 1 e o 2
'''

'''
Essa parte três visa explicar melhor o selecionamento de colunas com DataFrame
também visa explicar a manipulação de colunas.
'''

# Criando um DataFrame com dicionários a partir de séries

s1 = pd.Series([1, 2, 3, 4, 5], name='c1')
s2 = pd.Series([10, 20, 30, 40, 50], name='c2')

df = pd.DataFrame({s1.name: s1, s2.name: s2})

#print(df)

# Selecionando colunas do DataFrame

# Selecionando colunas com listas ou formas com nomes das colunas

#print(df['c1'])

# Com listas de colunas para selecionar múltiplas colunas
#print(df[['c1', 'c2']])

'''
Podemos obter o mesmo resultado acima através de uma variável que armazena
uma lista de colunas e passar isso como um parâmetro do DataFrame.

lista_colunas = ['c1', 'c2']
print(df[lista_colunas])
'''

# Visualizando o tipo de dados do nosso DataFrame
'''
print(type(df['c1'])) # saída -> <class 'pandas.core.series.Series'>

print(type(df[['c1', 'c2']])) # saída -> <class 'pandas.core.frame.DataFrame'>

Isso é importante para entendermos operações exclusivas de DataFrames e Series.

print(df['c1'][0:3])

SAÍDA:

índice    c1
0          1
1          2
2          3

print(type(df['c1'][0:3])) # saída -> <class 'pandas.core.series.Series'>

Veja! Aqui ele saiu como um Series quando fizemos um slice selecionando um intervalo
de índices para uma coluna do DataFrame.

print(df['c1'][0])

SAÍDA:

índice    c1
0          1

print(type(df['c1'][0])) # saída -> <class 'numpy.int64'>

Veja! Aqui ele saiu como um vetor do NumPy quando fazemos o slice de uma linha
para uma coluna do DataFrame.
'''

# Adicionando colunas através de um valor constante ou escalar

'''
Você vai entender melhor sobre isso no código de exemplo:

Series3_operações_matemáticas
'''

#df['Multiplicação'] = df['c1'] * 10
#print(df)

'''
Tem como fazer operações escalares com strings também.
'''

#df['c3'] = 'Coluna_String'
#print(df)

'''
SAÍDA:

   c1  c2             c3
0   1  10  Coluna_String
1   2  20  Coluna_String
2   3  30  Coluna_String
3   4  40  Coluna_String
4   5  50  Coluna_String
'''

# Adicionando colunas através de operações matemáticas com outras colunas

'''
df['Soma'] = df['c1'] + df['c2']
print(df)
'''

# Podemos fazer operações escalares com as funções de agregação do Pandas também

#df['Média_c1'] = df['c1'].mean()
#print(df)

'''
Leia a anotação sobre Funções_de_Agregação.

Funções de agregação:

.min() -> menor valor
.max() -> maior valor
.sum() -> soma total de todos os valores da coluna
.mean() -> média aritmética da coluna
.count() -> conta a quantidade de dados daquela coluna
.agg([lista_funções_agregação]) -> permite múltiplas funções de agregação
'''

# Exemplo de uso com a função de agregação 

#resultados = df[['c1']].agg(['max', 'sum', 'mean'])
#print(resultados)
#print(type(resultados))

'''
O resultado é um pouco diferente, confira:

SAÍDA:
        c1
max    5.0
sum   15.0
mean   3.0
<class 'pandas.core.frame.DataFrame'>

O índice ser composto pelas funções no resultado da agregação é um comportamento 
padrão do Pandas para fornecer uma visão tabular e descritiva das operações 
realizadas. 

Resumindo: .agg() retorna um DataFrame, onde as funções são organizadas como índice.
'''

# Usando .insert() para adcionar colunas no dataframe

'''
Basicamente o insert funciona da seguinte forma: adicionar colunas em posições 
específicas.

Veja! 

DataFrame.insert(loc, column, value, allow_duplicates=False)

loc (int) -> A posição (índice) onde a nova coluna será inserida.

column (str) -> O nome da nova coluna a ser inserida.

value -> Os valores da nova coluna. Pode ser:

Um valor escalar (exemplo: 10, que será replicado em todas as linhas).

Uma lista, NumPy array, ou uma pd.Series com o mesmo número de elementos que o 
DataFrame.

allow_duplicates (bool, padrão: False) -> Permite duplicação de coluna

Se False, levanta um erro se o nome da coluna já existir no DataFrame.
Se True, permite a inserção de uma coluna com nome duplicado.


CUIDADO COM INSERT -> ELE PODE ALTERAR OS VALORES DE UM DATAFRAME
'''

#df.insert(3,"c4",10)
#print(f'\nUsando insert para inserir a colna c4:\n{df}')


# Remoção de colunas com del e pop

'''
O del apaga/remove a coluna do nosso DataFrame, básicamente é isso
'''

#del df['Média_c1']
#print(f'\n{df}')

'''
Outra forma de remoção de tabelas é com pop

DataFrame.pop(item)

item (str) -> Nome da coluna que você deseja remover do DataFrame.

'''

#df.pop('c2')
#print(f'\n{df}')

