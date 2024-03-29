# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:35 2019
Indicator.py
Creates indicators for a commodity
@author: 
"""
from enum import Enum
from Units import Unit, Price, Volume, Weight, Surface, Count, Ratio, UnitRatio
from Describable import Descriptor


class IndicatorGroup(Enum):
    """Énumération des différents indicateurs existants"""
    
    EXPORTS_AND_IMPORTS = "exports and imports"
    SUPPLY_AND_USE      = "supply and use"
    PRICES              = "prices"
    FEED_PRICE_RATIOS   = "feed-price ratios"
    QUANTITIES_FED      = "quantities fed"
    TRANSPORTATION      = "transportation"
    ANIMAL_UNIT_INDEXES = "animal unit indexes"

class Indicator(Descriptor): 
    """Classe définissant les indicateurs (mesures dans certaines unités)"""
    
    def __init__(self, Id: int, frequency: int, freqDesc: str, 
                 geogLocation: str, group: IndicatorGroup, unit: Unit):
        self.id = Id   # Identifiant numerique de l'indicateur
        self._frequency = freq   # Identifiant numerique de la frequence de mesure
        self._frequencyDesc = freqDesc   # Description de la frequence de mesure
        self._geogLocation = geogLocation   # Description de la zone geographique
        self.indicatorGroup = group   # Groupe de l'indicateur (Enum)
        self.unit = unit   # Unite de la mesure
    
    def describe(self):
        desc = ", IndicatorGroup : " + self.indicatorGroup 
        + ", Indicator_Id : " + self.id 
        + ", Frequency_Id : " + self._frequency 
        + ", Frequency : " + self._frequencyDesc 
        + ", Geographical Location : " + self._geogLocation 
        + self.unit.describe()
        return desc
