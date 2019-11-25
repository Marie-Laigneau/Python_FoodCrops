# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:35 2019
Measurement.py
Creates measurement class that defines the measurement of a commodity
@author: 
"""

from Indicator import Indicator
from Commodity import Commodity
from Describable import Descriptor


class Measurement(Descriptor):
    """Classe définissant une mesure correspondant à une ligne du jeu de 
    données"""
    
    def __init__(self, Id: int, year: int, value: float, tId: int, tDesc: str, 
                 commodity: Commodity, indicator: Indicator):
        """Une mesure est définie par son année, sa valeur, sa périodicité, 
        la culture vivière concernée, son indicateur de mesure, l'unité de cet 
        indicateur""" 
        
        self.id = Id   # Identifiant numerique de la mesure
        self._year = year   # Année de la mesure
        self._value = value   # Valeur numerique de la mesure
        self._timeperiodId = tId   # Identifiant numerique de la periode de temps couverte
        self._timeperiodDesc = tDesc   # Description textuelle de la periode
        self.commodity = commodity   # Culture viviere concernee
        self.indicator = indicator   # Indicateur de mesure

    def describe(self):
        desc = "Measurement_Id : " + self.id 
        + ", Year : " + self._year 
        + ", Time Period_Id : " + self._timeperiodId 
        + ", Time Period : " 
        + self._timeperiodDesc 
        + self.commodity.describe() 
        + self.indicator.describe() 
        + ", Amount : " + self._value
        return desc
