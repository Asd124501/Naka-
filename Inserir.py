import mysql.connector
con = mysql.connector.connect(host='localhost',database='LIVRARIA',user='root',password='')
cursor=con.cursor()

# inserindo vários registros
sql = "INSERT INTO livros (codigo, nome,autor ,editora,ano, preco) VALUES (%s,%s,%s,%s,%s,%s)"
values = [(103, "O homem mais esperto do facebook","Abdou Sait","Nova", 2015, 40.0) ]
cursor.executemany(sql, values)
con.commit()

print(cursor.rowcount, "registro(s) inserido(s)")
con.commit()