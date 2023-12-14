from Domain.mobilier import *
from Exceptions.exceptions import *
class FurnitureValidator():

    def validation(self,furniture):
        errors=""
        if type(furniture.getPrice())!=float:
            errors+="Stoc invalid; "
        if type(furniture.getStock())!=int:
            errors+="Pret invalid; "
        if furniture.getStock()<=0:
            errors+="Stocul invalid. Stocul nu poate sa fie mai mic ca zero; "
        if furniture.getPrice()<=0.0:
            errors+="Pret invalid; "
        if len(errors)>1:
            raise ValidationError(errors)

