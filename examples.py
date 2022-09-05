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

def make_mod_types():
    from waza_tsl import TSLFile, Patch, Color, MOD_type
    f = TSLFile("File with mod types")
    p1 = Patch("T.WAH")
    p1.set_mod(MOD_type.T_WAH,Color.GREEN,mode=1,polarity=0,sens=33,
               frequency=55,peak=66,effect_level=78,direct_mix=94)
    f.append(p1)
    p2 = Patch("AUTO WAH")
    p2.set_mod(MOD_type.AUTO_WAH,Color.YELLOW,mode=0,rate=11,depth=22,
               frequency=33,peak=44,effect_level=55,direct_mix=66)
    f.append(p2)
    f.save()

def make_fx_types():
    from waza_tsl import TSLFile, Patch, Color, FX_type
    f = TSLFile("File with fx types")
    p1 = Patch("T.WAH")
    p1.set_fx(FX_type.T_WAH,Color.RED,mode=0,polarity=1,sens=99,
               frequency=88,peak=77,effect_level=66,direct_mix=55)
    f.append(p1)
    p2 = Patch("AUTO WAH")
    p2.set_fx(FX_type.AUTO_WAH,Color.GREEN,mode=1,rate=44,depth=33,
               frequency=22,peak=11,effect_level=100,direct_mix=0)
    f.append(p2)
    f.save()

def make_mod_fx_pedal_wah():
    from waza_tsl import TSLFile, Patch, Color, MOD_type, FX_type, PEDAL_type
    f = TSLFile("File with pedal wah")
    p1 = Patch("G MOD VO VAH")
    p1.set_mod(MOD_type.PEDAL_WAH,Color.GREEN,type=PEDAL_type.VO_WAH,pedal_min=11,
              pedal_position=21,pedal_max=31,effect_level=61,direct_mix=81)
    f.append(p1)
    p2 = Patch("R MOD LIGHT WAH")
    p2.set_mod(MOD_type.PEDAL_WAH,Color.RED,type=PEDAL_type.LIGHT_WAH,pedal_min=12,
              pedal_position=22,pedal_max=32,effect_level=62,direct_mix=82)
    f.append(p2)
    p3 = Patch("Y FX 7STRING WAH")
    p3.set_fx(FX_type.PEDAL_WAH,Color.YELLOW,type=PEDAL_type.SEVEN_WAH,pedal_min=13,
              pedal_position=23,pedal_max=33,effect_level=63,direct_mix=83)
    f.append(p3)
    p4 = Patch("R FX RESO WAH")
    p4.set_fx(FX_type.PEDAL_WAH,Color.RED,type=PEDAL_type.RESO_WAH,pedal_min=14,
              pedal_position=24,pedal_max=34,effect_level=64,direct_mix=84)
    f.append(p4)
    f.save()

def make_mod_fx_comp():
    from waza_tsl import TSLFile, Patch, Color, MOD_type, FX_type, COMP_type
    f = TSLFile("File with comp types")
    p1 = Patch("G MOD BOSS COMP")
    p1.set_mod(MOD_type.COMP,Color.GREEN,type=COMP_type.BOSS_COMP,
               sustain=11,attack=31,level=61,tone=-45)
    f.append(p1)
    p2 = Patch("R MOD HI-BAND COMP")
    p2.set_mod(MOD_type.COMP,Color.RED,type=COMP_type.HI_BAND,
               sustain=12,attack=32,level=62,tone=-25)
    f.append(p2)
    p3 = Patch("Y MOD LIGHT COMP")
    p3.set_mod(MOD_type.COMP,Color.YELLOW,type=COMP_type.LIGHT,
               sustain=13,attack=33,level=63,tone=-5)
    f.append(p3)
    p4 = Patch("G FX D-COMP")
    p4.set_fx(FX_type.COMP,Color.GREEN,type=COMP_type.D_COMP,
               sustain=14,attack=34,level=64,tone=+15)
    f.append(p4)
    p5 = Patch("R FX ORANGE COMP")
    p5.set_fx(FX_type.COMP,Color.RED,type=COMP_type.ORANGE,
               sustain=15,attack=35,level=65,tone=+25)
    f.append(p5)
    p6 = Patch("Y FX FAT COMP")
    p6.set_fx(FX_type.COMP,Color.YELLOW,type=COMP_type.FAT,
               sustain=16,attack=36,level=66,tone=+35)
    f.append(p6)
    p7 = Patch("G FX MILD COMP")
    p7.set_fx(FX_type.COMP,Color.GREEN,type=COMP_type.MILD,
               sustain=17,attack=37,level=67,tone=+45)
    f.append(p7)
    f.save()

def make_mod_fx_limiter():
    from waza_tsl import TSLFile, Patch, Color, MOD_type, FX_type, LIMITER_type, RATIO_type
    f = TSLFile("File with limiter types")
    p1 = Patch("G MOD BOSS LIMITER")
    p1.set_mod(MOD_type.LIMITER,Color.GREEN,type=LIMITER_type.BOSS_LIMITER,
               threshold=11,attack=31,release=51,level=81,ratio=RATIO_type.R10to1)
    f.append(p1)
    p2 = Patch("R MOD RACK 160D LIMITER")
    p2.set_mod(MOD_type.LIMITER,Color.RED,type=LIMITER_type.RACK_160D,
               threshold=12,attack=32,release=52,level=82,ratio=RATIO_type.Rinfto1)
    f.append(p2)
    p3 = Patch("Y MOD VTG RACK U LIMITER")
    p3.set_mod(MOD_type.LIMITER,Color.YELLOW,type=LIMITER_type.VTG_RACK_U,
               threshold=13,attack=33,release=53,level=83,ratio=RATIO_type.R1p4to1)
    f.append(p3)
    p4 = Patch("G FX VTG RACK U LIMITER")
    p4.set_fx(FX_type.LIMITER,Color.GREEN,type=LIMITER_type.VTG_RACK_U,
               threshold=14,attack=34,release=54,level=84,ratio=RATIO_type.R2p6to1)
    f.append(p4)
    p5 = Patch("R FX BOSS LIMITER")
    p5.set_fx(FX_type.LIMITER,Color.RED,type=LIMITER_type.BOSS_LIMITER,
               threshold=15,attack=35,release=55,level=85,ratio=RATIO_type.R3p5to1)
    f.append(p5)
    p6 = Patch("Y FX RACK 160D LIMITER")
    p6.set_fx(FX_type.LIMITER,Color.YELLOW,type=LIMITER_type.RACK_160D,
               threshold=16,attack=36,release=56,level=86,ratio=RATIO_type.R6to1)
    f.append(p6)
    f.save()

def make_mod_fx_graphic_eq():
    from waza_tsl import TSLFile, Patch, Color, MOD_type, FX_type
    f = TSLFile("File with graphic eq")
    p1 = Patch("R MOD GRAPHIC EQ")
    p1.set_mod(MOD_type.GRAPHIC_EQ,Color.RED,level=+20,
               g31hz=-20,g62hz=-16,g125hz=-12,g250hz=-8,g500hz=-4,
               g1khz=0,g2khz=+4,g4khz=+8,g8khz=+12,g16khz=+16)
    f.append(p1)
    p2 = Patch("Y FX GRAPHIC EQ")
    p2.set_fx(FX_type.GRAPHIC_EQ,Color.YELLOW,level=-20,
               g31hz=+20,g62hz=+16,g125hz=+12,g250hz=+8,g500hz=+4,
               g1khz=0,g2khz=-4,g4khz=-8,g8khz=-12,g16khz=-16)
    f.append(p2)
    f.save()

def make_mod_fx_parametric_eq():
    from waza_tsl import TSLFile, Patch, Color, MOD_type, FX_type, Q_VALUE
    from waza_tsl import LOW_CUT, MID_FREQ, HIGH_CUT
    f = TSLFile("File with parametric eq")
    p1 = Patch("R MOD PARAM EQ enum")
    p1.set_mod(MOD_type.PARAMETRIC_EQ,Color.RED,level=+3,
               low_cut=LOW_CUT._FLAT,low_gain=-1,
               low_mid_frequency=MID_FREQ._630Hz,low_mid_gain=-4,low_mid_q=Q_VALUE._05,
               high_mid_frequency=MID_FREQ._2p50kHz,high_mid_gain=-5,high_mid_q=Q_VALUE._4,
               high_cut=HIGH_CUT._8kHz,high_gain=+1)
    f.append(p1)
    p2 = Patch("G FX PARAM EQ enum")
    p2.set_fx(FX_type.PARAMETRIC_EQ,Color.GREEN,level=+2,
               low_cut=LOW_CUT._100Hz,low_gain=-2,
               low_mid_frequency=MID_FREQ._800Hz,low_mid_gain=-5,low_mid_q=Q_VALUE._2,
               high_mid_frequency=MID_FREQ._1p60kHz,high_mid_gain=-4,high_mid_q=Q_VALUE._16,
               high_cut=HIGH_CUT._FLAT,high_gain=+2)
    f.append(p2)
    f.save()
