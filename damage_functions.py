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
    total_damage=0
    crit=[]
    for i in range(38):
        w=np.random.random()
        if w<(character._total_cr/100):
            crit.append(1)
        else:
            crit.append(0)
    
    total_damage+=1.9881*character._total_attack*(1+(character._total_elem_dmg/100))*(1+(((character._total_cd/100)-1)*crit[0]))

    total_damage+=2.8629*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[1]))
    total_damage+=2.8629*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[2]))

    total_damage+=2.2814*character._total_attack*(1+((character._total_elem_dmg+character._heavy_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[3]))

    total_damage+=0.5637*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[4]))
    total_damage+=0.9394*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[5]))
    total_damage+=1.5567*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[6]))
    total_damage+=0.3713*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[7]))
    total_damage+=0.3713*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[8]))
    total_damage+=0.3713*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[9]))
    total_damage+=1.1139*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[10]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[11]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[12]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[13]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[14]))
    total_damage+=1.1407*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[15]))

    total_damage+=0.5637*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[16]))
    total_damage+=0.9394*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[17]))
    total_damage+=1.5567*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[18]))
    total_damage+=0.3713*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[19]))
    total_damage+=0.3713*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[20]))
    total_damage+=0.3713*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[21]))
    total_damage+=1.1139*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[22]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[23]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[24]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[25]))
    total_damage+=0.2852*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[26]))
    total_damage+=1.1407*character._total_attack*(1+((character._total_elem_dmg+20+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[27]))

    total_damage+=2.7635*character._total_attack*(1+((character._total_elem_dmg+20+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[28]))
    total_damage+=2.7635*character._total_attack*(1+((character._total_elem_dmg+20+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[29]))
    total_damage+=0.0995*character._total_attack*(1+((character._total_elem_dmg+20+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[30]))
    total_damage+=0.0995*character._total_attack*(1+((character._total_elem_dmg+20+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[31]))
    total_damage+=0.0995*character._total_attack*(1+((character._total_elem_dmg+20+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[32]))
    total_damage+=0.0995*character._total_attack*(1+((character._total_elem_dmg+20+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[33]))

    total_damage+=15.2090*character._total_attack*(1+((character._total_elem_dmg+20+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[34]))

    total_damage+=1.433*character._total_attack*(1+((character._total_elem_dmg+character._outro_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[35]))
    total_damage+=1.433*character._total_attack*(1+((character._total_elem_dmg+character._outro_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[36]))
    total_damage+=1.433*character._total_attack*(1+((character._total_elem_dmg+character._outro_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[37]))

    return total_damage


def calculate_xiangli_yao_combo_damage(character:ech.Character)->float:
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
    total_damage=0
    crit=[]
    for i in range(50):
        w=np.random.random()
        if w<(character._total_cr/100):
            crit.append(1)
        else:
            crit.append(0)

    total_damage+=0.9941*character._total_attack*(1+(character._total_elem_dmg/100))*(1+(((character._total_cd/100)-1)*crit[0]))
    total_damage+=0.9941*character._total_attack*(1+(character._total_elem_dmg/100))*(1+(((character._total_cd/100)-1)*crit[1]))

    total_damage+=14.6606*character._total_attack*(1+((character._total_elem_dmg+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[2]))

    total_damage+=0.4959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[3]))
    total_damage+=0.4959*character._total_attack*(1+((character._total_elem_dmg+5+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[4]))
    total_damage+=0.4959*character._total_attack*(1+((character._total_elem_dmg+5+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[5]))
    total_damage+=1.7355*character._total_attack*(1+((character._total_elem_dmg+5+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[6]))
    total_damage+=1.7355*character._total_attack*(1+((character._total_elem_dmg+5+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[7]))

    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+5+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[8]))
    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+5+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[9]))
    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+5+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[10]))
    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+5+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[11]))
    total_damage+=0.6561*character._total_attack*(1+((character._total_elem_dmg+5+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[12]))
    total_damage+=0.6561*character._total_attack*(1+((character._total_elem_dmg+5+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[13]))

    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+5+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[14]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+10+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[15]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+10+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[16]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+10+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[17]))
    total_damage+=2.5528*character._total_attack*(1+((character._total_elem_dmg+10+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[18]))

    total_damage+=1.1967*character._total_attack*(1+((character._total_elem_dmg+10+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[19]))

    total_damage+=0.6092*character._total_attack*(1+((character._total_elem_dmg+10+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[20]))
    total_damage+=0.6092*character._total_attack*(1+((character._total_elem_dmg+10+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[21]))
    total_damage+=0.6092*character._total_attack*(1+((character._total_elem_dmg+10+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[22]))
    total_damage+=0.6092*character._total_attack*(1+((character._total_elem_dmg+10+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[23]))

    total_damage+=1.3325*character._total_attack*(1+((character._total_elem_dmg+10+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[24]))
    total_damage+=1.3325*character._total_attack*(1+((character._total_elem_dmg+10+character._basic_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[25]))

    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+10+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[26]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[27]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[28]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[29]))
    total_damage+=2.5528*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[30]))

    total_damage+=0.4959*character._total_attack*(1+((character._total_elem_dmg+15+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[31]))
    total_damage+=0.4959*character._total_attack*(1+((character._total_elem_dmg+15+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[32]))
    total_damage+=0.4959*character._total_attack*(1+((character._total_elem_dmg+15+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[33]))
    total_damage+=1.7355*character._total_attack*(1+((character._total_elem_dmg+15+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[34]))
    total_damage+=1.7355*character._total_attack*(1+((character._total_elem_dmg+15+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[35]))

    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[36]))
    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[37]))
    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[38]))
    total_damage+=0.2187*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[39]))
    total_damage+=0.6561*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[40]))
    total_damage+=0.6561*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[41]))

    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+15+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[42]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+20+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[43]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+20+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[44]))
    total_damage+=0.9573*character._total_attack*(1+((character._total_elem_dmg+20+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[45]))
    total_damage+=2.5528*character._total_attack*(1+((character._total_elem_dmg+20+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[46]))

    total_damage+=2.3763*character._total_attack*(1+((character._total_elem_dmg+15+character._outro_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[47]))
    total_damage+=2.3763*character._total_attack*(1+((character._total_elem_dmg+15+character._outro_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[48]))
    total_damage+=2.3763*character._total_attack*(1+((character._total_elem_dmg+15+character._outro_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[49]))

    return total_damage



def calculate_jinshi_combo_damage(character:ech.Character)->float:
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

    total_damage=0
    crit=[]
    for i in range(70):
        w=np.random.random()
        if w<(character._total_cr/100):
            crit.append(1)
        else:
            crit.append(0)
    

    total_damage+=1.5905*character._total_attack*(1+((character._total_elem_dmg+50)/100))*(1+(((character._total_cd/100)-1)*crit[0]))
    
    total_damage+=4.9981*character._total_attack*(1+((character._total_elem_dmg+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[1]))
    total_damage+=11.6622*character._total_attack*(1+((character._total_elem_dmg+character._ult_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[2]))

    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[3]))
    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[4]))
    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[5]))
    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[6]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[7]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[8]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[9]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[10]))
    total_damage+=0.3945*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[11]))

    total_damage+=1.0076*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[12]))
    total_damage+=0.7557*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[13]))
    total_damage+=0.7557*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[14]))
    total_damage+=2.5190*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[15]))

    total_damage+=0.8862*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[16]))
    total_damage+=0.7797*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[17]))
    total_damage+=0.2599*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[18]))
    total_damage+=0.2599*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[19]))
    total_damage+=0.9944*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[20]))
    total_damage+=0.6630*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[21]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[22]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[23]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[24]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[25]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[26]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[27]))
    total_damage+=0.7467*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[28]))

    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[29]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[30]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[31]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[32]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[33]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[34]))

    total_damage+=(3.4792+(25*0.4454))*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[35]))

    total_damage+=1.5905*character._total_attack*(1+((character._total_elem_dmg+50)/100))*(1+(((character._total_cd/100)-1)*crit[36]))

    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[37]))
    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[38]))
    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[39]))
    total_damage+=0.0987*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[40]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[41]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[42]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[43]))
    total_damage+=0.2959*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[44]))
    total_damage+=0.3945*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[45]))

    total_damage+=1.0076*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[46]))
    total_damage+=0.7557*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[47]))
    total_damage+=0.7557*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[48]))
    total_damage+=2.5190*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[49]))

    total_damage+=0.8862*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[50]))
    total_damage+=0.7797*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[51]))
    total_damage+=0.2599*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[52]))
    total_damage+=0.2599*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[53]))
    total_damage+=0.9944*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[54]))
    total_damage+=0.6630*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[55]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[56]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[57]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[58]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[59]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[60]))
    total_damage+=0.1867*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[61]))
    total_damage+=0.7467*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[62]))

    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[63]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[64]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[65]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[66]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[67]))
    total_damage+=0.1989*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[68]))

    total_damage+=(3.4792+(25*0.4454))*character._total_attack*(1+((character._total_elem_dmg+character._skill_dmg)/100))*(1+(((character._total_cd/100)-1)*crit[69]))

    return total_damage