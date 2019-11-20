import textwrap

class Bem:

    def __init__(self, codTipoBem, descTipoBem, descDetalhadaBem, valorBem):
        self.__codTipoBem = codTipoBem
        self.__descTipoBem = descTipoBem
        self.__descDetalhadaBem = descDetalhadaBem
        self.__valorBem = valorBem


    def __str__(self):
        formatado = f'''{self.getCodigoDoTipoDeBem()} --- {self.getDescricaoDoTipoDeBem()} --- R${self.getValorDoBem()}
Descrição: {textwrap.shorten(self.getDescricaoDetalhadaDoBem(), width=80)}'''
        return formatado


    def __repr__(self):
        pass
    
    def comparaBens(listaBens):
        pass

    def setCodigoDoTipoDeBem(novo):
        self.__ = novo
    def setDescricaoDoTipoDeBem(novo):
        self.__ = novo
    def setDescricaoDetalhadaDoBem(novo):
        self.__ = novo
    def setValorDoBem(novo):
        self.__ = novo

    def getCodigoDoTipoDeBem(self): return self.__codTipoBem
    def getDescricaoDoTipoDeBem(self): return self.__descTipoBem
    def getDescricaoDetalhadaDoBem(self): return self.__descDetalhadaBem
    def getValorDoBem(self): return self.__valorBem
