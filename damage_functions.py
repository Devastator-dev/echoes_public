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


def calculate_xiangli_yao_combo_damage(character:ech.Character)->float: # TODO
    pass