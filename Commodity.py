# -*- coding: utf-8 -*-
"""
Commodity.py
Enum class of the Commodity group
Created on Wed Oct 23 14:31:35 2019

@author: 
"""

from enum import Enum

class CommodityGroup(Enum):
    """Énumération des différentes cultures vivières existantes"""
    
    CORN                 = "Corn"
    BARLEY               = "Barley"
    OATS                 = "Oats"
    SORGHUM              = "Sorghum"
    BYPRODUCT_FEEDS      = "Byproduct feeds"
    COARSE_GRAINS        = "Coarse grains"
    HAY                  = "Hay"
    FEED_GRAINS          = "Feed grains"
    ANIMAL_PROTEIN_FEEDS = "Animal protein feeds"
    GRAIN_PROTEIN_FEEDS  = "Grain protein feeds"
    PROCESSED_FEEDS      = "Processed feeds"
    ENERGY_FEEDS         = "Energy feeds"
    OILSEED_MEAL_FEEDS   = "Oilseed meal feeds"


class Commodity:
    """Classe définissant les cultures vivières"""
    
    def __init__(self, group: CommodityGroup, Id: int, name: str):
        self.id = Id   # Identifiant numerique de la culture viviere
        self._name = name   # Description de la culture viviere
        self.group = group   # Groupe de la culture viviere
    
    def describe(self):
        desc = ", CommodityGroup : " + self.group 
        + ", Commodity_Id : " + self.id 
        + ", Commodity_Name : " + self._name
        return desc

