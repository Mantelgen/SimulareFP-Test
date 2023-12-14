from Business.ServiceFurniture import *

class UI:

    def __init__(self,service):
        self.__service=service
        self.__comenzi={"add_furniture":self.uiAddFurniture,"show_furniture":self.uiGetAll,
                        "delete_furniture":self.uiDeleteFurniture,"buy":self.uiBuy}

    def uiAddFurniture(self,params):
        if len(params)>5:
            print("Parametrii invalizi! ")
        else:
            cod = params[0]
            tip = params[1]
            name = params[2]
            errors = ""
            if not params[3].isdigit():
                errors += "Stoc invalid. "
            if not is_float(params[4]):
                errors+="Pret invalid. "
            if len(errors) > 0:
                raise ValueError(errors)
            else:
                stock = int(params[3])
                pret=float(params[4])
                self.__service.saveFurniture(cod,tip,name,stock,pret)


    def uiDeleteFurniture(self,params):
        if len(params)!=1:
            print("Parametrii invalizi! ")
        else:
            self.__service.deleteFurniture(params[0])

    def uiGetAll(self,params):
        if len(params)>0:
            print("Parametrii invalizi")
        else:
            print(self.__service.showFurniture())

    def uiBuy(self,params):
        if len(params)!=2:
            print("Parametrii invalizi")
        else:
            cod=params[0]
            if not params[1].isdigit():
                raise ValueError("Piese invalide")
            nr=int(params[1])
            name,price,newPieces=self.__service.buyFurniture(cod,nr)
            mesg="Am cumparat " +name + " in valoare de "+ str(price)+" lei si au mai ramas "+ str(newPieces)
            print(mesg)

    def run(self):
        while True:
            params = input(">>>")
            params.strip()
            params = params.split(" ")
            if len(params) == 0:
                print("Parametrii invalizi")
            if params[0]=="exit":
                exit(0)
            cmd_name=params[0].strip()
            params=params[1:]
            if cmd_name in self.__comenzi:
                try:
                    self.__comenzi[cmd_name](params)
                except ValueError as ex: print(ex)
                except ValidationError as ex: print(ex)
                except RepoError as ex: print(ex)
            else:
                print("Comanda invalida")

repo=FileRepo("D:\\Facultate\\Python\\AntrenamentSimulareFp\\Infrastructure\\furniture.txt")
validator=FurnitureValidator()
sf=ServiceFurniture(validator,repo)
ui=UI(sf)
ui.run()