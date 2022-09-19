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
    from waza_tsl import TSLFile, Patch, AMP
    f = TSLFile("File with amp types")
    p1 = Patch("ACOUSTIC")
    p1.set_amp(AMP.ACOUSTIC,
               gain=11,volume=21,bass=31,middle=41,treble=51,presence=61)
    f.append(p1)
    p2 = Patch("CLEAN")
    p2.set_amp(AMP.CLEAN,
               gain=12,volume=22,bass=32,middle=42,treble=52,presence=62)
               # Note: gain=12 is changed to gain=13
    f.append(p2)
    p3 = Patch("CRUNCH")
    p3.set_amp(AMP.CRUNCH,
               gain=13,volume=23,bass=33,middle=43,treble=53,presence=63)
    f.append(p3)
    p4 = Patch("LEAD")
    p4.set_amp(AMP.LEAD,
               gain=14,volume=24,bass=34,middle=44,treble=54,presence=64)
    f.append(p4)
    p5 = Patch("BROWN")
    p5.set_amp(AMP.BROWN,
               gain=15,volume=25,bass=35,middle=45,treble=55,presence=65)
    f.append(p5)
    f.save()

def make_bst_types():
    from waza_tsl import TSLFile, Patch, Color, BST
    f = TSLFile("File with bst types")
    p1 = Patch("TREBLE BOOST")
    p1.set_bst(BST.TREBLE_BOOST,Color.GREEN,drive=10,bottom=-50,tone=-45,
               solo_sw=0,solo_level=14,effect_level=16,direct_mix=18)
    f.append(p1)
    p2 = Patch("FAT DS")
    p2.set_bst(BST.FAT_DS,Color.RED,drive=30,bottom=-30,tone=-25,
               solo_sw=1,solo_level=34,effect_level=36,direct_mix=38)
    f.append(p2)
    p3 = Patch("BLUES DRIVE")
    p3.set_bst(BST.BLUES_DRIVE,Color.YELLOW,drive=50,bottom=-10,tone=-5,
               solo_sw=0,solo_level=54,effect_level=56,direct_mix=58)
    f.append(p3)
    p4 = Patch("T-SCREAM")
    p4.set_bst(BST.T_SCREAM,Color.GREEN,drive=80,bottom=+10,tone=+5,
               solo_sw=1,solo_level=74,effect_level=76,direct_mix=78)
    f.append(p4)
    p5 = Patch("DST+")
    p5.set_bst(BST.DSTPLUS,Color.RED,drive=100,bottom=+30,tone=+25,
               solo_sw=0,solo_level=84,effect_level=86,direct_mix=88)
    f.append(p5)
    p6 = Patch("'60s FUZZ")
    p6.set_bst(BST.SIXTIES_FUZZ,Color.YELLOW,drive=120,bottom=+50,tone=+45,
               solo_sw=1,solo_level=94,effect_level=96,direct_mix=98)
    f.append(p6)
    f.save()

def make_mod_types():
    from waza_tsl import TSLFile, Patch, Color, MOD
    f = TSLFile("File with mod types")
    p1 = Patch("T.WAH")
    p1.set_mod(MOD.T_WAH,Color.GREEN,mode=1,polarity=0,sens=33,
               frequency=55,peak=66,effect_level=78,direct_mix=94)
    f.append(p1)
    p2 = Patch("AUTO WAH")
    p2.set_mod(MOD.AUTO_WAH,Color.YELLOW,mode=0,rate=11,depth=22,
               frequency=33,peak=44,effect_level=55,direct_mix=66)
    f.append(p2)
    f.save()

def make_fx_types():
    from waza_tsl import TSLFile, Patch, Color, FX
    f = TSLFile("File with fx types")
    p1 = Patch("T.WAH")
    p1.set_fx(FX.T_WAH,Color.RED,mode=0,polarity=1,sens=99,
               frequency=88,peak=77,effect_level=66,direct_mix=55)
    f.append(p1)
    p2 = Patch("AUTO WAH")
    p2.set_fx(FX.AUTO_WAH,Color.GREEN,mode=1,rate=44,depth=33,
               frequency=22,peak=11,effect_level=100,direct_mix=0)
    f.append(p2)
    f.save()

def make_mod_fx_pedal_wah():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, PEDAL
    f = TSLFile("File with pedal wah")
    p1 = Patch("G MOD VO VAH")
    p1.set_mod(MOD.PEDAL_WAH,Color.GREEN,type=PEDAL.VO_WAH,pedal_min=11,
              pedal_position=21,pedal_max=31,effect_level=61,direct_mix=81)
    f.append(p1)
    p2 = Patch("R MOD LIGHT WAH")
    p2.set_mod(MOD.PEDAL_WAH,Color.RED,type=PEDAL.LIGHT_WAH,pedal_min=12,
              pedal_position=22,pedal_max=32,effect_level=62,direct_mix=82)
    f.append(p2)
    p3 = Patch("Y FX 7STRING WAH")
    p3.set_fx(FX.PEDAL_WAH,Color.YELLOW,type=PEDAL.SEVEN_WAH,pedal_min=13,
              pedal_position=23,pedal_max=33,effect_level=63,direct_mix=83)
    f.append(p3)
    p4 = Patch("R FX RESO WAH")
    p4.set_fx(FX.PEDAL_WAH,Color.RED,type=PEDAL.RESO_WAH,pedal_min=14,
              pedal_position=24,pedal_max=34,effect_level=64,direct_mix=84)
    f.append(p4)
    f.save()

def make_mod_fx_comp():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, COMP
    f = TSLFile("File with comp types")
    p1 = Patch("G MOD BOSS COMP")
    p1.set_mod(MOD.COMP,Color.GREEN,type=COMP.BOSS_COMP,
               sustain=11,attack=31,level=61,tone=-45)
    f.append(p1)
    p2 = Patch("R MOD HI-BAND COMP")
    p2.set_mod(MOD.COMP,Color.RED,type=COMP.HI_BAND,
               sustain=12,attack=32,level=62,tone=-25)
    f.append(p2)
    p3 = Patch("Y MOD LIGHT COMP")
    p3.set_mod(MOD.COMP,Color.YELLOW,type=COMP.LIGHT,
               sustain=13,attack=33,level=63,tone=-5)
    f.append(p3)
    p4 = Patch("G FX D-COMP")
    p4.set_fx(FX.COMP,Color.GREEN,type=COMP.D_COMP,
               sustain=14,attack=34,level=64,tone=+15)
    f.append(p4)
    p5 = Patch("R FX ORANGE COMP")
    p5.set_fx(FX.COMP,Color.RED,type=COMP.ORANGE,
               sustain=15,attack=35,level=65,tone=+25)
    f.append(p5)
    p6 = Patch("Y FX FAT COMP")
    p6.set_fx(FX.COMP,Color.YELLOW,type=COMP.FAT,
               sustain=16,attack=36,level=66,tone=+35)
    f.append(p6)
    p7 = Patch("G FX MILD COMP")
    p7.set_fx(FX.COMP,Color.GREEN,type=COMP.MILD,
               sustain=17,attack=37,level=67,tone=+45)
    f.append(p7)
    f.save()

def make_mod_fx_limiter():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, LIMITER
    from waza_tsl import RATIO, ratio, inf
    f = TSLFile("File with limiter types")
    p1 = Patch("G MOD BOSS LIMITER")
    p1.set_mod(MOD.LIMITER,Color.GREEN,type=LIMITER.BOSS_LIMITER,
               threshold=11,attack=31,release=51,level=81,ratio=RATIO._10to1)
    f.append(p1)
    p2 = Patch("R MOD RACK 160D LIMITER")
    p2.set_mod(MOD.LIMITER,Color.RED,type=LIMITER.RACK_160D,
               threshold=12,attack=32,release=52,level=82,ratio=RATIO._infto1)
    f.append(p2)
    p3 = Patch("Y MOD VTG RACK U LIMITER")
    p3.set_mod(MOD.LIMITER,Color.YELLOW,type=LIMITER.VTG_RACK_U,
               threshold=13,attack=33,release=53,level=83,ratio=RATIO._1p4to1)
    f.append(p3)
    p4 = Patch("G FX VTG RACK U LIMITER")
    p4.set_fx(FX.LIMITER,Color.GREEN,type=LIMITER.VTG_RACK_U,
               threshold=14,attack=34,release=54,level=84,ratio=RATIO._2p6to1)
    f.append(p4)
    p5 = Patch("R FX BOSS LIMITER")
    p5.set_fx(FX.LIMITER,Color.RED,type=LIMITER.BOSS_LIMITER,
               threshold=15,attack=35,release=55,level=85,ratio=RATIO._3p5to1)
    f.append(p5)
    p6 = Patch("Y FX RACK 160D LIMITER")
    p6.set_fx(FX.LIMITER,Color.YELLOW,type=LIMITER.RACK_160D,
               threshold=16,attack=36,release=56,level=86,ratio=RATIO._6to1)
    f.append(p6)
    p7 = Patch("R MOD func LIMITER RACK 160D") # same as p2
    p7.set_mod(MOD.LIMITER,Color.RED,type=LIMITER.RACK_160D,
               threshold=12,attack=32,release=52,level=82,ratio=ratio[inf:1])
    f.append(p7)
    p8 = Patch("R FX func BOSS LIMITER") # same as p5
    p8.set_fx(FX.LIMITER,Color.RED,type=LIMITER.BOSS_LIMITER,
               threshold=15,attack=35,release=55,level=85,ratio=ratio[3.5:1])
    f.append(p8)
    f.save()

def make_mod_fx_graphic_eq():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX
    f = TSLFile("File with graphic eq")
    p1 = Patch("R MOD GRAPHIC EQ")
    p1.set_mod(MOD.GRAPHIC_EQ,Color.RED,level=+20,
               _31hz=-20, _62hz=-16, _125hz=-12, _250hz=-8, _500hz=-4,
               _1khz=0, _2khz=+4, _4khz=+8, _8khz=+12, _16khz=+16)
    f.append(p1)
    p2 = Patch("Y FX GRAPHIC EQ")
    p2.set_fx(FX.GRAPHIC_EQ,Color.YELLOW,level=-20,
               _31hz=+20, _62hz=+16, _125hz=+12, _250hz=+8, _500hz=+4,
               _1khz=0, _2khz=-4, _4khz=-8, _8khz=-12, _16khz=-16)
    f.append(p2)
    f.save()

def make_mod_fx_parametric_eq():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, Q_VALUE, q_value
    from waza_tsl import LOW_CUT, low_cut, MID_FREQ, mid_freq, HIGH_CUT, high_cut
    f = TSLFile("File with parametric eq")
    p1 = Patch("R MOD PARAM EQ enum")
    p1.set_mod(MOD.PARAMETRIC_EQ,Color.RED,level=+3,
               low_cut=LOW_CUT._FLAT,low_gain=-1,
               low_mid_frequency=MID_FREQ._630Hz,low_mid_gain=-4,low_mid_q=Q_VALUE._05,
               high_mid_frequency=MID_FREQ._2p50kHz,high_mid_gain=-5,high_mid_q=Q_VALUE._4,
               high_cut=HIGH_CUT._8kHz,high_gain=+1)
    f.append(p1)
    p2 = Patch("G FX PARAM EQ enum")
    p2.set_fx(FX.PARAMETRIC_EQ,Color.GREEN,level=+2,
               low_cut=LOW_CUT._100Hz,low_gain=-2,
               low_mid_frequency=MID_FREQ._800Hz,low_mid_gain=-5,low_mid_q=Q_VALUE._2,
               high_mid_frequency=MID_FREQ._1p60kHz,high_mid_gain=-4,high_mid_q=Q_VALUE._16,
               high_cut=HIGH_CUT._FLAT,high_gain=+2)
    f.append(p2)
    p3 = Patch("Y MOD PARAM EQ func")
    p3.set_mod(MOD.PARAMETRIC_EQ,Color.YELLOW,level=-3,
               low_cut=low_cut(160),low_gain=+1,
               low_mid_frequency=mid_freq(500),low_mid_gain=+4,low_mid_q=q_value(1),
               high_mid_frequency=mid_freq(2.50e3),high_mid_gain=+5,high_mid_q=q_value(8),
               high_cut=high_cut(8e3),high_gain=-1)
    f.append(p3)
    p4 = Patch("R FX PARAM EQ func")
    p4.set_fx(FX.PARAMETRIC_EQ,Color.RED,level=-2,
               low_cut=low_cut(200),low_gain=+2,
               low_mid_frequency=mid_freq(1e3),low_mid_gain=+3,low_mid_q=q_value(1),
               high_mid_frequency=mid_freq(3.15e3),high_mid_gain=+4,high_mid_q=q_value(8),
               high_cut=high_cut(12.5e3),high_gain=0)
    f.append(p4)
    f.save()

def make_mod_fx_guitar_sim():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, GUITAR_SIM
    f = TSLFile("File with guitar sim")
    p1 = Patch("MOD S->H GUITAR SIM")
    p1.set_mod(MOD.GUITAR_SIM,Color.GREEN,type=GUITAR_SIM.S_H,
               low=-33,high=+22,level=55)
    f.append(p1)
    p2 = Patch("MOD H->HOLLOW GUITAR SIM")
    p2.set_mod(MOD.GUITAR_SIM,Color.RED,type=GUITAR_SIM.H_HOLLOW,
               low=-45,high=-35,level=44,body=66)
    f.append(p2)
    p3 = Patch("FX S->AC GUITAR SIM")
    p3.set_fx(FX.GUITAR_SIM,Color.YELLOW,type=GUITAR_SIM.S_AC,
               low=+33,high=+44,level=55,body=88)
    f.append(p3)
    p4 = Patch("FX P->AC GUITAR SIM")
    p4.set_fx(FX.GUITAR_SIM,Color.GREEN,type=GUITAR_SIM.P_AC,
               low=+44,high=-44,level=25,body=12)
    f.append(p4)
    f.save()

def make_mod_fx_slow_gear():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX
    f = TSLFile("File with slow gear")
    p1 = Patch("R MOD SLOW GEAR")
    p1.set_mod(MOD.SLOW_GEAR,Color.RED,sens=22,rise_time=33,level=44)
    f.append(p1)
    p2 = Patch("Y FX SLOW GEAR")
    p2.set_fx(FX.SLOW_GEAR,Color.YELLOW,sens=55,rise_time=66,level=77)
    f.append(p2)
    p3 = Patch("G FX SLOW GEAR")
    p3.set_fx(FX.SLOW_GEAR,Color.GREEN,sens=88,rise_time=99,level=11)
    f.append(p3)
    f.save()

def make_mod_fx_wave_synth():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, WAVE
    f = TSLFile("File with wave synth")
    p1 = Patch("R MOD WAVE SYNTH")
    p1.set_mod(MOD.WAVE_SYNTH,Color.RED,wave=WAVE.SAW,cutoff=11,resonance=21,
               filter_sens=31,filter_decay=41,filter_depth=51,
               synth_level=61,direct_mix=71)
    f.append(p1)
    p2 = Patch("Y FX WAVE SYNTH")
    p2.set_fx(FX.WAVE_SYNTH,Color.YELLOW,wave=WAVE.SQUARE,cutoff=12,resonance=22,
               filter_sens=32,filter_decay=42,filter_depth=52,
               synth_level=62,direct_mix=72)
    f.append(p2)
    f.save()

def make_mod_fx_octave():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, RANGE
    f = TSLFile("File with octave")
    p1 = Patch("R MOD OCTAVE")
    p1.set_mod(MOD.OCTAVE,Color.RED,
               range=RANGE._2,effect_level=33,direct_mix=4)
    f.append(p1)
    p2 = Patch("Y FX OCTAVE")
    p2.set_fx(FX.OCTAVE,Color.YELLOW,
              range=RANGE._4,effect_level=3,direct_mix=44)
    f.append(p2)
    f.save()

def make_mod_fx_pitch_shifter():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX, VOICE, MODE
    f = TSLFile("File with pitch shifter")
    p1 = Patch("R MOD PITCH SHIFTER")
    p1.set_mod(MOD.PITCH_SHIFTER,Color.RED,voice=VOICE._2,direct_mix=33,
               ps1_mode=MODE.FAST,ps1_pitch=-22,ps1_fine=-44,
               ps1_pre_delay=300,ps1_level=24,ps1_feedback=55,
               ps2_mode=MODE.SLOW,ps2_pitch=+22,ps2_fine=+33,
               ps2_pre_delay=200,ps2_level=43)
    f.append(p1)
    p2 = Patch("Y FX PITCH SHIFTER")
    p2.set_fx(FX.PITCH_SHIFTER,Color.YELLOW,voice=VOICE._1,direct_mix=66,
               ps1_mode=MODE.MONO,ps1_pitch=-12,ps1_fine=+23,
               ps1_pre_delay=100,ps1_level=78,ps1_feedback=99)
    f.append(p2)
    f.save()

def make_mod_fx_harmonist():
    from waza_tsl import TSLFile, Patch, Color, MOD, FX
    from waza_tsl import VOICE, HARMONY, MASTER_KEY
    f = TSLFile("File with harmonist")
    p1 = Patch("R MOD HARMONIST")
    p1.set_mod(MOD.HARMONIST,Color.RED,voice=VOICE._2,
               master_key=MASTER_KEY.A_flat_major,direct_mix=33,
               hr1_harmony=HARMONY.minus_11_th,hr1_pre_delay=100,
               hr1_level=88,hr1_feedback=55,
               hr2_harmony=HARMONY.USER,hr2_level=33,hr2_pre_delay=200,
               hr2_perfect_unison = -24, # A_flat
               hr2_minor_second   = -20, # A
               hr2_major_second   = -16, # B_flat
               hr2_minor_third    = -12, # B
               hr2_major_third    =  -8, # C
               hr2_perfect_fourth =  -4, # D_flat
               hr2_tritone        =  +4, # D
               hr2_perfect_fifth  =  +8, # E_flat
               hr2_minor_sixth    = +12, # E
               hr2_major_sixth    = +16, # F
               hr2_minor_seventh  = +20, # F_sharp
               hr2_major_seventh  = +24, # G
               )
    f.append(p1)
    p2 = Patch("Y FX HARMONIST")
    p2.set_fx(FX.HARMONIST,Color.YELLOW,voice=VOICE._1,
               master_key=MASTER_KEY.C_sharp_minor,direct_mix=33,
               hr1_harmony=HARMONY.USER,hr1_level=44,hr1_pre_delay=299,
               hr1_perfect_unison = -24, # E
               hr1_minor_second   = -20, # F
               hr1_major_second   = -16, # F_sharp
               hr1_minor_third    = -12, # G
               hr1_major_third    =  -8, # A_flat
               hr1_perfect_fourth =  -4, # A
               hr1_tritone        =  +4, # B_flat
               hr1_perfect_fifth  =  +8, # B
               hr1_minor_sixth    = +12, # C
               hr1_major_sixth    = +16, # D_flat
               hr1_minor_seventh  = +20, # D
               hr1_major_seventh  = +24, # E_flat
               hr1_feedback=77)
    f.append(p2)
    f.save()
