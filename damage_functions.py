import numpy as np
import random
import copy
import echoes_main as ech

def calculate_hrover_combo_damage(character:ech.Character)->float:
    """
    This calculates folowing combo of havoc rover without buffs from other characters.
    -----------

    Intro 1x 1 hits total \n
    Skill 2x 3 hits total \n
    Heavy Attack: Devastation 1x 4 hits total \n
    Umbra: Basic P1 1x 5 hits total \n
    Umbra: Basic P2 1x 6 hits total \n 
    Umbra: Basic P3 1x 7 hits total \n
    Umbra: Basic P4 4x 11 hits total \n
    Umbra: Basic P5 5x 16 hits total \n
    Umbra: Basic P1 1x 17 hits total \n
    Umbra: Basic P2 1x 18 hits total \n
    Umbra: Basic P3 1x 19 hits total \n 
    Umbra: Basic P4 4x 23 hits total \n 
    Umbra: Basic P5 5x 28 hits total \n 
    Skill: Umbra: Lifetaker 6x 34 hits total \n
    Ultimate 1x 35 hits total \n
    Outro 3x 38 hits total \n
    """
    total_attack = character._total_attack
    total_cr = character._total_cr / 100
    total_cd = character._total_cd / 100
    total_elem_dmg = character._total_elem_dmg / 100
    skill_dmg = character._skill_dmg / 100
    heavy_dmg = character._heavy_dmg / 100
    basic_dmg = character._basic_dmg / 100
    ult_dmg = character._ult_dmg / 100
    outro_dmg = character._outro_dmg / 100

    multipliers = np.array([
        1.9881,  
        2.8629, 2.8629,  
        2.2814,
        0.5637, 0.9394, 1.5567, 0.3713, 0.3713,
          0.3713, 1.1139, 0.2852, 0.2852, 0.2852, 0.2852, 1.1407,
        0.5637, 0.9394, 1.5567, 0.3713, 0.3713,
          0.3713, 1.1139, 0.2852, 0.2852, 0.2852, 0.2852, 1.1407,
        2.7635, 2.7635, 0.0995, 0.0995, 0.0995, 0.0995,
        15.2090, 
        1.433, 1.433, 1.433
    ])

    bonus_types = np.array([
        total_elem_dmg,
        total_elem_dmg + skill_dmg,
          total_elem_dmg + skill_dmg,  
        total_elem_dmg + heavy_dmg,
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2,
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2,
        total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
          total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2, 
        total_elem_dmg + basic_dmg + 0.2,
        total_elem_dmg + basic_dmg + 0.2,
        total_elem_dmg + skill_dmg + 0.2,
          total_elem_dmg + skill_dmg + 0.2, 
        total_elem_dmg + skill_dmg + 0.2,
          total_elem_dmg + skill_dmg + 0.2, 
          total_elem_dmg + skill_dmg + 0.2, 
          total_elem_dmg + skill_dmg + 0.2, 
        total_elem_dmg + ult_dmg + 0.2, 
        total_elem_dmg + outro_dmg,
          total_elem_dmg + outro_dmg,
          total_elem_dmg + outro_dmg 
    ])

    crit = np.random.rand(38) < total_cr
    hit_damage = multipliers * total_attack * (1 + bonus_types) * (1 + ((total_cd - 1) * crit))
    return np.sum(hit_damage)









def calculate_xiangli_combo_damage(character: ech.Character) -> float:
    """

    Calculates damage of xiangli yao combo:

    Intro   2x 2 hits total \n
    Ultimate: Cogiation Model   1x 3 hits total \n
    Ultimate: Skill: Divergence     5x 8 hits total  \n
    Forte: Mid-Air Attack: Revamp   6x 14 hits total \n
    Forte: Skill: Law of Reigns    5x 19 hits total \n
    Ultimate: Basic: Pivot - Impale P1  1x 20 hits total \n
    Ultimate: Basic: Pivot - Impale P2  4x 24 hits total \n
    Ultimate: Basic: Pivot - Impale P3  2x 26 hits total \n
    Forte: Skill: Law of Reigns    5x 31 hits total \n
    Ultimate: Skill: Divergence     5x 36 hits total \n
    Forte: Mid-Air Attack: Revamp   6x 42 hits total \n
    Forte: Skill: Law of Reigns (Swap-Cancel)   5x 47 hits total \n
    Outro   3x 50 hits total \n

    """
    total_attack = character._total_attack
    total_cr = character._total_cr / 100
    total_cd = character._total_cd / 100
    total_elem_dmg = character._total_elem_dmg / 100
    ult_dmg = character._ult_dmg / 100
    skill_dmg = character._skill_dmg / 100
    basic_dmg = character._basic_dmg / 100
    outro_dmg = character._outro_dmg / 100

    multipliers = np.array([
        0.9941, 0.9941, 14.6606,
        0.4959, 0.4959, 0.4959, 1.7355, 1.7355,
        0.2187, 0.2187, 0.2187, 0.2187, 0.6561, 0.6561,
        0.9573, 0.9573, 0.9573, 0.9573, 2.5528,
        1.1967,
        0.6092, 0.6092, 0.6092, 0.6092,
        1.3325, 1.3325,
        0.9573, 0.9573, 0.9573, 0.9573, 2.5528,
        0.4959, 0.4959, 0.4959, 1.7355, 1.7355,
        0.2187, 0.2187, 0.2187, 0.2187, 0.6561, 0.6561,
        0.9573, 0.9573, 0.9573, 0.9573, 2.5528,
        2.3763, 2.3763, 2.3763
    ])
    
    bonus_types = np.array([
        total_elem_dmg,
        total_elem_dmg,
        total_elem_dmg + ult_dmg,
        total_elem_dmg + skill_dmg + 0.05,
          total_elem_dmg + skill_dmg + 0.05,
        total_elem_dmg + skill_dmg + 0.05,
          total_elem_dmg + skill_dmg + 0.05,
          total_elem_dmg + skill_dmg + 0.05,
        total_elem_dmg + ult_dmg + 0.05,
          total_elem_dmg + ult_dmg + 0.05, 
        total_elem_dmg + ult_dmg + 0.05,
          total_elem_dmg + ult_dmg + 0.05,
        total_elem_dmg + ult_dmg + 0.05,
          total_elem_dmg + ult_dmg + 0.05,
        total_elem_dmg + ult_dmg + 0.05,
          total_elem_dmg + ult_dmg + 0.1,
        total_elem_dmg + ult_dmg + 0.1,
          total_elem_dmg + ult_dmg + 0.1,
        total_elem_dmg + ult_dmg + 0.1,
          total_elem_dmg + basic_dmg + 0.1,
        total_elem_dmg + basic_dmg + 0.1,
          total_elem_dmg + basic_dmg + 0.1,
        total_elem_dmg + basic_dmg + 0.1,
          total_elem_dmg + basic_dmg + 0.1,
        total_elem_dmg + basic_dmg + 0.1,
          total_elem_dmg + basic_dmg + 0.1,
        total_elem_dmg + ult_dmg + 0.1,
          total_elem_dmg + ult_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.15,
          total_elem_dmg + ult_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.15,
          total_elem_dmg + skill_dmg + 0.15,
        total_elem_dmg + skill_dmg + 0.15,
          total_elem_dmg + skill_dmg + 0.15,
        total_elem_dmg + skill_dmg + 0.15,
          total_elem_dmg + skill_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.15,
          total_elem_dmg + ult_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.15,
        total_elem_dmg + ult_dmg + 0.2,
        total_elem_dmg + ult_dmg + 0.2,
        total_elem_dmg + ult_dmg + 0.2,
        total_elem_dmg + ult_dmg + 0.2,
        total_elem_dmg + ult_dmg + 0.2,
        total_elem_dmg + outro_dmg + 0.15,
        total_elem_dmg + outro_dmg + 0.15,
        total_elem_dmg + outro_dmg + 0.15
    ])

    crit = np.random.rand(50) < total_cr
    
    # Calculate total damage using vectorized operations
    hit_damage = multipliers * total_attack * (1 + bonus_types) * (1 + ((total_cd - 1) * crit))
    return np.sum(hit_damage)






def calculate_jinshi_combo_damage(character: ech.Character) -> float:
    """

    Calculates jinshi combo damage:

    Intro   1x 1 hits total \n
    Ultimate    2x 3 hits total \n
    Skill: Overflowing Radiance     9x 12 hits total \n
    Incarnation: Skill: Crescent Divinity   4x 16 hits total \n
    Incarnation: Basic P1   1x 17 hits total \n
    Incarnation: Basic P2   3x 20 hits total \n
    Incarnation: Basic P3   2x 22 hits total \n
    Incarnation: Basic P4   7x 29 hits total \n
    Skill: Illuminous Ephiphany     6x 35    hits total \n
    Illuminous Epiphany: Stella Glamor      1x 36   hits total \n
    Intro       1x 37    hits total \n
    Skill: Overflowing Radiance     9x 46    hits total \n
    Incarnation: Skill: Crescent Divinity   4x 50 hits total \n
    Incarnation: Basic P1   1x 51 hits total \n
    Incarnation: Basic P2   3x 54 hits total \n
    Incarnation: Basic P3   2x 56 hits total \n
    Incarnation: Basic P4   7x 63 hits total \n
    Skill: Illuminous Ephiphany Star DMG    6x 69 hits total \n
    Skill: Illuminous Ephiphany Sun DMG     1x 70 hits total \n
    
    """

    total_attack = character._total_attack
    total_cr = character._total_cr / 100
    total_cd = character._total_cd / 100
    total_elem_dmg = character._total_elem_dmg / 100
    ult_dmg = character._ult_dmg / 100
    skill_dmg = character._skill_dmg / 100


    intro_bonus = total_elem_dmg + 0.5
    ult_bonus = total_elem_dmg + ult_dmg
    skill_bonus = total_elem_dmg + skill_dmg
    outro_bonus = total_elem_dmg + 0.5


    multipliers = np.array([
        1.5905,  
        4.9981, 11.6622, 
        0.0987, 0.0987, 0.0987, 0.0987, 0.2959, 0.2959,
          0.2959, 0.2959, 0.3945, 
        1.0076, 0.7557, 0.7557, 2.5190, 
        0.8862, 0.7797, 0.2599, 0.2599, 0.9944, 0.6630, 
        0.1867, 0.1867, 0.1867, 0.1867, 0.1867, 0.1867, 0.7467,
        0.1989, 0.1989, 0.1989, 0.1989, 0.1989, 0.1989,  
        (3.4792 + (25 * 0.4454)), 
        1.5905,
        0.0987, 0.0987, 0.0987, 0.0987, 0.2959, 0.2959, 
        0.2959, 0.2959, 0.3945,
        1.0076, 0.7557, 0.7557, 2.5190, 
        0.8862, 0.7797, 0.2599, 0.2599, 0.9944, 0.6630, 
        0.1867, 0.1867, 0.1867, 0.1867, 0.1867, 0.1867, 0.7467, 
        0.1989, 0.1989, 0.1989, 0.1989, 0.1989, 0.1989, 
        (3.4792 + (25 * 0.4454)) 
    ])


    bonus_types = np.array([
        intro_bonus,

        ult_bonus,
        ult_bonus, 

        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus, 
        skill_bonus, 
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus, 
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 
        skill_bonus,
        skill_bonus,
        skill_bonus, 
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,  
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,

        intro_bonus,


        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus,
        skill_bonus, 
        skill_bonus,
        skill_bonus,  
        skill_bonus,
        skill_bonus,
        skill_bonus, 
        skill_bonus,
        skill_bonus,
        skill_bonus, 
        skill_bonus, 
        skill_bonus,
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 
        skill_bonus,
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 
        skill_bonus, 

        skill_bonus
    ])
    
    crit = np.random.rand(70) < total_cr
    hit_damage = multipliers * total_attack * (1 + bonus_types) * (1 + ((total_cd - 1) * crit))
    return np.sum(hit_damage)






def calculate_shorekeeper_build_quality(character:ech.Character)->float:
    '''
    Calculates build quality for Shorekeeper based on her optimal combo:
    
    Intro Skill: Discernment - Initial skill cast 3x  3

    Discernment Healing: 289 + 1.32% HP  

    Basic P1 - First basic attack 1x  4
    Basic P2 - Second basic attack 2x  6
    Basic P3 - Third basic attack 3x  9
    Basic P4 - Fourth basic attack 1x  10
    Forte: Heavy Atk: Illation - Enhanced heavy attack  5x  15
    Skill: Chaos Theory - Second skill cast 1x  16

    Healing: 1313 + 5.97% HP  

    Liberation - Liberation attack 

    Healing: 438 + 2.39% HP  10x
    '''
    
    quality_parameter=0
    total_er=character._total_er
    total_hp=character._total_hp
    total_healing=character._total_healing/100
    total_attack = character._total_attack
    total_cr = character._total_cr / 100
    total_cd = character._total_cd / 100
    total_elem_dmg = character._total_elem_dmg / 100
    ult_dmg = character._ult_dmg / 100
    skill_dmg = character._skill_dmg / 100
    basic_dmg = character._basic_dmg / 100
    outro_dmg = character._outro_dmg / 100
    heavy_dmg = character._heavy_dmg / 100

    if (total_er>=230) and (total_er<=240):
        quality_parameter+=100000
    elif (total_er<230) and (total_er>200):
        quality_parameter+=60000
    elif (total_er<200) and (total_er>170):
        quality_parameter+=30000
    elif total_er<170:
        quality_parameter+=9000
    elif total_er>240:
        quality_parameter+=90000
    
    multipliers = np.array([0.1964, 0.1964, 0.1964, 0.2326, 0.1747, 0.1747, 0.1707, 0.1707, 0.1707, 0.5323,
                            0.1389, 0.1389, 0.1389, 0.1389, 0.1389, 0.2729, 0.2729, 0.2729, 0.2729, 0.2729, 0.3131])
    
    total_heals=289+total_hp*0.0132+1313+total_hp*0.0597+(438+total_hp*0.0239)*10
    quality_parameter+=total_heals*5

    bonus_types=np.array([total_elem_dmg,total_elem_dmg,total_elem_dmg,total_elem_dmg+basic_dmg,total_elem_dmg+basic_dmg,
                          total_elem_dmg+basic_dmg,total_elem_dmg+basic_dmg,total_elem_dmg+basic_dmg,total_elem_dmg+basic_dmg,
                          total_elem_dmg+basic_dmg,total_elem_dmg+heavy_dmg,total_elem_dmg+heavy_dmg,total_elem_dmg+heavy_dmg,
                          total_elem_dmg+heavy_dmg,total_elem_dmg+heavy_dmg,total_elem_dmg,total_elem_dmg,total_elem_dmg
                          ,total_elem_dmg,total_elem_dmg,total_elem_dmg+skill_dmg])
    
    crit = np.concatenate([np.ones(3), np.random.rand(18) < total_cr])

    hit_damage=multipliers*total_attack*(1+bonus_types)*(1+((total_cd-1)*crit))
    quality_parameter+=np.sum(hit_damage)
    return quality_parameter