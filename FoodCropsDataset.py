# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:35 2019
FoodCropsDataset.py
Creates functions for reading the data and filtering them according to given criterion
@author: 
"""

from FoodCropFactory import FoodCropFactory
from Indicator import *
from Commodity import *
import pandas

class FoodCropsDataset:
    """Classe définissant le point d'entrée du modèle """
    
    def __init__(self, factory: FoodCropFactory):
        self.factory = factory
        self.__commodityGroupMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon les cultures vivieres
        self.__indicatorGroupMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon les indicateurs
        self.__locationMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon la zone geographique
        self.__unitMeasurementIndex = {}   # Création du dictionnaire pour la recherche selon l'unite de mesure
        self.measurementList = []
    
    def load(self, datasetPath: str):
        """Prends le chemin vers le fichier csv et réalise l'ensemble des 
        instanciations du modèle"""
        database = pandas.read_csv(datasetPath)
        c = 0
        m = 0
        for index, row in database.iterrows():   # On parcourt le jeu de données ligne par ligne
            c = c + 1
            m = 0
            #groupIndic_Id   = row[0]
            groupIndic_Desc  = row[1]
            #groupCommod_Id  = row[2]
            groupCommod_Desc = row[3]
            #geogLocation_Id = row[4]
            #sortOrder       = row[5]
            geogLocation     = row[6]
            commodity_Id     = row[7]
            commodity_Desc   = row[8]
            indicator_Id     = row[9]
            indicator_Desc   = row[10]
            unit_Id          = row[11]
            unit_Desc        = row[12]
            year             = row[13]
            frequency_Id     = row[14]
            frequency_Desc   = row[15]
            timeperiod_Id    = row[16]
            timeperiod_Desc  = row[17]
            amount           = row[18]
            
            # Pour la creation de l'unite
            if unit_Id == 4 or unit_Id == 5 or unit_Id == 12 or unit_Id == 31:
                unit = self.factory.createPrice(unit_Id)
            if unit_Id == 17 or unit_Id == 18:
                unit = self.factory.createVolume(unit_Id)
            if unit_Id == 7 or unit_Id == 8 or unit_Id == 9 or unit_Id == 41:
                if unit_Id == 7 or unit_Id == 9:
                    m = 1000
                if unit_Id == 8:
                    m = 1000000
                if unit_Id == 41:
                    m = 1
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
            if geogLocation not in self.__locationMeasurementIndex.keys():
                self.__locationMeasurementIndex[geogLocation] = {}
            self.__locationMeasurementIndex[geogLocation][c] = measurement
            
            # On rentre l'index du groupe de la culture viviere dans le 
            # dictionnaire correspondant associé à la mesure correspondante
            if (groupCommod_Desc not in 
                self.__commodityGroupMeasurementIndex.keys()):
                self.__commodityGroupMeasurementIndex[groupCommod_Desc] = {}
            self.__commodityGroupMeasurementIndex[groupCommod_Desc][c] = measurement
            
            # On rentre l'index du groupe de l'indicateur dans le dictionnaire
            # correspondant associé à la mesure correspondante
            if (groupIndic_Desc not in 
            self.__indicatorGroupMeasurementIndex.keys()):
                self.__indicatorGroupMeasurementIndex[groupIndic_Desc] = {}
            self.__indicatorGroupMeasurementIndex[groupIndic_Desc][c] = measurement
            
            # On rentre l'index de l'unite de mesure dans le dictionnaire
            # correspondant associé à la mesure correspondante
            if unit_Id not in self.__unitMeasurementIndex.keys():
                self.__unitMeasurementIndex[unit_Id] = {}
            self.__unitMeasurementIndex[unit_Id][c] = measurement
            
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
            list1 = self.__commodityGroupMeasurementIndex[commodityGroup.value.capitalize()]
        
        # On crée une liste comprenant l'ensemble des mesures ayant le meme 
        # groupe d'indicateur que celui recherché
        if indicatorGroup == None:
            list2 = self.measurementList
        else:
            list2 = self.__indicatorGroupMeasurementIndex[indicatorGroup.value]
        
        # On crée une liste comprenant l'ensemble des mesures ayant la meme 
        # unite de mesure que celle recherchée
        if unit == None:
            list3 = self.measurementList
        else:
            list3 = self.__unitMeasurementIndex[unit.name]
        
        # On crée une liste comprenant l'ensemble des mesures ayant la meme 
        # zone geographique que celle recherchée
        if geographicalLocation == None:
            list4 = self.measurementList
        else:
            list4 = self.__locationMeasurementIndex[geographicalLocation]
        
        # on crée une fonction pour chercher l'intersection entre 4 listes
        def intersection(l1, l2, l3, l4):
            return list(set(l1) & set(l2) & set(l3) & set(l4))

        L = intersection(list1, list2, list3, list4)
        
        for l in L:
            print(l.describe()+"\n")

