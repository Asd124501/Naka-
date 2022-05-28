from Livros import Livros
from LivrosDao import LivrosDAO


class LivrosControle:

    def __init__(self):
        self.lDAO=LivrosDAO()
        self.livros=None

#   def cadastrar(self, codigo, descricao, preco, qtde):
#        prod=Produto(int(codigo), descricao, float(preco), int(qtde))
#       return self.pDAO.cadastrar(prod)

    def cadastrar(self, codigo,nome,autor,editora,ano,preco):
        liv=Livros(codigo,nome,autor,editora,ano,preco)
        return self.lDAO.cadastrar(liv)

    def atualizar(self, codigo,nome,autor,editora,ano,preco):
        if not self.livros.getCodigo()==int(codigo):
           return False
        self.produto.setPreco(float(preco))
        return self.lDAO.atualizar(self.livros)

    def consultar(self, codigo):
        self.livros=self.lDAO.consultar(codigo)

        if self.livros!=None:
            dados=[str(self.livros.getCodigo()), self.livros.getNome(), str(self.livros.getAutor()), str(self.livros.getEditora()), str(self.livros.getAno()), str(self.livros.getPreco())]
            return dados
        return None

    def excluir(self, codigo):
        if not self.livros.getCodigo()==int(codigo):
           return False
        return self.lDAO.excluir(int(codigo))


