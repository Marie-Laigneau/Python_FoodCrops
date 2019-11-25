# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:35 2019
Unit.py
Creates various unit-classes that inherit Unit class
@author: 
"""
from abc import ABC, abstractmethod

class Unit(ABC):
    """Classe définissant une unité de mesure"""
    
    def __init__(self, Id: int, name: str):
        super().__init__()
        self.id = Id
        self.name = name

#TODO add Describable attribute to sub-classes

class Price(Unit):
    """Classe définissant l'unité de mesure : Prix"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Price")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class Volume(Unit):
    """Classe définissant l'unité de mesure : Volume"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Volume")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class Weight(Unit):
    """Classe définissant l'unité de mesure : Poids"""
    
    def __init__(self, Id: int, multiplier: float):
        Unit.__init__(self, Id, "Weight")
        self.__multiplier = multiplier   # permet d'indiquer l'ordre de grandeur (Kilo, Mega, …)
    
    def describe(self):
        desc = ", Unit : " + self.name + " (" + self.__multiplier + ")"
        return desc


class Surface(Unit):
    """Classe définissant l'unité de mesure : Surface"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Surface")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class Count(Unit):
    """Classe définissant l'unité de mesure : Nombre"""
    
    def __init__(self, Id: int, what: str):
        Unit.__init__(self, Id, "Count")
        self.__what = what   # permet d'indiquer de quoi on parle (graines, …)
        
    def describe(self):
        desc = ", Unit : " + self.name + " (" + self.__what + ")"
        return desc


class Ratio(Unit):
    """Classe définissant l'unité de mesure : Ratio"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Ratio")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class UnitRatio(Ratio):
    """Classe définissant l'unité de mesure : UnitRatio"""

    def __init__(self, Id: int, unit1: Unit, unit2: Unit):
        Ratio.__init__(self, Id)
        self.__unit1 = unit1
        self.__unit2 = unit2
    
    def describe(self):
        desc = ", UnitRatio : " + self.__unit1.name + " per " + self.__unit2.name
        return desc

