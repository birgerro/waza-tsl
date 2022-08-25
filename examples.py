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
    from waza_tsl import TSLFile, Patch, AMP_type
    f = TSLFile("File with amp types")
    p1 = Patch("ACOUSTIC")
    p1.set_amp(AMP_type.ACOUSTIC,
               gain=11,volume=21,bass=31,middle=41,treble=51,presence=61)
    f.append(p1)
    p2 = Patch("CLEAN")
    p2.set_amp(AMP_type.CLEAN,
               gain=12,volume=22,bass=32,middle=42,treble=52,presence=62)
               # Note: gain=12 is changed to gain=13
    f.append(p2)
    p3 = Patch("CRUNCH")
    p3.set_amp(AMP_type.CRUNCH,
               gain=13,volume=23,bass=33,middle=43,treble=53,presence=63)
    f.append(p3)
    p4 = Patch("LEAD")
    p4.set_amp(AMP_type.LEAD,
               gain=14,volume=24,bass=34,middle=44,treble=54,presence=64)
    f.append(p4)
    p5 = Patch("BROWN")
    p5.set_amp(AMP_type.BROWN,
               gain=15,volume=25,bass=35,middle=45,treble=55,presence=65)
    f.append(p5)
    f.save()

def make_bst_types():
    from waza_tsl import TSLFile, Patch, Color, BST_type
    f = TSLFile("File with bst types")
    p1 = Patch("TREBLE BOOST")
    p1.set_bst(BST_type.TREBLE_BOOST,Color.GREEN,drive=10,bottom=-50,tone=-45,
               solo_sw=0,solo_level=14,effect_level=16,direct_mix=18)
    f.append(p1)
    p2 = Patch("FAT DS")
    p2.set_bst(BST_type.FAT_DS,Color.RED,drive=30,bottom=-30,tone=-25,
               solo_sw=1,solo_level=34,effect_level=36,direct_mix=38)
    f.append(p2)
    p3 = Patch("BLUES DRIVE")
    p3.set_bst(BST_type.BLUES_DRIVE,Color.YELLOW,drive=50,bottom=-10,tone=-5,
               solo_sw=0,solo_level=54,effect_level=56,direct_mix=58)
    f.append(p3)
    p4 = Patch("T-SCREAM")
    p4.set_bst(BST_type.T_SCREAM,Color.GREEN,drive=80,bottom=+10,tone=+5,
               solo_sw=1,solo_level=74,effect_level=76,direct_mix=78)
    f.append(p4)
    p5 = Patch("DST+")
    p5.set_bst(BST_type.DSTPLUS,Color.RED,drive=100,bottom=+30,tone=+25,
               solo_sw=0,solo_level=84,effect_level=86,direct_mix=88)
    f.append(p5)
    p6 = Patch("'60s FUZZ")
    p6.set_bst(BST_type.SIXTIES_FUZZ,Color.YELLOW,drive=120,bottom=+50,tone=+45,
               solo_sw=1,solo_level=94,effect_level=96,direct_mix=98)
    f.append(p6)
    f.save()
