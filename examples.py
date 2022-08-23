# -*- coding: utf-8 -*-
"""
Created: 2022-08-23
@author: bro

"""

def make_default_file():
    from waza_tsl import TSLFile, Patch
    f = TSLFile("File with default values")
    p = Patch("Clear patch")
    f.append(p)
    f.save()
