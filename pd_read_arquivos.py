import pandas as pd

# ler arquivo csv
#df = pd.read_csv(r"C:\Estudando_pandas\Arquivos_csv_estudos\202401_Compras.csv",encoding='latin1',sep = ";", header=0, nrows=10, usecols=["Número do Contrato","Objeto","Fundamento Legal"])

# ler arquivos excel
#df = pd.read_excel(r"C:\Estudando_pandas\Arquivos_excel_para_estudos\Relatorio DER Novembro2024.xlsx", sheet_name= 0)

#arquivo_excel = pd.ExcelFile(r"C:\Estudando_pandas\Arquivos_excel_para_estudos\Relatorio DER Novembro2024.xlsx")

#print(arquivo_excel.sheet_names)

#ABA1 = arquivo_excel.parse("Multas-Novembro")
#ABA2 = arquivo_excel.parse("Protocolo-Novembro")

#print(ABA1, ABA2)

# ler arquivos json,
#df = pd.read_json("/caminho/arquivo.json")

# com sqlalquemy podemos ler arquivos sql com pandas

'''
import pandas as pd from sqlalchemy import create_engine

# Criar a engine de conexão 
engine = create_engine('mysql+pymysql://usuario:senha@host:porta/nome_do_banco') 

# Consulta SQL 
query = "SELECT * FROM sua_tabela" 

# Ler dados do SQL para o DataFrame
df_sql = pd.read_sql(query, engine) # Exibir o DataFrame
'''
#print(df.info())
#print(df)