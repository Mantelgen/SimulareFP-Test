class furniture:

    def __init__(self,cod,tip,nume,stoc,pret):
        '''
        initializarea unui obiect de tip furniture
        :param id: id-ul unic al obiectului
        :param cod: codul obiectului
        :param tip: tipul mobilierului
        :param nume: numele mobilierului
        :param stoc: stocul disponibil
        :param pret: pretul unui obiect
        '''
        self.__code = cod
        self.__type = tip
        self.__name = nume
        self.__stock = stoc
        self.__price = pret

    def getCode(self):
        '''
        getter pentru codul unic
        :return:
        '''
        return self.__code

    def setCode(self,value):
        """
        setter pentru cod
        :param value: codul nou
        :return: noul cod setat
        """
        self.__code=value
        return self.__code

    def getType(self):
        '''
        getter pentru tip
        :return: tipul obiectului
        '''
        return self.__type

    def setType(self,value):
        '''
        setter pentru tip
        :param value: tipul nou
        :return: tipul nou al boiectului
        '''
        self.__type=value
        return self.__type

    def getName(self):
        '''
        getter pentru nume
        :return: numele obicetului
        '''
        return self.__name

    def setName(self,value):
        '''
        setter pentru nume
        :param value: noul nume al obiectului
        :return: noul nume setat
        '''
        self.__name=value
        return self.__name

    def getStock(self):
        '''
        getter pentru stoc
        :return: stocul de obiecte
        '''
        return self.__stock

    def setStock(self,value):
        '''
        setter pentru stock
        :param value: noua valoare pentru stoc
        :return: noua valoare setata pentru stock
        '''
        self.__stock=value
        return self.__stock

    def getPrice(self):
        '''
        getter pentru pret
        :return: pretul obiectului
        '''
        return self.__price

    def setPrice(self,value):
        '''
        setter pentru pret
        :param value: noul pret
        :return: noul pret setat
        '''
        self.__price=value
        return self.__price

    def __repr__(self):
        rep=str(self.getCode())+","+str(self.getType())+","+str(self.getName())+","+str(self.getStock())+","+str(self.getPrice())
        return rep

    def __eq__(self, other):
        value= self.__code==other.__code and self.__type==other.__type and self.__name==other.__name and  self.__stock==other.__stock
        value=value and self.__price==other.__price
        return value

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
masa=furniture("CI01","lemn","Masa de lemn de stejar",100,19.15)
print(masa)