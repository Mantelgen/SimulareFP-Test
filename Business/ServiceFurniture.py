from Validation.validation import *
from Infrastructure.repoFurniture import *

class ServiceFurniture:

    def __init__(self,validator,repoFurniture):
        self.__validator=validator
        self.__repo=repoFurniture

    def createFurniture(self,code,type,name,stock,price):
        Furniture=furniture(code,type,name,stock,price)
        self.__validator.validation(Furniture)
        return Furniture

    def saveFurniture(self,code,type,name,stock,price):
        Furniture=self.createFurniture(code,type,name,stock,price)
        self.__repo.save(Furniture)

    def deleteFurniture(self,idDelete):
        self.__repo.delete(idDelete)
    def modifyFurniture(self,idModify,code,type,name,stock,price):
        Furniture = self.createFurniture(code, type, name, stock, price)
        self.__repo.modify(idModify,Furniture)

    def showFurniture(self):
        return self.__repo.getAllObjects()

    def searchFurnitureType(self,type):
        furnitures=self.__repo.searchByType(type)
        for i in furnitures:
            print(i)
    def buyFurniture(self,code,numberPieces):
        for i in self.__repo.getAllObjects():
            if i.getCode()==code:
                name=i.getName()
                price=numberPieces*i.getPrice()
                newPieces=i.getStock()-numberPieces
                self.modifyFurniture(code,i.getCode(),i.getType(),i.getName(),newPieces,i.getPrice())
        return name,price,newPieces