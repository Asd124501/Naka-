class Livros:
    '''
    codigo=0
    descricao=''
    preco=0.0
    qtde=0
    '''
    def __init__(self, codigo,nome,autor,editora,ano,preco):
        self.codigo=codigo
        self.nome=nome
        self.autor=autor
        self.editora=editora
        self.ano=ano
        self.preco=preco
    def getCodigo(self):
        return self.codigo
    def getNome(self):
        return self.nome
    def getAutor(self):
        return self.autor
    def getEditora(self):
        return self.editora
    def getAno(self):
        return self.ano
    def getPreco(self):
        return self.preco