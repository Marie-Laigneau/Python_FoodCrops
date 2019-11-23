# -*- coding: utf-8 -*-
"""
FoodCropsFactory.py
Defines methods for creating other factory classes
Created on Wed Oct 23 14:31:35 2019

@author: 
"""

from Unit import *
from Measurement import *
from Indicator import Indicator
from Commodity import Commodity

class FoodCropFactory:
    """Classe permettant de créer de nouvelles instances des classes, de les
    indexer par identifiant, de renvoyer les classes déjà indexées quand on 
    demande la création avec un identifiant déjà connu"""
    
    def __init__(self):
        self._unitsRegistry = {}   # Création du dictionnaire de la classe Unit
        self._indicatorsRegistry = {}   # Création du premier dictionnaire de la classe Indicator (pour la recherche sur les indicateurs)
        self._commodityRegistry = {}   # Création du dictionnaire de la classe Commodity

    def createVolume(self, Id: int):
        """Méthode usine de la classe : Volume"""
        
        if 'Volume' in self.unitsRegistry.keys():
            if Id in self.unitsRegistry['Volume'].keys():
                return self.unitsRegistry['Volume'][Id]
            else:
                self.unitsRegistry['Volume'][Id] = Volume(Id)
                return self.unitsRegistry['Volume'][Id]
        else:
            self.unitsRegistry['Volume'] = {}
            self.unitsRegistry['Volume'][Id] = Volume(Id)
            return self.unitsRegistry['Volume'][Id]
        
    def createPrice(self, Id: int):
        """Méthode usine de la classe : Price"""
        
        if 'Price' in self.unitsRegistry.keys():
            if Id in self.unitsRegistry['Price'].keys():
                return self.unitsRegistry['Price'][Id]
            else:
                self.unitsRegistry['Price'][Id] = Price(Id)
                return self.unitsRegistry['Price'][Id]
        else:
            self.unitsRegistry['Price'] = {}
            self.unitsRegistry['Price'][Id] = Price(Id)
            return self.unitsRegistry['Price'][Id]

    def createWeight(self, Id: int, multiplier: float):
        """Méthode usine de la classe : Weight"""
        
        if 'Weight' in self.unitsRegistry.keys():
            if Id in self.unitsRegistry['Weight'].keys():
                return self.unitsRegistry['Weight'][Id]
            else:
                self.unitsRegistry['Weight'][Id] = Weight(Id, multiplier)
                return self.unitsRegistry['Weight'][Id]
        else:
            self.unitsRegistry['Weight'] = {}
            self.unitsRegistry['Weight'][Id] = Weight(Id, multiplier)
            return self.unitsRegistry['Weight'][Id]
    
    def createSurface(self, Id: int):
        """Méthode usine de la classe : Surface"""
        
        if 'Surface' in self.unitsRegistry.keys():
            if Id in self.unitsRegistry['Surface'].keys():
                return self.unitsRegistry['Surface'][Id]
            else:
                self.unitsRegistry['Surface'][Id] = Surface(Id)
                return self.unitsRegistry['Surface'][Id]
        else:
            self.unitsRegistry['Surface'] = {}
            self.unitsRegistry['Surface'][Id] = Surface(Id)
            return self.unitsRegistry['Surface'][Id]
        
    def createCount(self, Id: int, what: str):
        """Méthode usine de la classe : Count"""
        
        if 'Count' in self.unitsRegistry.keys():
            if Id in self.unitsRegistry['Count'].keys():
                return self.unitsRegistry['Count'][Id]
            else:
                self.unitsRegistry['Count'][Id] = Count(Id, what)
                return self.unitsRegistry['Count'][Id]
        else:
            self.unitsRegistry['Count'] = {}
            self.unitsRegistry['Count'][Id] = Count(Id, what)
            return self.unitsRegistry['Count'][Id]
        
    def createRatio(self, Id: int):
        """Méthode usine de la classe : Ratio"""
        
        if 'Ratio' in self.unitsRegistry.keys():
            if Id in self.unitsRegistry['Ratio'].keys():
                return self.unitsRegistry['Ratio'][Id]
            else:
                self.unitsRegistry['Ratio'][Id] = Ratio(Id)
                return self.unitsRegistry['Ratio'][Id]
        else:
            self.unitsRegistry['Ratio'] = {}
            self.unitsRegistry['Ratio'][Id] = Ratio(Id)
            return self.unitsRegistry['Ratio'][Id]
        
    def createUnitRatio(self, Id: int, unit1: Unit, unit2: Unit):
        """Méthode usine de la classe : UnitRatio"""
        
        if 'UnitRatio' in self.unitsRegistry.keys():
            if Id in self.unitsRegistry['UnitRatio'].keys():
                return self.unitsRegistry['UnitRatio'][Id]
            else:
                self.unitsRegistry['UnitRatio'][Id] = UnitRatio(Id, unit1, 
                                  unit2)
                return self.unitsRegistry['UnitRatio'][Id]
        else:
            self.unitsRegistry['UnitRatio'] = {}
            self.unitsRegistry['UnitRatio'][Id] = UnitRatio(Id, unit1, unit2)
            return self.unitsRegistry['UnitRatio'][Id]

    def createCommodity(self, group: CommodityGroup, Id: int, name: str):
        """Méthode usine de la classe : Commodity"""
        
        if group in self.commodityRegistry.keys():
            if Id in self.commodityRegistry[group].keys():
                return self.commodityRegistry[group][Id]
            else:
                self.commodityRegistry[group][Id] = Commodity(group, Id, name)
                return self.commodityRegistry[group][Id]
        else:
            self.commodityRegistry[group] = {}
            self.commodityRegistry[group][Id] = Commodity(group, Id, name)
            return self.commodityRegistry[group][Id]

    def createIndicator(self, Id: int, name : str, frequency: int, 
                        frequencyDesc: str, geogLocation: str, 
                        indicatorGroup: IndicatorGroup, unit: Unit):
        """Méthode usine de la classe : Indicator"""
        
        # Pour la recherche sur les indicateurs
        if indicatorGroup in self.indicatorsRegistry.keys():
            if Id in self.indicatorsRegistry[indicatorGroup].keys():
                return self.indicatorsRegistry[indicatorGroup][Id]
            else:
                self.indicatorsRegistry[indicatorGroup][Id] = Indicator(Id, 
                                       frequency, frequencyDesc, geogLocation, 
                                       indicatorGroup, unit)
                return self.indicatorsRegistry[indicatorGroup][Id]
        else:
            self.indicatorsRegistry[indicatorGroup] = {}
            self.indicatorsRegistry[indicatorGroup][Id] = Indicator(Id, 
                                       frequency, frequencyDesc, geogLocation, 
                                       indicatorGroup, unit)
            return self.indicatorsRegistry[indicatorGroup][Id]
        
    def createMeasurement(self, Id: int, year: int, value: float, 
                          timeperiodId: int, timeperiodDesc: str, 
                          commodity: Commodity, indicator: Indicator):
        """Méthode usine de la classe : Measurement"""
        
        return Measurement(Id, year, value, timeperiodId, timeperiodDesc, 
                    commodity, indicator)


        
