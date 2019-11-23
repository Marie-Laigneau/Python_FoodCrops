# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:35 2019
Indicator.py
Creates indicators for a commodity
@author: 
"""
from enum import Enum
from Units import *

class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = "exports and imports"
    SUPPLY_AND_USE      = "supply and use"
    PRICES              = "prices"
    FEED_PRICE_RATIOS   = "feed price ratios"
    QUANTITIES_FED      = "auqntities fed"
    TRANSPORTATION      = "transportation"
    ANIMAL_UNIT_INDEXES = "animal unit indexes"

class Indicator:        
    def __init__(self, Id: int, freq: int, freqDesc: str, 
                 geogLocation: str, group: IndicatorGroup, unit: Unit):
        self.id = Id #str
        self.frequency = freq #int
        self.frequencyDesc = freqDesc #str
        self.geoLocation = geoLoc #str
        self.IndicatorGroup = group #Enum: IndicatorGroup

    
