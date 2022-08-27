# -*- coding: utf-8 -*-
"""
Created: 2022-08-19
@author: bro

"""

import json
from copy import deepcopy
from enum import Enum

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


class AMP_type(Enum):
    ACOUSTIC =  1
    CLEAN    =  8
    CRUNCH   = 11
    BROWN    = 23
    LEAD     = 24

class Color(Enum):
    GREEN  = 0
    RED    = 1
    YELLOW = 2

class BST_type(Enum):
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

class MOD_type(Enum):
    T_WAH         =  0 # T.WAH
    AUTO_WAH      =  1


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
        if value is None:
            value = CLEAR_DATA[index] # if value is None, use default value
        if index in KNOWN_INDEXES:
            name,case,limits = KNOWN_INDEXES[index]
        else:
            name = "UNKNOWN PARAMETER"
            case = "minmax"
            limits = [0,255] # any byte value
        if case == "listed" and value not in limits:
            raise ValueError(f"Value for {name} must be one of: {limits}")
        elif case == "minmax":
            low,high = limits
            value = min(max(low,value),high)
        elif case == "scaled":
            base,slope,low,high = limits
            value = min(max(low,round(base+slope*value)),high)
        self.data["paramSet"]["User%Patch"][index] = value

    def set_amp(self,amp_type,gain=None,presence=None,volume=None,
                              bass=None,middle=None,treble=None):
        if isinstance(amp_type, AMP_type):
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
        if isinstance(bst_type, BST_type):
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
        if isinstance(mod_type, MOD_type):
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

    def set_fx(self,fx_type,**kw):
        raise NotImplementedError

    def set_reverb(self,reverb_type,**kw):
        raise NotImplementedError

    def set_delay2(self,delay_type,**kw):
        raise NotImplementedError


KNOWN_INDEXES = {
    # AMP:
    81 : ["AMP:TYPE",     "listed", [1,8,11,23,24]],
    82 : ["AMP:GAIN",     "scaled", [20,0.8,20,100]],
    84 : ["AMP:BASS",     "minmax", [0,100]],
    85 : ["AMP:MIDDLE",   "minmax", [0,100]],
    86 : ["AMP:TREBLE",   "minmax", [0,100]],
    87 : ["AMP:PRESENCE", "minmax", [0,100]],
    88 : ["AMP:VOLUME",   "minmax", [0,100]],
    # BST:
    2305 : ["BST:GREEN TYPE",   "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    2306 : ["BST:RED TYPE",     "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    2307 : ["BST:YELLOW TYPE",  "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    2320 : ["BST:COLOR",        "listed", [0,1,2]],
    2325 : ["BST OR MOD",       "listed", [0,1]],
    48   : ["BST:ON/OFF",       "listed", [0,1]],
    49   : ["BST:TYPE",         "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    50   : ["BST:DRIVE",        "minmax", [0,120]],
    51   : ["BST:BOTTOM",       "scaled", [50,1,0,100]],
    52   : ["BST:TONE",         "scaled", [50,1,0,100]],
    53   : ["BST:SOLO SW",      "listed", [0,1]],
    54   : ["BST:SOLO LEVEL",   "minmax", [0,100]],
    55   : ["BST:EFFECT LEVEL", "minmax", [0,100]],
    56   : ["BST:DIRECT MIX",   "minmax", [0,100]],
    # MOD:
    2308 : ["MOD:GREEN TYPE",  "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2309 : ["MOD:RED TYPE",    "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2310 : ["MOD:YELLOW TYPE", "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2321 : ["MOD:COLOR",       "listed", [0,1,2]],
    192  : ["MOD:ON/OFF",      "listed", [0,1]],
    193  : ["MOD:TYPE",        "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    # 2325 "BST OR MOD" is located under BST
    # MOD:T.WAH:
    204  : ["MOD:T.WAH:MODE",         "listed", [0,1]], # 0=LPF, 1=BPF
    205  : ["MOD:T.WAH:POLARITY",     "listed", [0,1]], # 0=DOWN, 1=UP
    206  : ["MOD:T.WAH:SENS",         "minmax", [0,100]],
    207  : ["MOD:T.WAH:FREQUENCY",    "minmax", [0,100]],
    208  : ["MOD:T.WAH:PEAK",         "minmax", [0,100]],
    209  : ["MOD:T.WAH:DIRECT MIX",   "minmax", [0,100]],
    210  : ["MOD:T.WAH:EFFECT LEVEL", "minmax", [0,100]],
    # MOD:AUTO WAH:
    212  : ["MOD:AUTO WAH:MODE",         "listed", [0,1]], # 0=LPF, 1=BPF
    213  : ["MOD:AUTO WAH:FREQUENCY",    "minmax", [0,100]],
    214  : ["MOD:AUTO WAH:PEAK",         "minmax", [0,100]],
    215  : ["MOD:AUTO WAH:RATE",         "minmax", [0,100]],
    216  : ["MOD:AUTO WAH:DEPTH",        "minmax", [0,100]],
    217  : ["MOD:AUTO WAH:DIRECT MIX",   "minmax", [0,100]],
    218  : ["MOD:AUTO WAH:EFFECT LEVEL", "minmax", [0,100]],
}

# Make a mapping of parameter names to indexes, grouped by subsystem
# translate space (' '), dash ('-'), dot ('.') and '/' to underscore ('_')
as_identifier = str.maketrans({' ':'_','-':'_','.':'_','/':'_'})
PARAMETERS = dict()
for index,(subsystems,_,_) in KNOWN_INDEXES.items():
    subsystems = subsystems.split(':')
    current = PARAMETERS
    for subsystem in subsystems[:-1]:
        name = subsystem.translate(as_identifier)
        if name not in current:
            current[name] = dict()
        current = current[name]
    # convert the actual parameter names to lower case:
    param = subsystems[-1].lower().translate(as_identifier)
    current[param] = index
