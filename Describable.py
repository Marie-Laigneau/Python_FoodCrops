# -*- coding: utf-8 -*-
"""
Describe.py
Abstract interface for describe method
@author: 
"""

from abc import ABC, abstractmethod

class Descriptor(ABCMeta):
    @abstractmethod
    def describe(self):
        desc = self.__class__.__name__
        return desc
