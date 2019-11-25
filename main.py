#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:35 2019
Indicator.py
Creates indicators for a commodity
@author: 
"""

from FoodCropsDataset import FoodCropsDataset
from FoodCropFactory import FoodCropFactory
from Commodity import CommodityGroup
from Units import Price, Volume, Weight, Surface, Count, Ratio, UnitRatio
from Indicator import IndicatorGroup

def main():
    factory = FoodCropFactory()
    dataset = FoodCropsDataset(factory)
    path = str(input("Enter csv file path: "))
    dataset.load(path)
    option = str(input("Enter your option: "))
    while(option is not 'exit'):
        # option 'filter': 
        # display the resulting measurement according to the input criterion

        if option == 'filter':
            # get input criterion
            crit_comm = str(input("Which commodity group? Enter \'N\' for None: "))
            if crit_comm == 'N':
                crit1 = None
            else:
                # convert crit_comm string to its corresponding enum type
                try:
                    # take the lower case of user input
                    crit1 = CommodityGroup(crit_comm.lower())
                except:
                    print('The name you entered is not a valid commodity group\n')
                    option = 'filter'
                    # do it again
                    continue

            crit_indi = str(input("Which indicator group? Enter \'N\' for None: "))
            if crit_indi == 'N':
                crit2 = None
            else: 
                # do the same thing to crit_indi
                try:
                    # take the lower case of user input
                    crit2 = IndicatorGroup(crit_indi.lower())
                except:
                    print('The name you entered is not a valid indicator group\n')
                    option = 'filter'
                    # do it again
                    continue

            # no need to convert the geolocation input
            crit_geol = str(input("Which geographical location? Enter \'N\' for None: "))
            if crit_geol == 'N':
                crit3 = None
            else:
                crit3 = crit_geol

            # put unit input to correponding unit as in Unit class
            crit_unit = str(input("Which unit? Enter \'N\' for None: "))
            # switch to the right subclass
            if crit_unit == 'N':
                crit4 = None
            else:
                crit_unit = crit_unit.lower()
                if crit_unit == 'price':
                    crit4 = Price(0)

                elif crit_unit == 'volume':
                    crit4 = Volume(0)

                elif crit_unit == 'weight':
                    crit4 = Weight(0)

                elif crit_unit == 'surface':
                    crit4 = Surface(0)

                elif crit_unit == 'count':
                    crit4 = Count(0)

                elif crit_unit == 'ratio':
                    crit4 = Ratio(0)

                elif crit_unit == 'unitratio':
                    crit4 = UnitRatio(1, Ratio(0), Ratio(1))

                else:
                    print('The name you entered is not a valid unit name\n')
                    option = 'filter'
                    # do it again
                    continue

            dataset.findMeasurements(crit1, crit2, crit3, crit4)

        elif option == 'help':
            HELPMSG = 'Saisir \'filter\' pour filtrage et \'exit\' pour arrêter'
            print(HELPMSG + '\n')
        elif option == 'exit':
            break
        else :
            print('Please enter a valid option, or type \'help\'\n')

        option = str(input("Enter your option: "))

if __name__ == "__main__":
    # execute only if run as a script
    main()
