# -*- coding: utf-8 -*-
"""
Created: 2022-08-19
@author: bro

"""

import json
from copy import deepcopy
from enum import Enum, IntEnum
from math import log10, log2
from known_indexes import KNOWN_INDEXES, PARAMETERS

# Clear patch is the default setting after CLEAR from the app's WRITE menu
CLEAR_PATCH = "clear_patch.json" # Patch with binary data as ints
CLEAR_DATA = json.load(open(CLEAR_PATCH,'r'))["paramSet"]["User%Patch"]

class TSLFile:
    def __init__(self,name="New liveset"):
        self.name = name
        self.content = dict()
        self.content["name"] = name
        self.content["formatRev"] = "0000"
        self.content["device"] = "WAZA-AIR"
        self.content["data"] = [[]]
        self.patches = list()
    def append(self,patch):
        self.patches.append(patch)
    def save(self,filename=None):
        if filename is None:
            filename = self.name + ".tsl"
        filedata = deepcopy(self.content)
        for patch in self.patches:
            patchdata = deepcopy(patch.data)
            values = patchdata["paramSet"]["User%Patch"]
            for i in range(len(values)):
                values[i] = f"{values[i]:02X}"
            filedata["data"][0].append(patchdata)
        json.dump(filedata,open(filename,'w'),separators=(',',':') )

class Patch:
    def __init__(self,name="New patch"):
        self.data = json.load(open(CLEAR_PATCH,'r'))
        self.set_name(name)
    def set_name(self,name):
        for i,c in enumerate(name.ljust(16)[:16]):
            self[i] = ord(c)
    def get_name(self):
        name = self[:16]
        return bytes(name).decode()
    name = property(get_name,set_name)

    def __getitem__(self,index):
        return self.data["paramSet"]["User%Patch"][index]
    def __setitem__(self,index,value):
        if index in KNOWN_INDEXES:
            name,case,limits = KNOWN_INDEXES[index]
        else:
            name = "UNKNOWN PARAMETER"
            case = "minmax"
            limits = [0,255] # any byte value
        if value is None:
            # if value is None, use default value
            self.data["paramSet"]["User%Patch"][index] = CLEAR_DATA[index]
            if case == "2bytes":
                self.data["paramSet"]["User%Patch"][index+1] = CLEAR_DATA[index+1]
            return # do not change default value
        if case == "listed" and value not in limits:
            raise ValueError(f"Value for {name} must be one of: {limits}")
        elif case == "minmax":
            low,high = limits
            value = min(max(low,value),high)
        elif case == "scaled":
            base,slope,low,high = limits
            value = min(max(low,round(base+slope*value)),high)
        elif case == "2bytes":
            low,high = limits
            split = divmod(min(max(low,value),high),128)
            self.data["paramSet"]["User%Patch"][index:index+2] = split
            return
        self.data["paramSet"]["User%Patch"][index] = value

    def set_amp(self,amp_type,gain=None,presence=None,volume=None,
                              bass=None,middle=None,treble=None):
        if isinstance(amp_type, AMP):
            self[81] = amp_type.value
        else:
            raise TypeError(f"amp_type must be an AMP_type, not '{type(amp_type)}'")
        self[82] = gain
        self[84] = bass
        self[85] = middle
        self[86] = treble
        self[87] = presence
        self[88] = volume

    def set_bst(self,bst_type,color,drive=None,bottom=None,tone=None,
                solo_sw=None,solo_level=None,effect_level=None,direct_mix=None):
        if isinstance(bst_type, BST):
            self[49] = bst_type.value
        else:
            raise TypeError(f"bst_type must be an BST_type, not '{type(bst_type)}'")
        self[48] = 1 # BST on
        self[50] = drive
        self[51] = bottom
        self[52] = tone
        self[53] = solo_sw
        self[54] = solo_level
        self[55] = effect_level
        self[56] = direct_mix
        index = 2305 + color.value
        self[index] = bst_type.value
        self[2320] = color.value
        self[2325] = 0 # BST, not MOD

    def set_mod(self,mod_type,color,**kw):
        if isinstance(mod_type, MOD):
            self[193] = mod_type.value
        else:
            raise TypeError(f"mod_type must be an MOD_type, not '{type(mod_type)}'")
        params = PARAMETERS["MOD"][mod_type.name]
        for param,index in params.items():
            value = kw.get(param) # params not listed in kw get set to default (value=None)
            self[index] = value
        self[192] = 1 # MOD on
        index = 2308 + color.value
        self[index] = mod_type.value
        self[2321] = color.value
        self[2325] = 1 # MOD, not BST

    def set_delay(self,delay_type,**kw):
        raise NotImplementedError

    def set_fx(self,fx_type,color,**kw):
        if isinstance(fx_type, FX):
            self[461] = fx_type.value
        else:
            raise TypeError(f"fx_type must be an FX_type, not '{type(fx_type)}'")
        params = PARAMETERS["FX"][fx_type.name]
        for param,index in params.items():
            value = kw.get(param) # params not listed in kw get set to default (value=None)
            self[index] = value
        self[460] = 1 # FX on
        index = 2314 + color.value
        self[index] = fx_type.value
        self[2323] = color.value
        self[2326] = 1 # FX, not DELAY1

    def set_reverb(self,reverb_type,**kw):
        raise NotImplementedError

    def set_delay2(self,delay_type,**kw):
        raise NotImplementedError


class AMP(Enum):
    ACOUSTIC =  1
    CLEAN    =  8
    CRUNCH   = 11
    BROWN    = 23
    LEAD     = 24

class Color(Enum):
    GREEN  = 0
    RED    = 1
    YELLOW = 2

class BST(Enum):
    MID_BOOST    =  0
    CLEAN_BOOST  =  1
    TREBLE_BOOST =  2
    CRUNCH_OD    =  3
    NATURAL_OD   =  4
    WARM_OD      =  5
    FAT_DS       =  6
    METAL_DS     =  8
    OCT_FUZZ     =  9
    BLUES_DRIVE  = 10
    OVERDRIVE    = 11
    T_SCREAM     = 12 # T-SCREAM
    TURBO_OD     = 13
    DISTORTION   = 14
    RAT          = 15
    GUV_DS       = 16
    DSTPLUS      = 17 # DST+
    METAL_ZONE   = 18
    SIXTIES_FUZZ = 19 # '60s FUZZ
    MUFF_FUZZ    = 20

class MOD(Enum):
    T_WAH         =  0 # T.WAH
    AUTO_WAH      =  1
    PEDAL_WAH     =  2
    COMP          =  3
    LIMITER       =  4
    GRAPHIC_EQ    =  6
    PARAMETRIC_EQ =  7
    GUITAR_SIM    =  9
    SLOW_GEAR     = 10
    WAVE_SYNTH    = 12
    OCTAVE        = 14
    PITCH_SHIFTER = 15
    HARMONIST     = 16
    AC_PROCESSOR  = 18
    PHASER        = 19
    FLANGER       = 20
    TREMOLO       = 21
    ROTARY        = 22

FX = MOD # alternate name

class PEDAL(IntEnum):
    CRY_WAH   = 0
    VO_WAH    = 1
    FAT_WAH   = 2
    LIGHT_WAH = 3
    SEVEN_WAH = 4 # 7STRING WAH
    RESO_WAH  = 5

class COMP(IntEnum):
    BOSS_COMP = 0
    HI_BAND   = 1 # HI-BAND
    LIGHT     = 2
    D_COMP    = 3 # D-COMP
    ORANGE    = 4
    FAT       = 5
    MILD      = 6

class LIMITER(IntEnum):
    BOSS_LIMITER = 0
    RACK_160D    = 1
    VTG_RACK_U   = 2

class RATIO(IntEnum): # For LIMITER
    _1to1   =  0 # 1:1
    _1p2to1 =  1 # 1.2:1
    _1p4to1 =  2 # 1.4:1
    _1p6to1 =  3 # 1.6:1
    _1p8to1 =  4 # 1.8:1
    _2to1   =  5 # 2:1
    _2p3to1 =  6 # 2.3:1
    _2p6to1 =  7 # 2.6:1
    _3to1   =  8 # 3:1
    _3p5to1 =  9 # 3.5:1
    _4to1   = 10 # 4:1
    _5to1   = 11 # 5:1
    _6to1   = 12 # 6:1
    _8to1   = 13 # 8:1
    _10to1  = 14 # 10:1
    _12to1  = 15 # 12:1
    _20to1  = 16 # 20:1
    _infto1 = 17 # inf:1
# alternatively, use function to get closest value to a numerical frequency:
class ratio:
    def __getitem__(self,ratio):
        if type(ratio) is not slice:
            raise TypeError("Please use n:1 syntax")
        n = ratio.start
        d = ratio.stop
        if d != 1:
            n /= d
        if n < 1:
            return 0
        numerators = [1,1.2,1.4,1.6,1.8,2,2.3,2.6,3,3.5,4,5,6,8,10,12,20]
        for i in range(len(numerators)-1):
            v1,v2 = numerators[i:i+2]
            if v1 <= n <= v2:
                if (n-v1)/(v2-v1) < 0.5:
                    return i
                else:
                    return i+1
        # ratio > 20:1
        return 17
ratio = ratio()
inf = float("inf")
# Usage: ratio[2.3:1]

class Q_VALUE(IntEnum): # For PARAMETRIC EQ
    _05 = 0 # 0.5
    _1  = 1 # 1
    _2  = 2 # 2
    _4  = 3 # 4
    _8  = 4 # 8
    _16 = 5 # 16
# alternatively, use function to get closest value to a numerical frequency:
def q_value(value):
    if value < 0.5:
        return 0
    elif value > 16:
        return 5
    else:
        return round(log2(value))+1

class LOW_CUT(IntEnum): # For PARAMETRIC EQ
    FLAT     =  0
    _FLAT    =  0
    _20Hz    =  1 # 20.0 Hz
    _25Hz    =  2 # 25.0 Hz
    _31p5Hz  =  3 # 31.5 Hz
    _40Hz    =  4 # 40.0 Hz
    _50Hz    =  5 # 50.0 Hz
    _63Hz    =  6 # 63.0 Hz
    _80Hz    =  7 # 80.0 Hz
    _100Hz   =  8 # 100 Hz
    _125Hz   =  9 # 125 Hz
    _160Hz   = 10 # 160 Hz
    _200Hz   = 11 # 200 Hz
    _250Hz   = 12 # 250 Hz
    _315Hz   = 13 # 315 Hz
    _400Hz   = 14 # 400 Hz
    _500Hz   = 15 # 500 Hz
    _630Hz   = 16 # 630 Hz
    _800Hz   = 17 # 800 Hz
# alternatively, use function to get closest value to a numerical frequency:
def low_cut(frequency):
    if frequency < 20:
        return 0   # FLAT
    elif frequency > 800:
        return 17  # 800Hz
    else:
        return  round(log10(frequency)*10) - 12

class MID_FREQ(IntEnum): # For PARAMETRIC EQ
    _20Hz    =  0 # 20.0 Hz
    _25Hz    =  1 # 25.0 Hz
    _31p5Hz  =  2 # 31.5 Hz
    _40Hz    =  3 # 40.0 Hz
    _50Hz    =  4 # 50.0 Hz
    _63Hz    =  5 # 63.0 Hz
    _80Hz    =  6 # 80.0 Hz
    _100Hz   =  7 # 100 Hz
    _125Hz   =  8 # 125 Hz
    _160Hz   =  9 # 160 Hz
    _200Hz   = 10 # 200 Hz
    _250Hz   = 11 # 250 Hz
    _315Hz   = 12 # 315 Hz
    _400Hz   = 13 # 400 Hz
    _500Hz   = 14 # 500 Hz
    _630Hz   = 15 # 630 Hz
    _800Hz   = 16 # 800 Hz
    _1kHz    = 17 # 1.00 kHz
    _1p25kHz = 18 # 1.25 kHz
    _1p60kHz = 19 # 1.60 kHz
    _2kHz    = 20 # 2.00 kHz
    _2p50kHz = 21 # 2.50 kHz
    _3p15kHz = 22 # 3.15 kHz
    _4kHz    = 23 # 4.00 kHz
    _5kHz    = 24 # 5.00 kHz
    _6p30kHz = 25 # 6.30 kHz
    _8kHz    = 26 # 8.00 kHz
    _10kHz   = 27 # 10.0 kHz
# alternatively, use function to get closest value to a numerical frequency:
def mid_freq(frequency):
    if frequency < 20:
        return 0   # 20Hz
    elif frequency > 10e3:
        return 27  # 10kHz
    else:
        return  round(log10(frequency)*10) - 13

class HIGH_CUT(IntEnum): # For PARAMETRIC EQ
    _630Hz   =  0 # 630 Hz
    _800Hz   =  1 # 800 Hz
    _1kHz    =  2 # 1.00 kHz
    _1p25kHz =  3 # 1.25 kHz
    _1p60kHz =  4 # 1.60 kHz
    _2kHz    =  5 # 2.00 kHz
    _2p50kHz =  6 # 2.50 kHz
    _3p15kHz =  7 # 3.15 kHz
    _4kHz    =  8 # 4.00 kHz
    _5kHz    =  9 # 5.00 kHz
    _6p30kHz = 10 # 6.30 kHz
    _8kHz    = 11 # 8.00 kHz
    _10kHz   = 12 # 10.0 kHz
    _12p5kHz = 13 # 12.5 kHz
    _FLAT    = 14
    FLAT     = 14
# alternatively, use function to get closest value to a numerical frequency:
def high_cut(frequency):
    if frequency < 630:
        return 0   # 630Hz
    elif frequency > 12.5e3:
        return 14  # FLAT
    else:
        return  round(log10(frequency)*10) - 28

class GUITAR_SIM(IntEnum):
    S_H      = 0 # S->H
    H_S      = 1 # H->S
    H_HF     = 2 # H->HF
    S_HOLLOW = 3 # S->HOLLOW
    H_HOLLOW = 4 # H->HOLLOW
    S_AC     = 5 # S->AC
    H_AC     = 6 # H->AC
    P_AC     = 7 # P->AC

class WAVE(IntEnum): # For WAVE SYNTH
    SAW    = 0
    SQUARE = 1

class RANGE(IntEnum): # For OCTAVE
    _1 = 0
    _2 = 1
    _3 = 2
    _4 = 3

class VOICE(IntEnum): # For PITCH SHIFTER and HARMONIST
    _1 = 0
    _2 = 1

class MODE(IntEnum): # For PITCH SHIFTER
    FAST   = 0
    MEDIUM = 1
    SLOW   = 2
    MONO   = 3

class HARMONY(IntEnum): # For HARMONIST
    minus_2_oct =  0 # -2oct
    minus_14_th =  1 # -14th
    minus_13_th =  2 # -13th
    minus_12_th =  3 # -12th
    minus_11_th =  4 # -11th
    minus_10_th =  5 # -10th
    minus_9_th  =  6 # -9th
    minus_1_oct =  7 # -1oct
    minus_7_th  =  8 # -7th
    minus_6_th  =  9 # -6th
    minus_5_th  = 10 # -5th
    minus_4_th  = 11 # -4th
    minus_3_rd  = 12 # -3rd
    minus_2_nd  = 13 # -2nd
    UNISON      = 14
    plus_2_nd   = 15 # +2nd
    plus_3_rd   = 16 # +3rd
    plus_4_th   = 17 # +4th
    plus_5_th   = 18 # +5th
    plus_6_th   = 19 # +6th
    plus_7_th   = 20 # +7th
    plus_1_oct  = 21 # +1oct
    plus_9_th   = 22 # +9th
    plus_10_th  = 23 # +10th
    plus_11_th  = 24 # +11th
    plus_12_th  = 25 # +12th
    plus_13_th  = 26 # +13th
    plus_14_th  = 27 # +14th
    plus_2_oct  = 28 # +2oct
    USER        = 29

class MASTER_KEY(IntEnum): # For HARMONIST
    # Major keys:
    C_major       =  0 # C  (Am)
    D_flat_major  =  1 # Db (Bbm)
    D_major       =  2 # D  (Bm)
    E_flat_major  =  3 # Eb (Cm)
    E_major       =  4 # E  (C#m)
    F_major       =  5 # F  (Dm)
    F_sharp_major =  6 # F# (D#m)
    G_major       =  7 # G  (Em)
    A_flat_major  =  8 # Ab (Fm)
    A_major       =  9 # A  (F#m)
    B_flat_major  = 10 # Bb (Gm)
    B_major       = 11 # B  (G#m)
    # Minor keys:
    A_minor       =  0 # C  (Am)
    B_flat_minor  =  1 # Db (Bbm)
    B_minor       =  2 # D  (Bm)
    C_minor       =  3 # Eb (Cm)
    C_sharp_minor =  4 # E  (C#m)
    D_minor       =  5 # F  (Dm)
    D_sharp_minor =  6 # F# (D#m)
    E_minor       =  7 # G  (Em)
    F_minor       =  8 # Ab (Fm)
    F_sharp_minor =  9 # A  (F#m)
    G_minor       = 10 # Bb (Gm)
    G_sharp_minor = 11 # B  (G#m)

def user_harmony(master_key,hr="hr1",
                 C=0,D_flat=0,D=0,E_flat=0,E=0,F=0,
                 F_sharp=0,G=0,A_flat=0,A=0,B_flat=0,B=0):
    parameters = [
        "_perfect_unison",
        "_minor_second",
        "_major_second",
        "_minor_third",
        "_major_third",
        "_perfect_fourth",
        "_tritone",
        "_perfect_fifth",
        "_minor_sixth",
        "_major_sixth",
        "_minor_seventh",
        "_major_seventh",
        ]
    output = {"master_key" : master_key}
    output[hr+parameters[( 0-master_key)%12]] = C
    output[hr+parameters[( 1-master_key)%12]] = D_flat
    output[hr+parameters[( 2-master_key)%12]] = D
    output[hr+parameters[( 3-master_key)%12]] = E_flat
    output[hr+parameters[( 4-master_key)%12]] = E
    output[hr+parameters[( 5-master_key)%12]] = F
    output[hr+parameters[( 6-master_key)%12]] = F_sharp
    output[hr+parameters[( 7-master_key)%12]] = G
    output[hr+parameters[( 8-master_key)%12]] = A_flat
    output[hr+parameters[( 9-master_key)%12]] = A
    output[hr+parameters[(10-master_key)%12]] = B_flat
    output[hr+parameters[(11-master_key)%12]] = B
    return output

class AC_PROCESSOR(IntEnum):
    SMALL  = 0
    MEDIUM = 1
    BRIGHT = 2
    POWER  = 3

class PHASER(IntEnum):
    _4STAGE  = 0
    _8STAGE  = 1
    _12STAGE = 2
    BiPHASE  = 3

def step_rate(value):
    if isinstance(value,int):
        return value+1
    if isinstance(value,str) and value.upper() == "OFF":
        return 0
    if value is False:
        return 0
    raise ValueError("step_rate must be 0--100 or the string \"OFF\"")

class FL_LOW_CUT(IntEnum):
    FLAT = 0
    _55Hz = 1
    _110Hz = 2
    _165Hz = 3
    _200Hz = 4
    _280Hz = 5
    _340Hz = 6
    _400Hz = 7
    _500Hz = 8
    _630Hz = 9
    _800Hz = 10
