import mysql.connector

from Livros import Livros

class LivrosDAO:
#    con=None
#   cursor=None
    def __init__(self):
        self.con=None
        self.cursor=None
    def conectar(self):
        self.con=mysql.connector.connect(host='localhost',
                    database='Livraria',user='root',password='')
        if not self.con.is_connected():
            return False
        self.cursor=self.con.cursor()
        return True

    def desconectar(self):
        if self.con.is_connected():
            self.con.close()

    def cadastrar(self, Livros):
        sql='insert into Livros values (%s,%s,%s,%s)'
        valores=(Livros.getCodigo(), Livros.getNome(),
                 Livros.getAutor(), Livros.getEditora(), Livros.getAno(), Livros.getPreco())
        if not self.conectar():
            return False
        self.cursor.execute(sql,valores)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        return False

    def consultar(self, codigo):
        sql='select * from Livros where codigo='+str(codigo)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        for (codigo,nome, autor, editora,ano , preco) in self.cursor:
            return Livros(codigo,nome,autor,editora,ano,preco)
        return None

    def atualizar(self,l):
        sql='update Livros set preco=%s,where codigo=%s'
        valores=(l.getPreco(),l.getCodigo())
        if not self.conectar():
            return False
        self.cursor.execute(sql,valores)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        return False

    def excluir(self, codigo):
        sql='delete from Livros where codigo='+str(codigo)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        return False
'''
pd=ProdutoDAO()
produto=pd.consultar(101)
print('Produto: ', produto.getDescricao())
'''