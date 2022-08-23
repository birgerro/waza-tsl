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

def make_amp_types():
    from waza_tsl import TSLFile, Patch, ACOUSTIC,CLEAN,CRUNCH,LEAD,BROWN
    f = TSLFile("File with amp types")
    p1 = Patch("ACOUSTIC")
    p1.set_amp(ACOUSTIC,gain=11,volume=21,bass=31,middle=41,treble=51,presence=61)
    f.append(p1)
    p2 = Patch("CLEAN")
    p2.set_amp(CLEAN,gain=12,volume=22,bass=32,middle=42,treble=52,presence=62)
    f.append(p2)
    p3 = Patch("CRUNCH")
    p3.set_amp(CRUNCH,gain=13,volume=23,bass=33,middle=43,treble=53,presence=63)
    f.append(p3)
    p4 = Patch("LEAD")
    p4.set_amp(LEAD,gain=14,volume=24,bass=34,middle=44,treble=54,presence=64)
    f.append(p4)
    p5 = Patch("BROWN")
    p5.set_amp(BROWN,gain=15,volume=25,bass=35,middle=45,treble=55,presence=65)
    f.append(p5)
    f.save()
