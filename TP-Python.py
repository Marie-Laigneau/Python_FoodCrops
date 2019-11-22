#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:13:59 2019

@author: marielaigneau
"""

from enum import Enum
from abc import ABC, abstractmethod
import pandas


################################# DESCRIBABLE #################################

class Describable(ABC):
    
    def __init__():
        super.__init__()
    
    @abstractmethod
    def describe(self):
        pass


#################################### UNITS ####################################

class Unit(ABC):
    """Classe définissant une unité de mesure"""
    
    def __init__(self, Id: int, name: str):
        super().__init__()
        self.id = Id
        self.name = name


class Price(Unit, Describable):
    """Classe définissant l'unité de mesure : Prix"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Price")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class Volume(Unit, Describable):
    """Classe définissant l'unité de mesure : Volume"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Volume")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class Weight(Unit, Describable):
    """Classe définissant l'unité de mesure : Poids"""
    
    def __init__(self, Id: int, multiplier: float):
        Unit.__init__(self, Id, "Weight")
        self._multiplier = multiplier   # permet d'indiquer l'ordre de grandeur (Kilo, Mega, …)
    
    def describe(self):
        desc = ", Unit : " + self.name + " (" + self._multiplier + ")"
        return desc


class Surface(Unit, Describable):
    """Classe définissant l'unité de mesure : Surface"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Surface")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class Count(Unit, Describable):
    """Classe définissant l'unité de mesure : Nombre"""
    
    def __init__(self, Id: int, what: str):
        Unit.__init__(self, Id, "Count")
        self._what = what   # permet d'indiquer de quoi on parle (graines, …)
        
    def describe(self):
        desc = ", Unit : " + self.name + " (" + self._what + ")"
        return desc


class Ratio(Unit, Describable):
    """Classe définissant l'unité de mesure : Ratio"""
    
    def __init__(self, Id: int):
        Unit.__init__(self, Id, "Ratio")
    
    def describe(self):
        desc = ", Unit : " + self.name
        return desc


class UnitRatio(Ratio, Describable):
    
    def __init__(self, Id: int, unit1: Unit, unit2: Unit):
        Ratio.__init__(self, Id)
        self._unit1 = unit1
        self._unit2 = unit2
    
    def describe(self):
        desc = ", Unit : " + self._unit1.name + " per " + self._unit2.name
        return desc



################################## COMMODITY ##################################

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


class Commodity(Describable):
    """Classe définissant les cultures vivières"""
    
    def __init__(self, group: CommodityGroup, Id: int, name: str):
        self.id = Id   # Identifiant numerique de la culture viviere
        self._name = name   # Description de la culture viviere
        self.group = group   # Groupe de la culture viviere
    
    def describe(self):
        desc = ", CommodityGroup : " + self.group + ", Commodity_Id : " 
        + self.id + ", Commodity_Name : " + self._name
        return desc



################################## INDICATOR ##################################

class IndicatorGroup(Enum):
    """Énumération des différents indicateurs existants"""
    
    EXPORTS_AND_IMPORTS = "exports and imports"
    SUPPLY_AND_USE      = "supply and use"
    PRICES              = "prices"
    FEED_PRICE_RATIOS   = "feed price ratios"
    QUANTITIES_FED      = "quantities fed"
    TRANSPORTATION      = "transportation"
    ANIMAL_UNIT_INDEXES = "animal unit indexes"


class Indicator(Describable):
    """Classe définissant les indicateurs (mesures dans certaines unités)"""
      
    def __init__(self, Id: int, name: str, frequency: int, frequencyDesc: str, 
                 geogLocation: str, indicatorGroup: IndicatorGroup, 
                 unit: Unit):
        """Un indicateur fait partie d'un groupe d'indicateurs (Enum)"""
        
        self.id = Id   # Identifiant numerique de l'indicateur
        self.name = name   # Description de l'indicateur
        self._frequency = frequency   # Identifiant numerique de la frequence de mesure
        self._frequencyDesc = frequencyDesc   # Description de la frequence de mesure
        self._geogLocation = geogLocation   # Description de la zone geographique
        self.indicatorGroup = indicatorGroup   # Groupe de l'indicateur  
        self.unit = unit   # Unite de la mesure
    
    def describe(self):
        desc = ", IndicatorGroup : " + self.indicatorGroup 
        + ", Indicator_Id : " + self.id + ", Indicator_Name : " + self.name 
        + ", Frequency_Id : " + self._frequency + ", Frequency : " 
        + self._frequencyDesc + ", Geographical Location : " 
        + self._geogLocation + self.unit.describe()
        return desc



################################# MEASUREMENT #################################

class Measurement(Describable):
    """Classe définissant une mesure correspondant à une ligne du jeu de 
    données"""
    
    def __init__(self, Id: int, year: int, value: float, timeperiodId: int, 
                 timeperiodDesc: str, commodity: Commodity, 
                 indicator: Indicator):
        """Une mesure est définie par son année, sa valeur, sa périodicité, 
        la culture vivière concernée, son indicateur de mesure, l'unité de cet 
        indicateur""" 
        
        self.id = Id   # Identifiant numerique de la mesure
        self._year = year   # Année de la mesure
        self._value = value   # Valeur numerique de la mesure
        self._timeperiodId = timeperiodId   # Identifiant numerique de la periode de temps couverte
        self._timeperiodDesc = timeperiodDesc   # Description textuelle de la periode
        self.commodity = commodity   # Culture viviere concernee
        self.indicator = indicator   # Indicateur de mesure
    
    def describe(self):
        desc = "Measurement_Id : " + self.id + ", Year : " + self._year 
        + ", Time Period_Id : " + self._timeperiodId + ", Time Period : " 
        + self._timeperiodDesc + self.commodity.describe() 
        + self.indicator.describe() + ", Amount : " + self._value
        return desc


############################## FOOD CROPS FACTORY ##############################

class FoodCropsFactory:
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


############################# FOOD CROPS DATASET ##############################

class FoodCropsDataset:
    """Classe définissant le point d'entrée du modèle """
    
    def __init__(self, factory: FoodCropsFactory):
        self.factory = factory
        self._commodityGroupMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon les cultures vivieres
        self._indicatorGroupMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon les indicateurs
        self._locationMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon la zone geographique
        self._unitMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon l'unite de mesure
        self.measurementList = []
    
    def load(self, datasetPath: str):
        """Prends le chemin vers le fichier csv et réalise l'ensemble des 
        instanciations du modèle"""
        database = pandas.read_csv(datasetPath)
        c=0
        m=0
        for index, row in database.iterrows():   # On parcourt le jeu de données ligne par ligne
            c+=1
            m==0
            #groupIndic_Id = row[1]
            groupIndic_Desc = row[2]
            #groupCommod_Id = row[3]
            groupCommod_Desc = row[4]
            #geogLocation_Id = row[5]
            #sortOrder = row[6]
            geogLocation = row[7]
            commodity_Id = row[8]
            commodity_Desc = row[9]
            indicator_Id = row[10]
            indicator_Desc = row[11]
            unit_Id = row[12]
            unit_Desc = row[13]
            year = row[14]
            frequency_Id = row[15]
            frequency_Desc = row[16]
            timeperiod_Id = row[17]
            timeperiod_Desc = row[18]
            amount = row[19]
            
            # Pour la creation de l'unite
            if unit_Id == 4 or unit_Id == 5 or unit_Id == 12 or unit_Id == 31:
                unit = self.factory.createPrice(unit_Id)
            if unit_Id == 17 or unit_Id == 18:
                unit = self.factory.createVolume(unit_Id)
            if unit_Id == 7 or unit_Id == 8 or unit_Id == 9 or unit_Id == 41:
                if unit_Id == 7 or unit_Id == 9:
                    m=1000
                if unit_Id == 8:
                    m=1000000
                if unit_Id == 41:
                    m=1
                unit = self.factory.createWeight(unit_Id,m)
            if unit_Id == 2 or unit_Id == 10 or unit_Id == 44:
                unit = self.factory.createSurface(unit_Id)
            if (unit_Id == 1 or unit_Id == 3 or unit_Id == 15 or unit_Id == 16 
            or unit_Id == 46):
                unit = self.factory.createCount(unit_Id, unit_Desc)
            if (unit_Id == 13 or unit_Id == 6 or unit_Id == 11 or unit_Id == 14 
            or unit_Id == 45):
                unit = self.factory.createRatio(unit_Id)
            
            # Pour la creation de l'indicateur
            indicator = self.factory.createIndicator(indicator_Id, 
                        indicator_Desc, frequency_Id, frequency_Desc, 
                        geogLocation, groupIndic_Desc, unit)
            
            # Pour la creation de la culture viviere
            commodity = self.factory.createCommodity(groupCommod_Desc, 
                        commodity_Id, commodity_Desc)
            
            # Pour la creation de la mesure
            measurement = self.factory.createMeasurement(c, year, amount, 
                        timeperiod_Id, timeperiod_Desc, commodity, indicator)
            
            # On rentre l'index de la zone geographique dans le dictionnaire 
            # correspondant associé à la mesure correspondante
            if geogLocation not in self._locationMeasurementIndex.keys():
                self._locationMeasurementIndex[geogLocation] = {}
            self._locationMeasurementIndex[geogLocation][c] = measurement
            
            # On rentre l'index du groupe de la culture viviere dans le 
            # dictionnaire correspondant associé à la mesure correspondante
            if (groupCommod_Desc not in 
                self._commodityGroupMeasurementIndex.keys()):
                self._commodityGroupMeasurementIndex[groupCommod_Desc] = {}
            self._commodityGroupMeasurementIndex[groupCommod_Desc][c] = measurement
            
            # On rentre l'index du groupe de l'indicateur dans le dictionnaire
            # correspondant associé à la mesure correspondante
            if (groupIndic_Desc not in 
            self._indicatorGroupMeasurementIndex.keys()):
                self._indicatorGroupMeasurementIndex[groupIndic_Desc] = {}
            self._indicatorGroupMeasurementIndex[groupIndic_Desc][c] = measurement
            
            # On rentre l'index de l'unite de mesure dans le dictionnaire
            # correspondant associé à la mesure correspondante
            if unit_Id not in self._unitMeasurementIndex.keys():
                self._unitMeasurementIndex[unit_Id] = {}
            self._unitMeasurementIndex[unit_Id][c] = measurement
            
            self.measurementList.append(measurement)

    def findMeasurements(self, commodityGroup : CommodityGroup = None, 
                         indicatorGroup : IndicatorGroup = None, 
                         geographicalLocation : str = None, 
                         unit : Unit = None):
        
        # On crée une liste comprenant l'ensemble des mesures ayant le meme 
        # groupe de culture viviere que celui recherché
        if commodityGroup == None:
            list1 = self.measurementList   # regarder si il est possible de passer directement par la bibliothèque
        else:
            list1 = self._commodityGroupMeasurementIndex[commodityGroup.value]
        
        # On crée une liste comprenant l'ensemble des mesures ayant le meme 
        # groupe d'indicateur que celui recherché
        if indicatorGroup == None:
            list2 = self.measurementList
        else:
            list2 = self._indicatorGroupMeasurementIndex[indicatorGroup.value]
        
        # On crée une liste comprenant l'ensemble des mesures ayant la meme 
        # unite de mesure que celle recherchée
        if unit == None:
            list3 = self.measurementList
        else:
            list3 = self._unitMeasurementIndex[unit.value]
        
        # On crée une liste comprenant l'ensemble des mesures ayant la meme 
        # zone geographique que celle recherchée
        if geographicalLocation == None:
            list4 = self.measurementList
        else:
            list4 = self._locationMeasurementIndex[geographicalLocation.value]
        
        L = list1.intersection(list2, list3, list4)
        
        for l in L:
            print(l.describe()+"\n")

