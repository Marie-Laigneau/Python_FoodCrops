# -*- coding: utf-8 -*-
"""
Commodity.py
Enum class of the Commodity group
Created on Wed Oct 23 14:31:35 2019

@author: 
"""

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
    OTHER                = "other"


