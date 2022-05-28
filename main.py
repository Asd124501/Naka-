# importanto o driver de conexão com o mysql
import mysql.connector
# fazendo a conexão com bando de dados
# o objeto 'con' mantém um sessão aberta para acesso ao banco de dados
con = mysql.connector.connect(host='localhost',database='LIVRARIA',user='root',password='')
# podemos testar se a conexão está ativa
# o objeto cursor permite executar comandos sql, como se estivesse sendo executado no console
cursor = con.cursor()
cursor.execute("select database();")
linha = cursor.fetchone() # obtém o banco ao qual se está conectado
print("Conectado ao banco de dados ",linha)
# executando o comando para criar uma tabela no banco conectado
cursor.execute("CREATE TABLE Livros (codigo INT PRIMARY KEY, nome CHAR(40),autor CHAR(40), Editora CHAR(40), Ano INT, preco FLOAT)")