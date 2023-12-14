from Exceptions.exceptions import *
from Domain.mobilier import *
class repoFurniture:

    def __init__(self):
        self._objects=[]

    def save(self,furniture):
        for i in self._objects:
            if i.getCode()==furniture.getCode():
                raise RepoError("Obiectul exista deja in lista")
        self._objects.append(furniture)

    def delete(self,idObject):
        ok=False
        for i in self._objects:
            if i.getCode()==idObject:
                ok=True
                self._objects.remove(i)
        if not ok:
            raise RepoError("Obiectul nu exista in lista! ")


    def modify(self,idModify,newObject):
        ok=False
        for i in range(0,len(self._objects)):
            if self._objects[i].getCode() == idModify:
                self._objects[i]=newObject
                ok=True
        if not ok:
            raise RepoError("Obiectul nu exista in lista! ")
    def searchByType(self,type):
        typeList=[]
        for i in self._objects:
            if i.getType()==type and i.getStock()>0:
                typeList.append(i)
        if typeList!=[]:
            return typeList
        raise RepoError("Nu exista obiecte cu tipul specificat! ")
    def getAllObjects(self):
        return self._objects

class FileRepo(repoFurniture):

    def __init__(self,file_path):
        self.__filePath=file_path
        repoFurniture.__init__(self)

    def __readAllFromFile(self):
        with open(self.__filePath,"r") as f:
            self._objects.clear()
            lines=f.readlines()
            for line in lines:
                line.strip()
                if line != "":
                    parts = line.split(",")
                    cod=parts[0]
                    tip=parts[1]
                    name=parts[2]
                    stoc=int(parts[3])
                    pret=float(parts[4])
                    self._objects.append(furniture(cod,tip,name,stoc,pret))

    def __writeAllToFile(self):
        '''
        scrierea in fisier
        :return:
        '''
        with open(self.__filePath, "w") as f:
            for problem in self._objects:
                f.write(str(problem)+"\n")

    def save(self,furniture):
        '''
        salvarea in fisier
        :param problem:
        :return:
        '''
        self.__readAllFromFile()
        repoFurniture.save(self, furniture)
        self.__writeAllToFile()

    def delete(self,idObject):
        '''
        stergerea din fisier
        :param id:
        :return:
        '''
        self.__readAllFromFile()
        repoFurniture.delete(self, idObject)
        self.__writeAllToFile()

    def modify(self,idModify,newObject):
        '''
        modificarea in fisier
        :param idModify:
        :param newObject:
        :return:
        '''
        self.__readAllFromFile()
        repoFurniture.modify(self, idModify, newObject)
        self.__writeAllToFile()

    def searchByType(self,type):
        '''
        cautarea in fisier dupa tip
        :param type:
        :return:
        '''
        self.__readAllFromFile()
        return repoFurniture.searchByType(self, type)

    def getAllObjects(self):
        '''
        getter pentru toate obiectele
        :return:
        '''
        self.__readAllFromFile()
        return repoFurniture.getAllObjects(self)
