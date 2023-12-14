from Domain.mobilier import *

class testFurniture:
    def test_Furniture(self):
        masa = furniture("CI01", "lemn", "Masa de lemn de stejar", 100, 19.15)
        assert masa.getCode()=="CI01"
        assert masa.getType()=="lemn"
        assert masa.getName()=="Masa de lemn de stejar"
        assert masa.getStock()==100
        assert masa.getPrice()==19.15

