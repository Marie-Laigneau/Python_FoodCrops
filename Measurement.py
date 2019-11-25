# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:35 2019
Measurement.py
Creates measurement class that defines the measurement of a commodity
@author: 
"""

from Indicator import Indicator
from Commodity import Commodity

class MeasurementType:
    def __init__(self, Id: int, dscp: str):
        self.id = Id # <int>
        self.description = dscp # <str>


class Measurement:
    def __init__(self, year: int, value: float, tId: int, tDesc: str, 
                 mtype: MeasurementType, commodity: Commodity, 
                 indicator: Indicator):
        self.__year = year
        self.__value = value
        self.__timeperiodId = tId
        self.__timeperiodDesc = tDesc
        self.mtype = mtype
        self.commodity = commodity
        self.indicator = indicator

    def describe(self):
        desc = ", Measurement : " + self.mtype.description
        return desc
