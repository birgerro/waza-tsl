#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Split out on 2022-09-09

@author: birger
"""

KNOWN_INDEXES = {
    # AMP:
    81 : ["AMP|TYPE",     "listed", [1,8,11,23,24]],
    82 : ["AMP|GAIN",     "scaled", [20,0.8,20,100]],
    84 : ["AMP|BASS",     "minmax", [0,100]],
    85 : ["AMP|MIDDLE",   "minmax", [0,100]],
    86 : ["AMP|TREBLE",   "minmax", [0,100]],
    87 : ["AMP|PRESENCE", "minmax", [0,100]],
    88 : ["AMP|VOLUME",   "minmax", [0,100]],
    # BST:
    2305 : ["BST|GREEN TYPE",   "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    2306 : ["BST|RED TYPE",     "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    2307 : ["BST|YELLOW TYPE",  "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    2320 : ["BST|COLOR",        "listed", [0,1,2]],
    2325 : ["BST OR MOD",       "listed", [0,1]],
    48   : ["BST|ON/OFF",       "listed", [0,1]],
    49   : ["BST|TYPE",         "listed", [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]],
    50   : ["BST|DRIVE",        "minmax", [0,120]],
    51   : ["BST|BOTTOM",       "scaled", [50,1,0,100]],
    52   : ["BST|TONE",         "scaled", [50,1,0,100]],
    53   : ["BST|SOLO SW",      "listed", [0,1]],
    54   : ["BST|SOLO LEVEL",   "minmax", [0,100]],
    55   : ["BST|EFFECT LEVEL", "minmax", [0,100]],
    56   : ["BST|DIRECT MIX",   "minmax", [0,100]],
    # MOD:
    2308 : ["MOD|GREEN TYPE",  "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2309 : ["MOD|RED TYPE",    "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2310 : ["MOD|YELLOW TYPE", "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2321 : ["MOD|COLOR",       "listed", [0,1,2]],
    192  : ["MOD|ON/OFF",      "listed", [0,1]],
    193  : ["MOD|TYPE",        "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    # 2325 "BST OR MOD" is located under BST
    # MOD|T.WAH:
    204  : ["MOD|T.WAH|MODE",         "listed", [0,1]], # 0=LPF, 1=BPF
    205  : ["MOD|T.WAH|POLARITY",     "listed", [0,1]], # 0=DOWN, 1=UP
    206  : ["MOD|T.WAH|SENS",         "minmax", [0,100]],
    207  : ["MOD|T.WAH|FREQUENCY",    "minmax", [0,100]],
    208  : ["MOD|T.WAH|PEAK",         "minmax", [0,100]],
    209  : ["MOD|T.WAH|DIRECT MIX",   "minmax", [0,100]],
    210  : ["MOD|T.WAH|EFFECT LEVEL", "minmax", [0,100]],
    # MOD|AUTO WAH:
    212  : ["MOD|AUTO WAH|MODE",         "listed", [0,1]], # 0=LPF, 1=BPF
    213  : ["MOD|AUTO WAH|FREQUENCY",    "minmax", [0,100]],
    214  : ["MOD|AUTO WAH|PEAK",         "minmax", [0,100]],
    215  : ["MOD|AUTO WAH|RATE",         "minmax", [0,100]],
    216  : ["MOD|AUTO WAH|DEPTH",        "minmax", [0,100]],
    217  : ["MOD|AUTO WAH|DIRECT MIX",   "minmax", [0,100]],
    218  : ["MOD|AUTO WAH|EFFECT LEVEL", "minmax", [0,100]],
    # MOD|PEDAL WAH:
    220 : ["MOD|PEDAL WAH|TYPE",           "listed", [0,1,2,3,4,5]],
    221 : ["MOD|PEDAL WAH|PEDAL POSITION", "minmax", [0,100]],
    222 : ["MOD|PEDAL WAH|PEDAL MIN",      "minmax", [0,100]],
    223 : ["MOD|PEDAL WAH|PEDAL MAX",      "minmax", [0,100]],
    224 : ["MOD|PEDAL WAH|EFFECT LEVEL",   "minmax", [0,100]],
    225 : ["MOD|PEDAL WAH|DIRECT MIX",     "minmax", [0,100]],
    # MOD|COMP:
    227 : ["MOD|COMP|TYPE",    "listed", [0,1,2,3,4,5,6]],
    228 : ["MOD|COMP|SUSTAIN", "minmax", [0,100]],
    229 : ["MOD|COMP|ATTACK",  "minmax", [0,100]],
    230 : ["MOD|COMP|TONE",    "scaled", [50,1,0,100]], # Input: -50 -- +50
    231 : ["MOD|COMP|LEVEL",   "minmax", [0,100]],
    # MOD|LIMITER:
    233 : ["MOD|LIMITER|TYPE",      "listed", [0,1,2]],
    234 : ["MOD|LIMITER|ATTACK",    "minmax", [0,100]],
    235 : ["MOD|LIMITER|THRESHOLD", "minmax", [0,100]],
    236 : ["MOD|LIMITER|RATIO",     "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    237 : ["MOD|LIMITER|RELEASE",   "minmax", [0,100]],
    238 : ["MOD|LIMITER|LEVEL",     "minmax", [0,100]],
    # MOD|GRAPHIC EQ:
    240 : ["MOD|GRAPHIC EQ|31Hz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    241 : ["MOD|GRAPHIC EQ|62Hz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    242 : ["MOD|GRAPHIC EQ|125Hz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    243 : ["MOD|GRAPHIC EQ|250Hz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    244 : ["MOD|GRAPHIC EQ|500Hz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    245 : ["MOD|GRAPHIC EQ|1kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    246 : ["MOD|GRAPHIC EQ|2kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    247 : ["MOD|GRAPHIC EQ|4kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    248 : ["MOD|GRAPHIC EQ|8kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    249 : ["MOD|GRAPHIC EQ|16kHz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    250 : ["MOD|GRAPHIC EQ|LEVEL",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    # MOD|PARAMETRIC EQ:
    252 : ["MOD|PARAMETRIC EQ|LOW CUT",            "minmax", [0,17]],
    253 : ["MOD|PARAMETRIC EQ|LOW GAIN",           "scaled", [20,1,0,40]], # Input: -20 -- +20
    254 : ["MOD|PARAMETRIC EQ|LOW MID FREQUENCY",  "minmax", [0,27]],
    255 : ["MOD|PARAMETRIC EQ|LOW MID Q",          "listed", [0,1,2,3,4,5]],
    256 : ["MOD|PARAMETRIC EQ|LOW MID GAIN",       "scaled", [20,1,0,40]], # Input: -20 -- +20
    257 : ["MOD|PARAMETRIC EQ|HIGH MID FREQUENCY", "minmax", [0,27]],
    258 : ["MOD|PARAMETRIC EQ|HIGH MID Q",         "listed", [0,1,2,3,4,5]],
    259 : ["MOD|PARAMETRIC EQ|HIGH MID GAIN",      "scaled", [20,1,0,40]], # Input: -20 -- +20
    260 : ["MOD|PARAMETRIC EQ|HIGH GAIN",          "scaled", [20,1,0,40]], # Input: -20 -- +20
    261 : ["MOD|PARAMETRIC EQ|HIGH CUT",           "minmax", [0,14]],
    262 : ["MOD|PARAMETRIC EQ|LEVEL",              "scaled", [20,1,0,40]], # Input: -20 -- +20
    # MOD|GUITAR SIM:
    270 : ["MOD|GUITAR SIM|TYPE",  "listed", [0,1,2,3,4,5,6,7]],
    271 : ["MOD|GUITAR SIM|LOW",   "scaled", [50,1,0,100]], # Input: -50 -- +50
    272 : ["MOD|GUITAR SIM|HIGH",  "scaled", [50,1,0,100]], # Input: -50 -- +50
    273 : ["MOD|GUITAR SIM|LEVEL", "minmax", [0,100]],
    274 : ["MOD|GUITAR SIM|BODY",  "minmax", [0,100]],
    # MOD|SLOW GEAR:
    276 : ["MOD|SLOW GEAR|SENS",      "minmax", [0,100]],
    277 : ["MOD|SLOW GEAR|RISE TIME", "minmax", [0,100]],
    278 : ["MOD|SLOW GEAR|LEVEL",     "minmax", [0,100]],
    # MOD|WAVE SYNTH:
    288 : ["MOD|WAVE SYNTH|WAVE",         "listed", [0,1]],
    289 : ["MOD|WAVE SYNTH|CUTOFF",       "minmax", [0,100]],
    290 : ["MOD|WAVE SYNTH|RESONANCE",    "minmax", [0,100]],
    291 : ["MOD|WAVE SYNTH|FILTER SENS",  "minmax", [0,100]],
    292 : ["MOD|WAVE SYNTH|FILTER DECAY", "minmax", [0,100]],
    293 : ["MOD|WAVE SYNTH|FILTER DEPTH", "minmax", [0,100]],
    294 : ["MOD|WAVE SYNTH|SYNTH LEVEL",  "minmax", [0,100]],
    295 : ["MOD|WAVE SYNTH|DIRECT MIX",   "minmax", [0,100]],
    # MOD|OCTAVE:
    305 : ["MOD|OCTAVE|RANGE",        "listed", [0,1,2,3]],
    306 : ["MOD|OCTAVE|EFFECT LEVEL", "minmax", [0,100]],
    307 : ["MOD|OCTAVE|DIRECT MIX",   "minmax", [0,100]],
    # MOD|PITCH SHIFTER:
    309 : ["MOD|PITCH SHIFTER|VOICE",         "listed", [0,1]],
    310 : ["MOD|PITCH SHIFTER|PS1:MODE",      "listed", [0,1,2,3]],
    311 : ["MOD|PITCH SHIFTER|PS1:PITCH",     "scaled", [24,1,0,48]],  # Input: -24 -- +24
    312 : ["MOD|PITCH SHIFTER|PS1:FINE",      "scaled", [50,1,0,100]], # Input: -50 -- +50
    313 : ["MOD|PITCH SHIFTER|PS1:PRE DELAY", "2bytes", [0,300]],
    315 : ["MOD|PITCH SHIFTER|PS1:LEVEL",     "minmax", [0,100]],
    316 : ["MOD|PITCH SHIFTER|PS2:MODE",      "listed", [0,1,2,3]],
    317 : ["MOD|PITCH SHIFTER|PS2:PITCH",     "scaled", [24,1,0,48]],  # Input: -24 -- +24
    318 : ["MOD|PITCH SHIFTER|PS2:FINE",      "scaled", [50,1,0,100]], # Input: -50 -- +50
    319 : ["MOD|PITCH SHIFTER|PS2:PRE DELAY", "2bytes", [0,300]],
    321 : ["MOD|PITCH SHIFTER|PS2:LEVEL",     "minmax", [0,100]],
    322 : ["MOD|PITCH SHIFTER|PS1:FEEDBACK",  "minmax", [0,100]],
    323 : ["MOD|PITCH SHIFTER|DIRECT MIX",    "minmax", [0,100]],
    # MOD|HARMONIST:
    325 : ["MOD|HARMONIST|VOICE",              "listed", [0,1]],
    326 : ["MOD|HARMONIST|HR1:HARMONY",        "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                                                          17,18,19,20,21,22,23,24,25,26,27,28,29]],
    327 : ["MOD|HARMONIST|HR1:PRE DELAY",      "2bytes", [0,300]],
    329 : ["MOD|HARMONIST|HR1:LEVEL",          "minmax", [0,100]],
    330 : ["MOD|HARMONIST|HR2:HARMONY",        "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                                                          17,18,19,20,21,22,23,24,25,26,27,28,29]],
    331 : ["MOD|HARMONIST|HR2:PRE DELAY",      "2bytes", [0,300]],
    333 : ["MOD|HARMONIST|HR2:LEVEL",          "minmax", [0,100]],
    334 : ["MOD|HARMONIST|HR1:FEEDBACK",       "minmax", [0,100]],
    335 : ["MOD|HARMONIST|DIRECT MIX",         "minmax", [0,100]],
    336 : ["MOD|HARMONIST|HR1:MAJOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    337 : ["MOD|HARMONIST|HR1:MINOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    338 : ["MOD|HARMONIST|HR1:MAJOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    339 : ["MOD|HARMONIST|HR1:PERFECT UNISON", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    340 : ["MOD|HARMONIST|HR1:MINOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    341 : ["MOD|HARMONIST|HR1:MAJOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    342 : ["MOD|HARMONIST|HR1:MINOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    343 : ["MOD|HARMONIST|HR1:MAJOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    344 : ["MOD|HARMONIST|HR1:PERFECT FOURTH", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    345 : ["MOD|HARMONIST|HR1:TRITONE",        "scaled", [24,1,0,48]],  # Input: -24 -- +24
    346 : ["MOD|HARMONIST|HR1:PERFECT FIFTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    347 : ["MOD|HARMONIST|HR1:MINOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    348 : ["MOD|HARMONIST|HR2:MAJOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    349 : ["MOD|HARMONIST|HR2:MINOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    350 : ["MOD|HARMONIST|HR2:MAJOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    351 : ["MOD|HARMONIST|HR2:PERFECT UNISON", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    352 : ["MOD|HARMONIST|HR2:MINOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    353 : ["MOD|HARMONIST|HR2:MAJOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    354 : ["MOD|HARMONIST|HR2:MINOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    355 : ["MOD|HARMONIST|HR2:MAJOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    356 : ["MOD|HARMONIST|HR2:PERFECT FOURTH", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    357 : ["MOD|HARMONIST|HR2:TRITONE",        "scaled", [24,1,0,48]],  # Input: -24 -- +24
    358 : ["MOD|HARMONIST|HR2:PERFECT FIFTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    359 : ["MOD|HARMONIST|HR2:MINOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    # MASTER KEY is a global parameter (?)
    920 : ["MASTER KEY",                  "listed", [0,1,2,3,4,5,6,7,8,9,10,11]],
    # MOD|AC.PROCESSOR:
    365 : ["MOD|AC.PROCESSOR|TYPE",             "listed", [0,1,2,3]],
    366 : ["MOD|AC.PROCESSOR|BASS",             "scaled", [50,1,0,100]], # Input: -50 -- +50
    367 : ["MOD|AC.PROCESSOR|MIDDLE",           "scaled", [50,1,0,100]], # Input: -50 -- +50
    368 : ["MOD|AC.PROCESSOR|MIDDLE FREQUENCY", "minmax", [0,27]],
    369 : ["MOD|AC.PROCESSOR|TREBLE",           "scaled", [50,1,0,100]], # Input: -50 -- +50
    370 : ["MOD|AC.PROCESSOR|PRESENCE",         "scaled", [50,1,0,100]], # Input: -50 -- +50
    371 : ["MOD|AC.PROCESSOR|LEVEL",            "minmax", [0,100]],
    # MOD|PHASER:
    373 : ["MOD|PHASER|TYPE",         "listed", [0,1,2,3]],
    374 : ["MOD|PHASER|RATE",         "minmax", [0,100]],
    375 : ["MOD|PHASER|DEPTH",        "minmax", [0,100]],
    376 : ["MOD|PHASER|MANUAL",       "minmax", [0,100]],
    377 : ["MOD|PHASER|RESONANCE",    "minmax", [0,100]],
    378 : ["MOD|PHASER|STEP RATE",    "minmax", [0,101]],
    379 : ["MOD|PHASER|EFFECT LEVEL", "minmax", [0,100]],
    380 : ["MOD|PHASER|DIRECT MIX",   "minmax", [0,100]],
    # MOD|FLANGER:
    382 : ["MOD|FLANGER|RATE",         "minmax", [0,100]],
    383 : ["MOD|FLANGER|DEPTH",        "minmax", [0,100]],
    384 : ["MOD|FLANGER|MANUAL",       "minmax", [0,100]],
    385 : ["MOD|FLANGER|RESONANCE",    "minmax", [0,100]],
    387 : ["MOD|FLANGER|LOW CUT",      "listed", [0,1,2,3,4,5,6,7,8,9,10]],
    388 : ["MOD|FLANGER|EFFECT LEVEL", "minmax", [0,100]],
    389 : ["MOD|FLANGER|DIRECT MIX",   "minmax", [0,100]],
    # MOD|TREMOLO:
    391 : ["MOD|TREMOLO|WAVE SHAPE", "minmax", [0,100]],
    392 : ["MOD|TREMOLO|RATE",       "minmax", [0,100]],
    393 : ["MOD|TREMOLO|DEPTH",      "minmax", [0,100]],
    394 : ["MOD|TREMOLO|LEVEL",      "minmax", [0,100]],
    # MOD|ROTARY:
    398 : ["MOD|ROTARY|RATE",  "minmax", [0,100]],
    401 : ["MOD|ROTARY|DEPTH", "minmax", [0,100]],
    402 : ["MOD|ROTARY|LEVEL", "minmax", [0,100]],
    # MOD|UNI-V:
    404 : ["MOD|UNI-V|RATE",  "minmax", [0,100]],
    405 : ["MOD|UNI-V|DEPTH", "minmax", [0,100]],
    406 : ["MOD|UNI-V|LEVEL", "minmax", [0,100]],
    # MOD|SLICER:
    415 : ["MOD|SLICER|PATTERN",      "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]],
    416 : ["MOD|SLICER|RATE",         "minmax", [0,100]],
    417 : ["MOD|SLICER|TRIGGER SENS", "minmax", [0,100]],
    418 : ["MOD|SLICER|EFFECT LEVEL", "minmax", [0,100]],
    419 : ["MOD|SLICER|DIRECT MIX",   "minmax", [0,100]],
    # MOD|VIBRATO:
    421 : ["MOD|VIBRATO|RATE",  "minmax", [0,100]],
    422 : ["MOD|VIBRATO|DEPTH", "minmax", [0,100]],
    425 : ["MOD|VIBRATO|LEVEL", "minmax", [0,100]],
    # MOD|RING MOD:
    427 : ["MOD|RING MOD|MODE",         "listed", [0,1]],
    428 : ["MOD|RING MOD|FREQUENCY",    "minmax", [0,100]],
    429 : ["MOD|RING MOD|EFFECT LEVEL", "minmax", [0,100]],
    430 : ["MOD|RING MOD|DIRECT MIX",   "minmax", [0,100]],
    # MOD|HUMANIZER:
    432 : ["MOD|HUMANIZER|MODE",   "listed", [0,1]],
    433 : ["MOD|HUMANIZER|VOWEL1", "listed", [0,1,2,3,4]],
    434 : ["MOD|HUMANIZER|VOWEL2", "listed", [0,1,2,3,4]],
    435 : ["MOD|HUMANIZER|SENS",   "minmax", [0,100]],
    436 : ["MOD|HUMANIZER|RATE",   "minmax", [0,100]],
    437 : ["MOD|HUMANIZER|DEPTH",  "minmax", [0,100]],
    438 : ["MOD|HUMANIZER|MANUAL", "minmax", [0,100]],
    439 : ["MOD|HUMANIZER|LEVEL",  "minmax", [0,100]],
    # MOD|CHORUS:
    441 : ["MOD|CHORUS|XOVER FREQUENCY", "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]],
    442 : ["MOD|CHORUS|LOW RATE",        "minmax", [0,100]],
    443 : ["MOD|CHORUS|LOW DEPTH",       "minmax", [0,100]],
    444 : ["MOD|CHORUS|LOW PRE DELAY",   "scaled", [0,2,0,80]], # Input: 0.0 -- 40.0 (half steps)
    445 : ["MOD|CHORUS|LOW LEVEL",       "minmax", [0,100]],
    446 : ["MOD|CHORUS|HIGH RATE",       "minmax", [0,100]],
    447 : ["MOD|CHORUS|HIGH DEPTH",      "minmax", [0,100]],
    448 : ["MOD|CHORUS|HIGH PRE DELAY",  "scaled", [0,2,0,80]], # Input: 0.0 -- 40.0 (half steps)
    449 : ["MOD|CHORUS|HIGH LEVEL",      "minmax", [0,100]],
    450 : ["MOD|CHORUS|DIRECT MIX",      "minmax", [0,100]],
    # MOD|AC.GUITAR SIM:
    2064 : ["MOD|AC.GUITAR SIM|HIGH",  "scaled", [50,1,0,100]], # Input: -50 -- +50
    2065 : ["MOD|AC.GUITAR SIM|BODY",  "minmax", [0,100]],
    2066 : ["MOD|AC.GUITAR SIM|LOW",   "scaled", [50,1,0,100]], # Input: -50 -- +50
    2068 : ["MOD|AC.GUITAR SIM|LEVEL", "minmax", [0,100]],
    # MOD|PHASER 90E:
    2109 : ["MOD|PHASER 90E|SCRIPT", "listed", [0,1]], # 0=OFF, 1=ON
    2110 : ["MOD|PHASER 90E|SPEED",  "minmax", [0,100]],
    # MOD|FLANGER 117E:
    2111 : ["MOD|FLANGER 117E|MANUAL", "minmax", [0,100]],
    2112 : ["MOD|FLANGER 117E|WIDTH",  "minmax", [0,100]],
    2113 : ["MOD|FLANGER 117E|SPEED",  "minmax", [0,100]],
    2114 : ["MOD|FLANGER 117E|REGEN",  "minmax", [0,100]],

    2326 : ["DELAY OR FX",    "listed", [0,1]], # 0=DELAY, 1=FX
    # FX:
    2314 : ["FX|GREEN TYPE",  "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2315 : ["FX|RED TYPE",    "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2316 : ["FX|YELLOW TYPE", "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    2323 : ["FX|COLOR",       "listed", [0,1,2]],
    460  : ["FX|ON/OFF",      "listed", [0,1]],
    461  : ["FX|TYPE",        "listed", [0,1,2,3,4,6,7,9,10,12,14,15,16,18,19,20,21,22,23,25,26,27,28,29,31,35,36]],
    # 2326 "DELAY OR FX" is located under DELAY
    # FX|T.WAH:
    472  : ["FX|T.WAH|MODE",         "listed", [0,1]], # 0=LPF, 1=BPF
    473  : ["FX|T.WAH|POLARITY",     "listed", [0,1]], # 0=DOWN, 1=UP
    474  : ["FX|T.WAH|SENS",         "minmax", [0,100]],
    475  : ["FX|T.WAH|FREQUENCY",    "minmax", [0,100]],
    476  : ["FX|T.WAH|PEAK",         "minmax", [0,100]],
    477  : ["FX|T.WAH|DIRECT MIX",   "minmax", [0,100]],
    478  : ["FX|T.WAH|EFFECT LEVEL", "minmax", [0,100]],
    # FX|AUTO WAH:
    480  : ["FX|AUTO WAH|MODE",         "listed", [0,1]], # 0=LPF, 1=BPF
    481  : ["FX|AUTO WAH|FREQUENCY",    "minmax", [0,100]],
    482  : ["FX|AUTO WAH|PEAK",         "minmax", [0,100]],
    483  : ["FX|AUTO WAH|RATE",         "minmax", [0,100]],
    484  : ["FX|AUTO WAH|DEPTH",        "minmax", [0,100]],
    485  : ["FX|AUTO WAH|DIRECT MIX",   "minmax", [0,100]],
    486  : ["FX|AUTO WAH|EFFECT LEVEL", "minmax", [0,100]],
    # FX|PEDAL WAH:
    488 : ["FX|PEDAL WAH|TYPE",           "listed", [0,1,2,3,4,5]],
    489 : ["FX|PEDAL WAH|PEDAL POSITION", "minmax", [0,100]],
    490 : ["FX|PEDAL WAH|PEDAL MIN",      "minmax", [0,100]],
    491 : ["FX|PEDAL WAH|PEDAL MAX",      "minmax", [0,100]],
    492 : ["FX|PEDAL WAH|EFFECT LEVEL",   "minmax", [0,100]],
    493 : ["FX|PEDAL WAH|DIRECT MIX",     "minmax", [0,100]],
    # FX|COMP:
    495 : ["FX|COMP|TYPE",    "listed", [0,1,2,3,4,5,6]],
    496 : ["FX|COMP|SUSTAIN", "minmax", [0,100]],
    497 : ["FX|COMP|ATTACK",  "minmax", [0,100]],
    498 : ["FX|COMP|TONE",    "scaled", [50,1,0,100]], # Input: -50 -- +50
    499 : ["FX|COMP|LEVEL",   "minmax", [0,100]],
    # FX|LIMITER:
    501 : ["FX|LIMITER|TYPE",      "listed", [0,1,2]],
    502 : ["FX|LIMITER|ATTACK",    "minmax", [0,100]],
    503 : ["FX|LIMITER|THRESHOLD", "minmax", [0,100]],
    504 : ["FX|LIMITER|RATIO",     "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    505 : ["FX|LIMITER|RELEASE",   "minmax", [0,100]],
    506 : ["FX|LIMITER|LEVEL",     "minmax", [0,100]],
    # FX|GRAPHIC EQ:
    508 : ["FX|GRAPHIC EQ|31Hz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    509 : ["FX|GRAPHIC EQ|62Hz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    510 : ["FX|GRAPHIC EQ|125Hz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    511 : ["FX|GRAPHIC EQ|250Hz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    512 : ["FX|GRAPHIC EQ|500Hz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    513 : ["FX|GRAPHIC EQ|1kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    514 : ["FX|GRAPHIC EQ|2kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    515 : ["FX|GRAPHIC EQ|4kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    516 : ["FX|GRAPHIC EQ|8kHz",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    517 : ["FX|GRAPHIC EQ|16kHz", "scaled", [20,1,0,40]], # Input: -20 -- +20
    518 : ["FX|GRAPHIC EQ|LEVEL",  "scaled", [20,1,0,40]], # Input: -20 -- +20
    # FX|PARAMETRIC EQ:
    520 : ["FX|PARAMETRIC EQ|LOW CUT",            "minmax", [0,17]],
    521 : ["FX|PARAMETRIC EQ|LOW GAIN",           "scaled", [20,1,0,40]], # Input: -20 -- +20
    522 : ["FX|PARAMETRIC EQ|LOW MID FREQUENCY",  "minmax", [0,27]],
    523 : ["FX|PARAMETRIC EQ|LOW MID Q",          "listed", [0,1,2,3,4,5]],
    524 : ["FX|PARAMETRIC EQ|LOW MID GAIN",       "scaled", [20,1,0,40]], # Input: -20 -- +20
    525 : ["FX|PARAMETRIC EQ|HIGH MID FREQUENCY", "minmax", [0,27]],
    526 : ["FX|PARAMETRIC EQ|HIGH MID Q",         "listed", [0,1,2,3,4,5]],
    527 : ["FX|PARAMETRIC EQ|HIGH MID GAIN",      "scaled", [20,1,0,40]], # Input: -20 -- +20
    528 : ["FX|PARAMETRIC EQ|HIGH GAIN",          "scaled", [20,1,0,40]], # Input: -20 -- +20
    529 : ["FX|PARAMETRIC EQ|HIGH CUT",           "minmax", [0,14]],
    530 : ["FX|PARAMETRIC EQ|LEVEL",              "scaled", [20,1,0,40]], # Input: -20 -- +20
    # FX|GUITAR SIM:
    538 : ["FX|GUITAR SIM|TYPE",  "listed", [0,1,2,3,4,5,6,7]],
    539 : ["FX|GUITAR SIM|LOW",   "scaled", [50,1,0,100]], # Input: -50 -- +50
    540 : ["FX|GUITAR SIM|HIGH",  "scaled", [50,1,0,100]], # Input: -50 -- +50
    541 : ["FX|GUITAR SIM|LEVEL", "minmax", [0,100]],
    542 : ["FX|GUITAR SIM|BODY",  "minmax", [0,100]],
    # FX|SLOW GEAR:
    544 : ["FX|SLOW GEAR|SENS",      "minmax", [0,100]],
    545 : ["FX|SLOW GEAR|RISE TIME", "minmax", [0,100]],
    546 : ["FX|SLOW GEAR|LEVEL",     "minmax", [0,100]],
    # FX|WAVE SYNTH:
    556 : ["FX|WAVE SYNTH|WAVE",         "listed", [0,1]],
    557 : ["FX|WAVE SYNTH|CUTOFF",       "minmax", [0,100]],
    558 : ["FX|WAVE SYNTH|RESONANCE",    "minmax", [0,100]],
    559 : ["FX|WAVE SYNTH|FILTER SENS",  "minmax", [0,100]],
    560 : ["FX|WAVE SYNTH|FILTER DECAY", "minmax", [0,100]],
    561 : ["FX|WAVE SYNTH|FILTER DEPTH", "minmax", [0,100]],
    562 : ["FX|WAVE SYNTH|SYNTH LEVEL",  "minmax", [0,100]],
    563 : ["FX|WAVE SYNTH|DIRECT MIX",   "minmax", [0,100]],
    # FX|OCTAVE:
    573 : ["FX|OCTAVE|RANGE",        "listed", [0,1,2,3]],
    574 : ["FX|OCTAVE|EFFECT LEVEL", "minmax", [0,100]],
    575 : ["FX|OCTAVE|DIRECT MIX",   "minmax", [0,100]],
    # FX|PITCH SHIFTER:
    577 : ["FX|PITCH SHIFTER|VOICE",         "listed", [0,1]],
    578 : ["FX|PITCH SHIFTER|PS1:MODE",      "listed", [0,1,2,3]],
    579 : ["FX|PITCH SHIFTER|PS1:PITCH",     "scaled", [24,1,0,48]],  # Input: -24 -- +24
    580 : ["FX|PITCH SHIFTER|PS1:FINE",      "scaled", [50,1,0,100]], # Input: -50 -- +50
    581 : ["FX|PITCH SHIFTER|PS1:PRE DELAY", "2bytes", [0,300]],
    583 : ["FX|PITCH SHIFTER|PS1:LEVEL",     "minmax", [0,100]],
    584 : ["FX|PITCH SHIFTER|PS2:MODE",      "listed", [0,1,2,3]],
    585 : ["FX|PITCH SHIFTER|PS2:PITCH",     "scaled", [24,1,0,48]],  # Input: -24 -- +24
    586 : ["FX|PITCH SHIFTER|PS2:FINE",      "scaled", [50,1,0,100]], # Input: -50 -- +50
    587 : ["FX|PITCH SHIFTER|PS2:PRE DELAY", "2bytes", [0,300]],
    589 : ["FX|PITCH SHIFTER|PS2:LEVEL",     "minmax", [0,100]],
    590 : ["FX|PITCH SHIFTER|PS1:FEEDBACK",  "minmax", [0,100]],
    591 : ["FX|PITCH SHIFTER|DIRECT MIX",    "minmax", [0,100]],
    # FX|HARMONIST:
    593 : ["FX|HARMONIST|VOICE",              "listed", [0,1]],
    594 : ["FX|HARMONIST|HR1:HARMONY",        "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                                                         17,18,19,20,21,22,23,24,25,26,27,28,29]],
    595 : ["FX|HARMONIST|HR1:PRE DELAY",      "2bytes", [0,300]],
    597 : ["FX|HARMONIST|HR1:LEVEL",          "minmax", [0,100]],
    598 : ["FX|HARMONIST|HR2:HARMONY",        "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                                                         17,18,19,20,21,22,23,24,25,26,27,28,29]],
    599 : ["FX|HARMONIST|HR2:PRE DELAY",      "2bytes", [0,300]],
    601 : ["FX|HARMONIST|HR2:LEVEL",          "minmax", [0,100]],
    602 : ["FX|HARMONIST|HR1:FEEDBACK",       "minmax", [0,100]],
    603 : ["FX|HARMONIST|DIRECT MIX",         "minmax", [0,100]],
    604 : ["FX|HARMONIST|HR1:MAJOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    605 : ["FX|HARMONIST|HR1:MINOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    606 : ["FX|HARMONIST|HR1:MAJOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    607 : ["FX|HARMONIST|HR1:PERFECT UNISON", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    608 : ["FX|HARMONIST|HR1:MINOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    609 : ["FX|HARMONIST|HR1:MAJOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    610 : ["FX|HARMONIST|HR1:MINOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    611 : ["FX|HARMONIST|HR1:MAJOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    612 : ["FX|HARMONIST|HR1:PERFECT FOURTH", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    613 : ["FX|HARMONIST|HR1:TRITONE",        "scaled", [24,1,0,48]],  # Input: -24 -- +24
    614 : ["FX|HARMONIST|HR1:PERFECT FIFTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    615 : ["FX|HARMONIST|HR1:MINOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    616 : ["FX|HARMONIST|HR2:MAJOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    617 : ["FX|HARMONIST|HR2:MINOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    618 : ["FX|HARMONIST|HR2:MAJOR SEVENTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    619 : ["FX|HARMONIST|HR2:PERFECT UNISON", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    620 : ["FX|HARMONIST|HR2:MINOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    621 : ["FX|HARMONIST|HR2:MAJOR SECOND",   "scaled", [24,1,0,48]],  # Input: -24 -- +24
    622 : ["FX|HARMONIST|HR2:MINOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    623 : ["FX|HARMONIST|HR2:MAJOR THIRD",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    624 : ["FX|HARMONIST|HR2:PERFECT FOURTH", "scaled", [24,1,0,48]],  # Input: -24 -- +24
    625 : ["FX|HARMONIST|HR2:TRITONE",        "scaled", [24,1,0,48]],  # Input: -24 -- +24
    626 : ["FX|HARMONIST|HR2:PERFECT FIFTH",  "scaled", [24,1,0,48]],  # Input: -24 -- +24
    627 : ["FX|HARMONIST|HR2:MINOR SIXTH",    "scaled", [24,1,0,48]],  # Input: -24 -- +24
    # 920 MASTER KEY is located under MOD|HARMONIST
    # FX|AC.PROCESSOR:
    633 : ["FX|AC.PROCESSOR|TYPE",             "listed", [0,1,2,3]],
    634 : ["FX|AC.PROCESSOR|BASS",             "scaled", [50,1,0,100]], # Input: -50 -- +50
    635 : ["FX|AC.PROCESSOR|MIDDLE",           "scaled", [50,1,0,100]], # Input: -50 -- +50
    636 : ["FX|AC.PROCESSOR|MIDDLE FREQUENCY", "minmax", [0,27]],
    637 : ["FX|AC.PROCESSOR|TREBLE",           "scaled", [50,1,0,100]], # Input: -50 -- +50
    638 : ["FX|AC.PROCESSOR|PRESENCE",         "scaled", [50,1,0,100]], # Input: -50 -- +50
    639 : ["FX|AC.PROCESSOR|LEVEL",            "minmax", [0,100]],
    # FX|PHASER:
    641 : ["FX|PHASER|TYPE",         "listed", [0,1,2,3]],
    642 : ["FX|PHASER|RATE",         "minmax", [0,100]],
    643 : ["FX|PHASER|DEPTH",        "minmax", [0,100]],
    644 : ["FX|PHASER|MANUAL",       "minmax", [0,100]],
    645 : ["FX|PHASER|RESONANCE",    "minmax", [0,100]],
    646 : ["FX|PHASER|STEP RATE",    "minmax", [0,101]],
    647 : ["FX|PHASER|EFFECT LEVEL", "minmax", [0,100]],
    648 : ["FX|PHASER|DIRECT MIX",   "minmax", [0,100]],
    # FX|FLANGER:
    650 : ["FX|FLANGER|RATE",         "minmax", [0,100]],
    651 : ["FX|FLANGER|DEPTH",        "minmax", [0,100]],
    652 : ["FX|FLANGER|MANUAL",       "minmax", [0,100]],
    653 : ["FX|FLANGER|RESONANCE",    "minmax", [0,100]],
    655 : ["FX|FLANGER|LOW CUT",      "listed", [0,1,2,3,4,5,6,7,8,9,10]],
    656 : ["FX|FLANGER|EFFECT LEVEL", "minmax", [0,100]],
    657 : ["FX|FLANGER|DIRECT MIX",   "minmax", [0,100]],
    # FX|TREMOLO:
    659 : ["FX|TREMOLO|WAVE SHAPE", "minmax", [0,100]],
    660 : ["FX|TREMOLO|RATE",       "minmax", [0,100]],
    661 : ["FX|TREMOLO|DEPTH",      "minmax", [0,100]],
    662 : ["FX|TREMOLO|LEVEL",      "minmax", [0,100]],
    # FX|ROTARY:
    666 : ["FX|ROTARY|RATE",  "minmax", [0,100]],
    669 : ["FX|ROTARY|DEPTH", "minmax", [0,100]],
    670 : ["FX|ROTARY|LEVEL", "minmax", [0,100]],
    # FX|UNI-V:
    672 : ["FX|UNI-V|RATE",  "minmax", [0,100]],
    673 : ["FX|UNI-V|DEPTH", "minmax", [0,100]],
    674 : ["FX|UNI-V|LEVEL", "minmax", [0,100]],
    # FX|SLICER:
    683 : ["FX|SLICER|PATTERN",      "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]],
    684 : ["FX|SLICER|RATE",         "minmax", [0,100]],
    685 : ["FX|SLICER|TRIGGER SENS", "minmax", [0,100]],
    686 : ["FX|SLICER|EFFECT LEVEL", "minmax", [0,100]],
    687 : ["FX|SLICER|DIRECT MIX",   "minmax", [0,100]],
    # FX|VIBRATO:
    689 : ["FX|VIBRATO|RATE",  "minmax", [0,100]],
    690 : ["FX|VIBRATO|DEPTH", "minmax", [0,100]],
    693 : ["FX|VIBRATO|LEVEL", "minmax", [0,100]],
    # FX|RING MOD:
    695 : ["FX|RING MOD|MODE",         "listed", [0,1]],
    696 : ["FX|RING MOD|FREQUENCY",    "minmax", [0,100]],
    697 : ["FX|RING MOD|EFFECT LEVEL", "minmax", [0,100]],
    698 : ["FX|RING MOD|DIRECT MIX",   "minmax", [0,100]],
    # FX|HUMANIZER:
    700 : ["FX|HUMANIZER|MODE",   "listed", [0,1]],
    701 : ["FX|HUMANIZER|VOWEL1", "listed", [0,1,2,3,4]],
    702 : ["FX|HUMANIZER|VOWEL2", "listed", [0,1,2,3,4]],
    703 : ["FX|HUMANIZER|SENS",   "minmax", [0,100]],
    704 : ["FX|HUMANIZER|RATE",   "minmax", [0,100]],
    705 : ["FX|HUMANIZER|DEPTH",  "minmax", [0,100]],
    706 : ["FX|HUMANIZER|MANUAL", "minmax", [0,100]],
    707 : ["FX|HUMANIZER|LEVEL",  "minmax", [0,100]],
    # FX|CHORUS:
    709 : ["FX|CHORUS|XOVER FREQUENCY", "listed", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]],
    710 : ["FX|CHORUS|LOW RATE",        "minmax", [0,100]],
    711 : ["FX|CHORUS|LOW DEPTH",       "minmax", [0,100]],
    712 : ["FX|CHORUS|LOW PRE DELAY",   "scaled", [0,2,0,80]], # Input: 0.0 -- 40.0 (half steps)
    713 : ["FX|CHORUS|LOW LEVEL",       "minmax", [0,100]],
    714 : ["FX|CHORUS|HIGH RATE",       "minmax", [0,100]],
    715 : ["FX|CHORUS|HIGH DEPTH",      "minmax", [0,100]],
    716 : ["FX|CHORUS|HIGH PRE DELAY",  "scaled", [0,2,0,80]], # Input: 0.0 -- 40.0 (half steps)
    717 : ["FX|CHORUS|HIGH LEVEL",      "minmax", [0,100]],
    718 : ["FX|CHORUS|DIRECT MIX",      "minmax", [0,100]],
    # FX|AC.GUITAR SIM:
    2079 : ["FX|AC.GUITAR SIM|HIGH",  "scaled", [50,1,0,100]], # Input: -50 -- +50
    2080 : ["FX|AC.GUITAR SIM|BODY",  "minmax", [0,100]],
    2081 : ["FX|AC.GUITAR SIM|LOW",   "scaled", [50,1,0,100]], # Input: -50 -- +50
    2083 : ["FX|AC.GUITAR SIM|LEVEL", "minmax", [0,100]],
    # FX|PHASER 90E:
    2115 : ["FX|PHASER 90E|SCRIPT", "listed", [0,1]], # 0=OFF, 1=ON
    2116 : ["FX|PHASER 90E|SPEED",  "minmax", [0,100]],
    # FX|FLANGER 117E:
    2117 : ["FX|FLANGER 117E|MANUAL", "minmax", [0,100]],
    2118 : ["FX|FLANGER 117E|WIDTH",  "minmax", [0,100]],
    2119 : ["FX|FLANGER 117E|SPEED",  "minmax", [0,100]],
    2120 : ["FX|FLANGER 117E|REGEN",  "minmax", [0,100]],
}

# Make a mapping of parameter names to indexes, grouped by subsystem
# translate space (' '), dash ('-'), dot ('.') and '/' to underscore ('_')
as_identifier = str.maketrans({' ':'_','-':'_','.':'_','/':'_',':':'_'})
PARAMETERS = dict()
for index,(subsystems,_,_) in KNOWN_INDEXES.items():
    subsystems = subsystems.split('|')
    current = PARAMETERS
    for subsystem in subsystems[:-1]:
        name = subsystem.translate(as_identifier)
        if name not in current:
            current[name] = dict()
        current = current[name]
    # convert the actual parameter names to lower case:
    param = subsystems[-1].lower().translate(as_identifier)
    if param[0].isdigit(): # First character cannot be a digit
        param = '_'+param
    current[param] = index
# MASTER KEY needs to have same index with HARMONIST for both MOD and FX:
PARAMETERS["MOD"]["HARMONIST"]["master_key"] = 920
PARAMETERS["FX"]["HARMONIST"]["master_key"]  = 920
