# -*- coding: utf-8 -*-
"""
Commodity.py
Enum class of the Commodity group
Created on Wed Oct 23 14:31:35 2019

@author: 
"""

from enum import Enum
from Describable import Descriptor


class CommodityGroup(Enum):
    """Énumération des différentes cultures vivières existantes"""
    
    CORN                 = "corn"
    BARLEY               = "barley"
    OATS                 = "oats"
    SORGHUM              = "sorghum"
    BYPRODUCT_FEEDS      = "byproduct feeds"
    COARSE_GRAINS        = "coarse grains"
    HAY                  = "hay"
    FEED_GRAINS          = "feed grains"
    ANIMAL_PROTEIN_FEEDS = "animal protein feeds"
    GRAIN_PROTEIN_FEEDS  = "grain protein feeds"
    PROCESSED_FEEDS      = "processed feeds"
    ENERGY_FEEDS         = "energy feeds"
    OILSEED_MEAL_FEEDS   = "oilseed meal feeds"


class Commodity(Descriptor):
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

