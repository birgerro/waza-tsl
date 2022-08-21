# -*- coding: utf-8 -*-
"""
Created: 2022-08-19
@author: bro

"""

import json
from copy import deepcopy

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
        if value is None:
            value = CLEAR_DATA[index]
        self.data["paramSet"]["User%Patch"][index] = value

    def set_amp(self,amp_type,gain=None,presence=None,volume=None,
                              bass=None,middle=None,treble=None):
        raise NotImplementedError

    def set_bst(self,bst_type,**kw):
        raise NotImplementedError

    def set_mod(self,mod_type,**kw):
        raise NotImplementedError

    def set_delay(self,delay_type,**kw):
        raise NotImplementedError

    def set_fx(self,fx_type,**kw):
        raise NotImplementedError

    def set_reverb(self,reverb_type,**kw):
        raise NotImplementedError

    def set_delay2(self,delay_type,**kw):
        raise NotImplementedError
