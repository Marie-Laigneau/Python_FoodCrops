# -*- coding: utf-8 -*-
"""
FoodCropsFactory.py
Defines methods for creating other factory classes
Created on Wed Oct 23 14:31:35 2019

@author: 
"""

from Units import *
from Measurement import *
from Indicator import Indicator, IndicatorGroup
from Commodity import Commodity, CommodityGroup

class FoodCropFactory:
    """Classe permettant de créer de nouvelles instances des classes, de les
    indexer par identifiant, de renvoyer les classes déjà indexées quand on 
    demande la création avec un identifiant déjà connu"""
    
    def __init__(self):
        self.__unitsRegistry = {}   # Création du dictionnaire de la classe Unit
        self.__indicatorsRegistry = {}   # Création du premier dictionnaire de la classe Indicator (pour la recherche sur les indicateurs)
        self.__commodityRegistry = {}   # Création du dictionnaire de la classe Commodity

    def createVolume(self, Id: int):
        """Méthode usine de la classe : Volume"""
        
        if 'Volume' in self.__unitsRegistry.keys():
            if Id in self.__unitsRegistry['Volume'].keys():
                return self.__unitsRegistry['Volume'][Id]
            else:
                self.__unitsRegistry['Volume'][Id] = Volume(Id)
                return self.__unitsRegistry['Volume'][Id]
        else:
            self.__unitsRegistry['Volume'] = {}
            self.__unitsRegistry['Volume'][Id] = Volume(Id)
            return self.__unitsRegistry['Volume'][Id]
        
    def createPrice(self, Id: int):
        """Méthode usine de la classe : Price"""
        
        if 'Price' in self.__unitsRegistry.keys():
            if Id in self.__unitsRegistry['Price'].keys():
                return self.__unitsRegistry['Price'][Id]
            else:
                self.__unitsRegistry['Price'][Id] = Price(Id)
                return self.__unitsRegistry['Price'][Id]
        else:
            self.__unitsRegistry['Price'] = {}
            self.__unitsRegistry['Price'][Id] = Price(Id)
            return self.__unitsRegistry['Price'][Id]

    def createWeight(self, Id: int, multiplier: float):
        """Méthode usine de la classe : Weight"""
        
        if 'Weight' in self.__unitsRegistry.keys():
            if Id in self.__unitsRegistry['Weight'].keys():
                return self.__unitsRegistry['Weight'][Id]
            else:
                self.__unitsRegistry['Weight'][Id] = Weight(Id, multiplier)
                return self.__unitsRegistry['Weight'][Id]
        else:
            self.__unitsRegistry['Weight'] = {}
            self.__unitsRegistry['Weight'][Id] = Weight(Id, multiplier)
            return self.__unitsRegistry['Weight'][Id]
    
    def createSurface(self, Id: int):
        """Méthode usine de la classe : Surface"""
        
        if 'Surface' in self.__unitsRegistry.keys():
            if Id in self.__unitsRegistry['Surface'].keys():
                return self.__unitsRegistry['Surface'][Id]
            else:
                self.__unitsRegistry['Surface'][Id] = Surface(Id)
                return self.__unitsRegistry['Surface'][Id]
        else:
            self.__unitsRegistry['Surface'] = {}
            self.__unitsRegistry['Surface'][Id] = Surface(Id)
            return self.__unitsRegistry['Surface'][Id]
        
    def createCount(self, Id: int, what: str):
        """Méthode usine de la classe : Count"""
        
        if 'Count' in self.__unitsRegistry.keys():
            if Id in self.__unitsRegistry['Count'].keys():
                return self.__unitsRegistry['Count'][Id]
            else:
                self.__unitsRegistry['Count'][Id] = Count(Id, what)
                return self.__unitsRegistry['Count'][Id]
        else:
            self.__unitsRegistry['Count'] = {}
            self.__unitsRegistry['Count'][Id] = Count(Id, what)
            return self.__unitsRegistry['Count'][Id]
        
    def createRatio(self, Id: int):
        """Méthode usine de la classe : Ratio"""
        
        if 'Ratio' in self.__unitsRegistry.keys():
            if Id in self.__unitsRegistry['Ratio'].keys():
                return self.__unitsRegistry['Ratio'][Id]
            else:
                self.__unitsRegistry['Ratio'][Id] = Ratio(Id)
                return self.__unitsRegistry['Ratio'][Id]
        else:
            self.__unitsRegistry['Ratio'] = {}
            self.__unitsRegistry['Ratio'][Id] = Ratio(Id)
            return self.__unitsRegistry['Ratio'][Id]
        
    def createUnitRatio(self, Id: int, unit1: Unit, unit2: Unit):
        """Méthode usine de la classe : UnitRatio"""
        
        if 'UnitRatio' in self.__unitsRegistry.keys():
            if Id in self.__unitsRegistry['UnitRatio'].keys():
                return self.__unitsRegistry['UnitRatio'][Id]
            else:
                self.__unitsRegistry['UnitRatio'][Id] = UnitRatio(Id, unit1, 
                                  unit2)
                return self.__unitsRegistry['UnitRatio'][Id]
        else:
            self.__unitsRegistry['UnitRatio'] = {}
            self.__unitsRegistry['UnitRatio'][Id] = UnitRatio(Id, unit1, unit2)
            return self.__unitsRegistry['UnitRatio'][Id]

    def createCommodity(self, group: CommodityGroup, Id: int, name: str):
        """Méthode usine de la classe : Commodity"""
        
        if group in self.__commodityRegistry.keys():
            if Id in self.__commodityRegistry[group].keys():
                return self.__commodityRegistry[group][Id]
            else:
                self.__commodityRegistry[group][Id] = Commodity(group, Id, name)
                return self.__commodityRegistry[group][Id]
        else:
            self.__commodityRegistry[group] = {}
            self.__commodityRegistry[group][Id] = Commodity(group, Id, name)
            return self.__commodityRegistry[group][Id]

    def createIndicator(self, Id: int, name : str, frequency: int, 
                        frequencyDesc: str, geogLocation: str, 
                        indicatorGroup: IndicatorGroup, unit: Unit):
        """Méthode usine de la classe : Indicator"""
        
        # Pour la recherche sur les indicateurs
        if indicatorGroup in self.__indicatorsRegistry.keys():
            if Id in self.__indicatorsRegistry[indicatorGroup].keys():
                return self.__indicatorsRegistry[indicatorGroup][Id]
            else:
                self.__indicatorsRegistry[indicatorGroup][Id] = Indicator(Id, 
                                       frequency, frequencyDesc, geogLocation, 
                                       indicatorGroup, unit)
                return self.__indicatorsRegistry[indicatorGroup][Id]
        else:
            self.__indicatorsRegistry[indicatorGroup] = {}
            self.__indicatorsRegistry[indicatorGroup][Id] = Indicator(Id, 
                                       frequency, frequencyDesc, geogLocation, 
                                       indicatorGroup, unit)
            return self.__indicatorsRegistry[indicatorGroup][Id]
        
    def createMeasurement(self, Id: int, year: int, value: float, 
                          timeperiodId: int, timeperiodDesc: str, 
                          commodity: Commodity, indicator: Indicator):
        """Méthode usine de la classe : Measurement"""
        
        return Measurement(Id, year, value, timeperiodId, timeperiodDesc, 
                    commodity, indicator)


        
