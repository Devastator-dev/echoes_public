import numpy as np
import random
import copy

class TooManyEchoesError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class StatsLowerThanZeroError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


echo_1_cost='1'
echo_3_cost='3'
echo_4_cost='4'

echo_costs={echo_1_cost:1,echo_3_cost:3,echo_4_cost:4}

# Code for every echo. You cant equip same echo twice
W27 = "W27"
H05_a = "H05_a"
H05="H05"
H02 = "H02"
G05 = "G05"
H12 = "H12"
H11 = "H11"
H22 = "H22"
W25 = "W25"
S09 = "S09"
H09 = "H09"
N12 = "N12"
W30 = "W30"
W26 = "W26"
N11 = "N11"
H01 = "H01"
N13 = "N13"
W31 = "W31"
H15 = "H15"
H19 = "H19"
H21 = "H21"
H08 = "H08"
G02 = "G02"
N14 = "N14"
G04 = "G04"
X54 = "X54"
S08 = "S08"
G01 = "G01"
S05 = "S05"
G03 = "G03"
X53 = "X53"
R55 = "R55"
W62 = "W62"
H41 = "H41"
W61 = "W61"
H53 = "H53"
H49 = "H49"
H51 = "H51"
H54 = "H54"
Z11 = "Z11"
W63 = "W63"
S06 = "S06"
H48 = "H48"
S55 = "S55"
W60 = "W60"
H42 = "H42"
H46 = "H46"
H80 = "H80"
H71 = "H71"
H72 = "H72"
W77 = "W77"
N74 = "N74"
R56 = "R56"
H73 = "H73"
W75 = "W75"
W76 = "W76"
H91 = "H91"
H81 = "H81"
Z01 = "Z01"

set_ff='GlacioDMG_s'
set_mr='FusionDMG_s'
set_vt='ElectroDMG_s'
set_sg='AeroDMG_s'
set_cl='SpectroDMG_s'
set_sse='HavocDMG_s'
set_rg='Healing_s'
set_mc='Energy_s'
set_lt='Attack_s'

main_hp_p='HP%'
main_atk_p='ATK%'
main_def_p='DEF%'

main_gl_dmg='GlacioDMG'
main_fu_dmg='FusionDMG'
main_el_dmg='ElectroDMG'
main_ae_dmg='AeroDMG'
main_sp_dmg='SpectroDMG'
main_ha_dmg='HavocDMG'
main_er='ER'

main_cr='CR'
main_cd='CD'
main_hb='HB'


cost_1_mainstats_val={}
cost_3_mainstats_val={}
cost_4_mainstats_val={}

cost_1_mainstats_val[main_hp_p]=[22.8,2280] #2280 hp for every 1 cost
cost_1_mainstats_val[main_atk_p]=[18,2280]
cost_1_mainstats_val[main_def_p]=[18,2280]

cost_3_mainstats_val[main_gl_dmg]=[30,100] #100 atk for every 3 cost
cost_3_mainstats_val[main_fu_dmg]=[30,100]
cost_3_mainstats_val[main_el_dmg]=[30,100]
cost_3_mainstats_val[main_ae_dmg]=[30,100]
cost_3_mainstats_val[main_sp_dmg]=[30,100]
cost_3_mainstats_val[main_ha_dmg]=[30,100]
cost_3_mainstats_val[main_er]=[32,100]
cost_3_mainstats_val[main_hp_p]=[30,100]
cost_3_mainstats_val[main_atk_p]=[30,100]
cost_3_mainstats_val[main_def_p]=[38,100]

cost_4_mainstats_val[main_cr]=[22,150] #150 atk for every 4 cost
cost_4_mainstats_val[main_cd]=[44,150]
cost_4_mainstats_val[main_hb]=[26,150]
cost_4_mainstats_val[main_hp_p]=[33,150]
cost_4_mainstats_val[main_atk_p]=[33,150]
cost_4_mainstats_val[main_def_p]=[41.5,150]


mainstats_cost_1=[main_hp_p,main_atk_p,main_def_p]
mainstats_cost_3=[main_hp_p,main_atk_p,main_def_p,main_ae_dmg,main_el_dmg,main_fu_dmg,main_gl_dmg,main_ha_dmg,main_sp_dmg,main_er]
mainstats_cost_4=[main_atk_p,main_def_p,main_hp_p,main_cr,main_cd,main_hb]


echo_cost_dict = {}

for key in [W27, H05,H05_a, H02, G05, H12, H11, H22, W25, S09, H09, N12, W30, W26, N11, H01, N13, W31, H15, H19, H21, H08, G02, N14, G04, X54, S08, G01, S05, G03, X53]:
    echo_cost_dict[key] = echo_1_cost


for key in [R55, W62, H41, W61, H53, H49, H51, H54, Z11, W63, S06, H48, S55, W60, H42, H46]:
    echo_cost_dict[key] = echo_3_cost


for key in [H80, H71, H72, W77, N74, R56, H73, W75, W76, H91, H81, Z01]:
    echo_cost_dict[key] = echo_4_cost

echo_cost_dict_sets={echo_1_cost:set([W27, H05,H05_a, H02, G05, H12, H11, H22, W25, S09, H09, N12, W30, W26, N11, H01, N13, W31, H15, H19, H21, H08, G02, N14, G04, X54, S08, G01, S05, G03, X53]),
                     echo_3_cost:set([R55, W62, H41, W61, H53, H49, H51, H54, Z11, W63, S06, H48, S55, W60, H42, H46]),
                     echo_4_cost:set([H80, H71, H72, W77, N74, R56, H73, W75, W76, H91, H81, Z01])}





full_sets={}
full_sets[set_ff]=[G05,H05_a,N12,W26,N11,H01,H15,H08,X53,H53,Z11,S06,W60,N74]
full_sets[set_mr]=[H05,W25,H09,N12,W30,H21,G02,N14,X54,H49,H42,H46,W77]
full_sets[set_vt]=[W27,H05,W25,S09,W30,N13,N14,X54,S08,W61,Z11,H42,W75,W76]
full_sets[set_sg]=[W27,H02,H22,W30,H19,H08,X54,G01,S05,R55,H41,H51,H71]
full_sets[set_cl]=[G05,H12,W26,H01,N13,W31,H15,N14,G03,X53,H41,H54,W63,H73,Z01]
full_sets[set_sse]=[H02,H05_a,N11,N13,W31,G04,S05,H49,S06,W60,H80,H81]
full_sets[set_rg]=[H12,H22,S09,H09,G02,S08,G01,W62,H51,W63,S55,H91]
full_sets[set_mc]=[H91,R55,H12,H11,S09,H53,N11,H72,H08,H48,S55,H46,G01,G03]
full_sets[set_lt]=[H05,H11,N12,H19,H21,G02,G04,S08,G03,W62,W61,H48,R56]

full_sets_as_sets={}
full_sets_as_sets[set_ff]=set([G05,H05_a,N12,W26,N11,H01,H15,H08,X53,H53,Z11,S06,W60,N74])
full_sets_as_sets[set_mr]=set([H05,W25,H09,N12,W30,H21,G02,N14,X54,H49,H42,H46,W77])
full_sets_as_sets[set_vt]=set([W27,H05,W25,S09,W30,N13,N14,X54,S08,W61,Z11,H42,W75,W76])
full_sets_as_sets[set_sg]=set([W27,H02,H22,W30,H19,H08,X54,G01,S05,R55,H41,H51,H71])
full_sets_as_sets[set_cl]=set([G05,H12,W26,H01,N13,W31,H15,N14,G03,X53,H41,H54,W63,H73,Z01])
full_sets_as_sets[set_sse]=set([H02,H05_a,N11,N13,W31,G04,S05,H49,S06,W60,H80,H81])
full_sets_as_sets[set_rg]=set([H12,H22,S09,H09,G02,S08,G01,W62,H51,W63,S55,H91])
full_sets_as_sets[set_mc]=set([H91,R55,H12,H11,S09,H53,N11,H72,H08,H48,S55,H46,G01,G03])
full_sets_as_sets[set_lt]=set([H05,H11,N12,H19,H21,G02,G04,S08,G03,W62,W61,H48,R56])




echo_sets={}
for i in full_sets:
    for j in full_sets[i]:
        try:
            if not echo_sets[j]:
                echo_sets[j]=[i]
            else: echo_sets[j].append(i)
        except(KeyError):
            echo_sets[j]=[i]


mainstats_probability_cost_1_weights=[1,1,1]


mainstats_probability_cost_3_weights=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]


mainstats_probability_cost_4_weights=[0.1666,0.1666,0.1666,0.1666,0.1666,0.1666]



# Defining substat names, values and weights

sub_hp='sub_HP'
sub_atk='sub_ATK'
sub_def='sub_DEF'
sub_hp_p='sub_HP%'
sub_atk_p='sub_ATK%'
sub_def_p='sub_DEF%'
sub_cr='sub_CR'
sub_cd='sub_CD'
sub_er='sub_ER'
sub_basic_dmg='sub_ba_DMG'
sub_heavy_dmg='sub_he_DMG'
sub_skill_dmg='sub_sk_DMG'
sub_ult_dmg='sub_ult_DMG'

substats=[sub_hp,sub_atk,sub_def,sub_hp_p,sub_atk_p,sub_def_p,sub_basic_dmg,sub_heavy_dmg,sub_skill_dmg,sub_ult_dmg,sub_er,sub_cr,sub_cd]
substats_weights=np.ones(13)*(1/13)


substat_val_weights=[7.33,14.65,19.54,23.51,15.63,10.42,5.95,2.98]

sub_hp_val=[320,360,390,430,470,510,540,580]
sub_er_val=[6.8,7.6,8.4,9.2,10,10.8,11.6,12.4]
sub_dmg_p_val=[6.4,7.1,7.9,8.6,9.4,10.1,10.9,11.6]
sub_def_p_val=[8.1,9,10,10.9,11.8,12.8,13.8,14.7]
sub_hp_p_val=[6.4,7.1,7.9,8.6,9.4,10.1,10.9,11.6]
sub_atk_p_val=[6.4,7.1,7.9,8.6,9.4,10.1,10.9,11.6]
sub_cd_val=[12.6,13.8,15,16.2,17.4,18.6,19.8,21]
sub_cr_val=[6.3,6.9,7.5,8.1,8.7,9.3,9.9,10.5]

sub_atk_val=[30,40,50,60]
sub_def_val=[40,50,60,70]
sub_flat_val_weights=[18.52,44.45,26.38,10.36]

sub_val_dict={}
sub_val_dict[sub_hp]=sub_hp_val
sub_val_dict[sub_atk]=sub_atk_val
sub_val_dict[sub_def]=sub_def_val
sub_val_dict[sub_basic_dmg]=sub_dmg_p_val
sub_val_dict[sub_ult_dmg]=sub_dmg_p_val
sub_val_dict[sub_skill_dmg]=sub_dmg_p_val
sub_val_dict[sub_heavy_dmg]=sub_dmg_p_val
sub_val_dict[sub_atk_p]=sub_atk_p_val
sub_val_dict[sub_def_p]=sub_def_p_val
sub_val_dict[sub_hp_p]=sub_hp_p_val
sub_val_dict[sub_cr]=sub_cr_val
sub_val_dict[sub_cd]=sub_cd_val
sub_val_dict[sub_er]=sub_er_val


weapon_abyss_surges='abyss_surges'
weapon_blazing_brilliance = 'blazing_brilliance'
weapon_emerald_of_genesis = 'emerald_of_genesis'



weap_elem_dmg='weap_elem_dmg'

weapons_stats_dict={}

weapons_stats_dict[weapon_abyss_surges]=[587,(36.4,sub_atk_p),(12.8,sub_er),(10,sub_basic_dmg),(10,sub_skill_dmg)]
weapons_stats_dict[weapon_blazing_brilliance] = [587, (48.6, sub_cd),(12, sub_atk_p),(56, sub_skill_dmg)]
weapons_stats_dict[weapon_emerald_of_genesis]=[587, (24.3, sub_cr), (12.8, sub_er),(12, sub_atk_p)]



desired_mainstats_list_1cost_dps=(main_atk_p)
desired_mainstats_list_3cost_havoc_dps=(main_ha_dmg,main_atk_p)
desired_mainstats_list_4cost_dps=(main_cd,main_cr,main_atk_p)

desired_mainstats_list_3cost_electro_dps=(main_el_dmg,main_atk_p)


desired_mainstats_list_havoc_dps=[desired_mainstats_list_1cost_dps,desired_mainstats_list_3cost_havoc_dps,desired_mainstats_list_4cost_dps]

desired_mainstats_list_electro_dps=[desired_mainstats_list_1cost_dps,desired_mainstats_list_3cost_electro_dps,desired_mainstats_list_4cost_dps]





echo_amounts_in_overworld={
 'W27': 39,
 'H05_a': 126,
 'H05' : 95,
 'H02': 77,
 'G05': 84,
 'H12': 120,
 'H11': 33,
 'H22': 67,
 'W25': 91,
 'S09': 101,
 'H09': 189,
 'N12': 74,
 'W30': 67,
 'W26': 47,
 'N11': 66,
 'H01': 153,
 'N13': 54,
 'W31': 139,
 'H15': 200,
 'H19': 23,
 'H21': 47,
 'H08': 170,
 'G02': 43,
 'N14': 46,
 'G04': 72,
 'X54': 20,
 'S08': 103,
 'G01': 55,
 'S05': 109,
 'G03': 40,
 'X53': 27,
 'R55': 21,
 'W62': 22,
 'H41': 25,
 'W61': 29,
 'H53': 32,
 'H49': 65,
 'H51': 22,
 'H54': 11,
 'Z11': 7,
 'W63': 22,
 'S06': 47,
 'H48': 55,
 'S55': 74,
 'W60': 19,
 'H42': 31,
 'H46': 27
}

sets_bonuses={
    set_ff:[[10,main_gl_dmg],[30,main_gl_dmg]],
    set_mr:[[10,main_fu_dmg],[30,main_fu_dmg]],
    set_vt:[[10,main_el_dmg],[30,main_el_dmg]],
    set_sg:[[10,main_ae_dmg],[30,main_ae_dmg]],
    set_cl:[[10,main_sp_dmg],[30,main_sp_dmg]],
    set_sse:[[10,main_ha_dmg],[30,main_ha_dmg]],
    set_rg:[[10,main_hb],[set_rg]],
    set_mc:[[10,main_er],[set_mc]],
    set_lt:[[10,main_atk_p],[20,main_atk_p]]
}









class Echo:
    def __init__(self,set:str ,code:str):
        self._set=set
        self._code=code
        self._cost=echo_costs[echo_cost_dict[code]]
        self._substats=self._roll_substats()
        self._mainstats=self._roll_mainstat()
        self._level=0



    def __eq__(self, value):
        return (self.read_substats() == value.read_substats() and self.read_name()==value.read_name())



    def _roll_mainstat(self):
        if self._cost==1:
            mainstat_roll=random.choices(mainstats_cost_1,mainstats_probability_cost_1_weights)[0]
            self._level=25
            return cost_1_mainstats_val[mainstat_roll],mainstat_roll
        
        elif self._cost==3:
            mainstat_roll=random.choices(mainstats_cost_3,mainstats_probability_cost_3_weights)[0]
            self._level=25
            return cost_3_mainstats_val[mainstat_roll],mainstat_roll
        
        else:
            mainstat_roll=random.choices(mainstats_cost_4,mainstats_probability_cost_4_weights)[0]
            self._level=25
            return cost_4_mainstats_val[mainstat_roll],mainstat_roll
    


    def _roll_substats(self):
        result=[]
        sub_choice=np.random.choice(np.array(substats),5,False,substats_weights)
        for i in sub_choice:
            if len(sub_val_dict[i])>4:
                value_choice=random.choices(sub_val_dict[i],substat_val_weights)
                res_tup=(value_choice,i)
                result.append(res_tup)
            else:
                value_choice=random.choices(sub_val_dict[i],sub_flat_val_weights)
                res_tup=(value_choice,i)
                result.append(res_tup)
        self._level=25
        return result



    def print_subs(self)->None:
        print('Substats: ')
        for i in self._substats:
            print(i[0],' ',i[1],'\n')
        pass

    def print_stats(self)->None:
        print('Name: ',self._code,
            '\n Set: ',self._set,
            '\n Cost: ',self._cost,
            '\n Mainstats: ',self._mainstats)
        self.print_subs()
        pass



    def read_mainstats(self):
        return self._mainstats
    


    def read_cost(self):
        return self._cost
    


    def read_substats(self):
        return self._substats
    


    def read_set(self):
        return self._set
    


    def read_name(self):
        return self._code


class Character:
    def __init__(self,echo_set:str,hp:int,atk:int,defe:int,ener:int,cr:int,cd:int,weapon:str,name:str,desired_elem_bonus:str,hb:int=0,elem_dmg:int=0,atk_bonus:int=0,) -> None:
        """
        Create character object with specified stats.

        Parameters
        -------------
        echo_set : str
                Echo set that character equips
        """
        self._echo_set=echo_set
        self._base_hp=hp
        self._base_atk=weapons_stats_dict[weapon][0]+atk
        self._base_defence=defe
        self._energy=ener
        self._cr=cr
        self._cd=cd
        self._healing=hb
        self._elem_dmg=elem_dmg
        self._inventory=[]
        self._equipped_echoes_cost1=[]
        self._equipped_echoes_cost3=[]
        self._equipped_echoes_cost4=[]
        self._weapon=weapon
        self._name=name
        self._desired_elem_bonus=desired_elem_bonus

        self._total_hp=self._base_hp
        self._total_attack=self._base_atk+(self._base_atk*(atk_bonus/100))
        self._total_defence=self._base_defence
        self._total_er=100
        self._total_cr=self._cr
        self._total_cd=self._cd
        self._total_elem_dmg=elem_dmg
        self._skill_dmg=0
        self._basic_dmg=0
        self._ult_dmg=0
        self._heavy_dmg=0
        self._outro_dmg=0
        self._total_healing=self._healing
        self.__apply_weapon_main_bonus()
        self._cond_bonuses_applied=False
        self._echo_bonus_applied=False
        self._echo_set_2pc_applied=False
        self._echo_set_5pc_applied=False
        self._num_of_1cost=0
        self._num_of_3cost=0
        self._num_of_4cost=0
        pass



    def __apply_weapon_main_bonus(self)->None:
        bonus=weapons_stats_dict[self._weapon][1]
        if bonus[1]==sub_atk_p:
            self._total_attack+=(bonus[0]/100)*self._base_atk
        elif bonus[1]==sub_cr:
            self._total_cr+=bonus[0]
        elif bonus[1]==sub_cd:
            self._total_cd+=bonus[0]
        elif bonus[1]==sub_def_p:
            self._total_defence+=bonus[0]
        elif bonus[1]==sub_er:
            self._total_er+=bonus[0]
        pass



    def _apply_weapon_conditional_bonuses(self)->None:
        bonuses=weapons_stats_dict[self._weapon][2:]
        if self._cond_bonuses_applied:
            print('Bonuses already applied')
        else:
            for i in bonuses:
                if i[1]==sub_atk_p:
                    self._total_attack+=(i[0]/100)*self._base_atk
                elif i[1]==sub_hp_p:
                    self._total_hp+=(i[0]/100)*self._base_hp
                elif i[1]==sub_er:
                    self._total_er+=i[0]
                elif i[1]==sub_def:
                    self._total_defence+=(i[0]/100)*self._base_defence
                elif i[1]==sub_basic_dmg:
                    self._basic_dmg+=i[0]
                elif i[1]==sub_skill_dmg:
                    self._skill_dmg+=i[0]
                elif i[1]==sub_ult_dmg:
                    self._ult_dmg+=i[0]
                elif i[1]==sub_heavy_dmg:
                    self._heavy_dmg+=i[0]
                elif i[1]==weap_elem_dmg:
                    self._elem_dmg+=i[0]
            self._cond_bonuses_applied=True
    


    def _disable_weapon_conditional_bonuses(self)->None:
        if not self._cond_bonuses_applied:
            print('Bonuses already disabled')
        else:
            bonuses=weapons_stats_dict[self._weapon][2:]
            for i in bonuses:
                if i[1]==sub_atk_p:
                    self._total_attack-=(i[0]/100)*self._base_atk
                elif i[1]==sub_hp_p:
                    self._total_hp-=(i[0]/100)*self._base_hp
                elif i[1]==sub_er:
                    self._total_er-=i[0]
                elif i[1]==sub_def:
                    self._total_defence-=(i[0]/100)*self._base_defence
                elif i[1]==sub_basic_dmg:
                    self._basic_dmg-=i[0]
                elif i[1]==sub_skill_dmg:
                    self._skill_dmg-=i[0]
                elif i[1]==sub_ult_dmg:
                    self._ult_dmg-=i[0]
                elif i[1]==sub_heavy_dmg:
                    self._heavy_dmg-=i[0]
                elif i[1]==weap_elem_dmg:
                    self._elem_dmg-=i[0]
            self._cond_bonuses_applied=False



    def enable_echo_bonuses(self):
        if self._echo_bonus_applied:
            return 0
        else:
            for i in self._inventory:
                if i.read_cost()==1:
                    if i.read_mainstats()[1]==main_atk_p:
                        self._total_attack+=(i.read_mainstats()[0][0]/100)*self._base_atk
                        self._total_hp+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_hp_p:
                        self._total_hp+=(i.read_mainstats()[0][0]/100)*self._base_hp
                        self._total_hp+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_def_p:
                        self._total_defence+=(i.read_mainstats()[0][0]/100)*self._base_defence
                        self._total_hp+=i.read_mainstats()[0][1]

                elif i.read_cost()==3:
                    if i.read_mainstats()[1]==main_atk_p:
                        self._total_attack+=(i.read_mainstats()[0][0]/100)*self._base_atk
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_hp_p:
                        self._total_hp+=(i.read_mainstats()[0][0]/100)*self._base_hp
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_def_p:
                        self._total_defence+=(i.read_mainstats()[0][0]/100)*self._base_defence
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_gl_dmg:
                        if self._desired_elem_bonus==main_gl_dmg:
                            self._total_elem_dmg+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_fu_dmg:
                        if self._desired_elem_bonus==main_fu_dmg:
                            self._total_elem_dmg+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_el_dmg:
                        if self._desired_elem_bonus==main_el_dmg:
                            self._total_elem_dmg+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_ae_dmg:
                        if self._desired_elem_bonus==main_ae_dmg:
                            self._total_elem_dmg+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_sp_dmg:
                        if self._desired_elem_bonus==main_sp_dmg:
                            self._total_elem_dmg+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_ha_dmg:
                        if self._desired_elem_bonus==main_ha_dmg:
                            self._total_elem_dmg+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_er:
                        self._total_er+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                        
                elif i.read_cost()==4:
                    if i.read_mainstats()[1]==main_atk_p:
                        self._total_attack+=(i.read_mainstats()[0][0]/100)*self._base_atk
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_hp_p:
                        self._total_hp+=(i.read_mainstats()[0][0]/100)*self._base_hp
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_def_p:
                        self._total_defence+=(i.read_mainstats()[0][0]/100)*self._base_defence
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_cd:
                        self._total_cd+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_cr:
                        self._total_cr+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1]==main_hb:
                        self._healing+=i.read_mainstats()[0][0]
                        self._total_attack+=i.read_mainstats()[0][1]
                subs=i.read_substats()
                for j in subs:
                    if j[1]==sub_atk:
                        self._total_attack+=j[0][0]
                    if j[1]==sub_atk_p:
                        self._total_attack+=(j[0][0]/100)*self._base_atk
                    if j[1]==sub_hp:
                        self._total_hp+=j[0][0]
                    if j[1]==sub_hp_p:
                        self._total_hp+=(j[0][0]/100)*self._base_hp
                    if j[1]==sub_def:
                        self._total_defence+=j[0][0]
                    if j[1]==sub_def_p:
                        self._total_defence+=(j[0][0]/100)*self._base_defence
                    if j[1]==sub_basic_dmg:
                        self._basic_dmg+=j[0][0]
                    if j[1]==sub_skill_dmg:
                        self._skill_dmg+=j[0][0]
                    if j[1]==sub_ult_dmg:
                        self._ult_dmg+=j[0][0]
                    if j[1]==sub_heavy_dmg:
                        self._heavy_dmg+=j[0][0]
                    if j[1]==sub_cd:
                        self._total_cd+=j[0][0]
                    if j[1]==sub_cr:
                        self._total_cr+=j[0][0]
                    if j[1]==sub_er:
                        self._total_er+=j[0][0]
            self._echo_bonus_applied=True


    def disable_echo_bonuses(self):
        if not self._echo_bonus_applied:
            return 0
        else:
            for i in self._inventory:
                if i.read_cost() == 1:
                    if i.read_mainstats()[1] == main_atk_p:
                        self._total_attack -= ((i.read_mainstats()[0][0] / 100) * self._base_atk)
                        self._total_hp -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_hp_p:
                        self._total_hp -= ((i.read_mainstats()[0][0] / 100) * self._base_hp)
                        self._total_hp -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_def_p:
                        self._total_defence -= ((i.read_mainstats()[0][0] / 100) * self._base_defence)
                        self._total_hp -= i.read_mainstats()[0][1]

                elif i.read_cost() == 3:
                    if i.read_mainstats()[1] == main_atk_p:
                        self._total_attack -= (i.read_mainstats()[0][0] / 100) * self._base_atk
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_hp_p:
                        self._total_hp -= (i.read_mainstats()[0][0] / 100) * self._base_hp
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_def_p:
                        self._total_defence -= (i.read_mainstats()[0][0] / 100) * self._base_defence
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_gl_dmg:
                        if self._desired_elem_bonus == main_gl_dmg:
                            self._total_elem_dmg -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_fu_dmg:
                        if self._desired_elem_bonus == main_fu_dmg:
                            self._total_elem_dmg -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_el_dmg:
                        if self._desired_elem_bonus == main_el_dmg:
                            self._total_elem_dmg -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_ae_dmg:
                        if self._desired_elem_bonus == main_ae_dmg:
                            self._total_elem_dmg -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_sp_dmg:
                        if self._desired_elem_bonus == main_sp_dmg:
                            self._total_elem_dmg -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_ha_dmg:
                        if self._desired_elem_bonus == main_ha_dmg:
                            self._total_elem_dmg -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_er:
                        self._total_er -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]

                elif i.read_cost() == 4:
                    if i.read_mainstats()[1] == main_atk_p:
                        self._total_attack -= (i.read_mainstats()[0][0] / 100) * self._base_atk
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_hp_p:
                        self._total_hp -= (i.read_mainstats()[0][0] / 100) * self._base_hp
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_def_p:
                        self._total_defence -= (i.read_mainstats()[0][0] / 100) * self._base_defence
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_cd:
                        self._total_cd -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_cr:
                        self._total_cr -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                    elif i.read_mainstats()[1] == main_hb:
                        self._healing -= i.read_mainstats()[0][0]
                        self._total_attack -= i.read_mainstats()[0][1]
                subs = i.read_substats()
                for j in subs:
                    if j[1] == sub_atk:
                        self._total_attack -= j[0][0]
                    if j[1] == sub_atk_p:
                        self._total_attack -= (j[0][0] / 100) * self._base_atk
                    if j[1] == sub_hp:
                        self._total_hp -= j[0][0]
                    if j[1] == sub_hp_p:
                        self._total_hp -= (j[0][0] / 100) * self._base_hp
                    if j[1] == sub_def:
                        self._total_defence -= j[0][0]
                    if j[1] == sub_def_p:
                        self._total_defence -= (j[0][0] / 100) * self._base_defence
                    if j[1] == sub_basic_dmg:
                        self._basic_dmg -= j[0][0]
                    if j[1] == sub_skill_dmg:
                        self._skill_dmg -= j[0][0]
                    if j[1] == sub_ult_dmg:
                        self._ult_dmg -= j[0][0]
                    if j[1] == sub_heavy_dmg:
                        self._heavy_dmg -= j[0][0]
                    if j[1] == sub_cd:
                        self._total_cd -= j[0][0]
                    if j[1] == sub_cr:
                        self._total_cr -= j[0][0]
                    if j[1] == sub_er:
                        self._total_er -= j[0][0]
            self._echo_bonus_applied=False

    

    def character_deepcopy(self):
        return copy.deepcopy(self)



    def print_character_stats(self)->None:
        print('Name: ',self._name,
              '\n Total hp: ', self._total_hp,
              '\n Total atk: ',self._total_attack,
              '\n Total def: ',self._total_defence,
              '\n Crit rate: ', self._total_cr,
              '%\n Crit damage: ',self._total_cd,
              '%\n Energy recharge: ',self._total_er,
              '%\n Elemental damage bonus: ',self._total_elem_dmg,
              '%\n Healing bonus: ', self._total_healing,
              '%\n Basic attack damage bonus: ',self._basic_dmg,
              '%\n Heavy attack damage bonus: ', self._heavy_dmg,
              '%\n Ultimate damage bonus: ', self._ult_dmg,
              '%\n Skill damage bonus: ',self._skill_dmg,
              '%\n Weapon: ',self._weapon,
              '\n Weapon bonuses applied: ',self._cond_bonuses_applied,
              '\n Echo bonus applied: ',self._echo_bonus_applied,
              '\n 2pc set bonus applied: ',self._echo_set_2pc_applied,
              '\n 5pc set bonus applied: ',self._echo_set_5pc_applied)
        
        pass



    def check_set(self):
        num_set_ff=0
        num_set_mr=0
        num_set_vt=0
        num_set_sg=0
        num_set_cl=0
        num_set_sse=0
        num_set_rg=0
        num_set_mc=0
        num_set_lt=0
        for i in self._inventory:
            if i.read_set()==set_ff:
                num_set_ff+=1
            if i.read_set()==set_mr:
                num_set_mr+=1
            if i.read_set()==set_vt:
                num_set_vt+=1
            if i.read_set()==set_sg:
                num_set_sg+=1
            if i.read_set()==set_cl:
                num_set_cl+=1
            if i.read_set()==set_sse:
                num_set_sse+=1
            if i.read_set()==set_rg:
                num_set_rg+=1
            if i.read_set()==set_mc:
                num_set_mc+=1
            if i.read_set()==set_lt:
                num_set_lt+=1
        num_set_dict = {
            set_ff:num_set_ff,
            set_mr:num_set_mr,
            set_vt:num_set_vt,
            set_sg:num_set_sg,
            set_cl:num_set_cl,
            set_sse:num_set_sse,
            set_rg:num_set_rg,
            set_mc:num_set_mc,
            set_lt:num_set_lt
        }
        if (not self._echo_set_2pc_applied) or (not self._echo_set_5pc_applied):
            not_elem_sets=[set_rg,set_mc,set_lt]
            if self._echo_set not in not_elem_sets:
                if num_set_dict[self._echo_set]>=2:
                    if not self._echo_set_2pc_applied:
                        self._total_elem_dmg+=10
                        self._echo_set_2pc_applied=True
                    if not self._echo_set_5pc_applied:
                        if num_set_dict[self._echo_set]==5:
                            self._total_elem_dmg+=30
                            self._echo_set_5pc_applied=True
            else:
                if self._echo_set==set_rg:
                    if num_set_dict[self._echo_set]>=2:
                        if not self._echo_set_2pc_applied:
                            self._total_healing+=10
                            self._echo_set_2pc_applied=True
                        #TODO supporting capabilities of sets
                        if not self._echo_set_5pc_applied:
                            if num_set_dict[self._echo_set]==5:
                                self._echo_set_5pc_applied=True
                if self._echo_set==set_mc: 
                    if num_set_dict[self._echo_set]>=2:
                        if not self._echo_set_2pc_applied:
                            self._total_er+=10
                            self._echo_set_2pc_applied=True
                        #TODO
                        if num_set_dict[self._echo_set]==5:
                            self._echo_set_5pc_applied=True
                if self._echo_set==set_lt:
                    if num_set_dict[self._echo_set]>=2:
                        if not self._echo_set_2pc_applied:
                            self._total_attack+=(10/100)*self._base_atk
                            self._echo_set_2pc_applied=True
                        if num_set_dict[self._echo_set]==5:
                            self._total_attack+=(20/100)*self._base_atk
                            self._outro_dmg+=60
                            self._echo_set_5pc_applied=True
        else:
            not_elem_sets=[set_rg,set_mc,set_lt]
            if self._echo_set not in not_elem_sets:
                if num_set_dict[self._echo_set]<5:
                    self._total_elem_dmg-=30
                    self._echo_set_5pc_applied=False
                    if num_set_dict[self._echo_set]<2:
                        self._total_elem_dmg-=10
                        self._echo_set_2pc_applied=False
            else:
                if self._echo_set==set_rg:
                    if num_set_dict[self._echo_set]<5:
                        self._echo_set_5pc_applied=False
                        if num_set_dict[self._echo_set]<2:
                            self._total_healing-=10
                            self._echo_set_2pc_applied=False
                        #TODO supporting capabilities of sets
                if self._echo_set==set_mc:
                    if num_set_dict[self._echo_set]<5:
                        self._echo_set_5pc_applied=False
                        if num_set_dict[self._echo_set]<2:
                            self._total_er-=10
                            self._echo_set_2pc_applied=False
                        #TODO
                if self._echo_set==set_lt:
                    if num_set_dict[self._echo_set]<5:
                        self._total_attack-=(20/100)*self._base_atk
                        self._outro_dmg-=60
                        self._echo_set_5pc_applied=False
                        if num_set_dict[self._echo_set]<2:
                            self._total_attack-=(10/100)*self._base_atk
                            self._echo_set_2pc_applied=False



class Inventory():
    def __init__(self,desired_mainstats:list,desired_set:str,calculated_damage:int) -> None:
        self._desired_mainstats=desired_mainstats
        self._desired_set=desired_set
        self._equipped_echoes=[]
        self._equipped_echoes_cost1=[]
        self._equipped_echoes_cost3=[]
        self._equipped_echoes_cost4=[]
        self._num_of_1cost=0
        self._num_of_3cost=0
        self._num_of_4cost=0
        self._calculated_damage=calculated_damage
        pass



    def pick_best_echoes(self,echo_list:list,character:Character,damage_function)->float:
        for i in echo_list:
            if i.read_cost()==1:
                if i.read_set()==self._desired_set:
                    if i.read_mainstats()[1] in self._desired_mainstats[0]:
                        if self._num_of_1cost<2 and character._num_of_1cost<2:
                            #self._equipped_echoes_cost1.append(i)
                            character._equipped_echoes_cost1.append(i)
                            self._num_of_1cost+=1
                            character._num_of_1cost+=1
                            character.disable_echo_bonuses()
                            character._inventory.append(i)
                            character.enable_echo_bonuses()
                        elif self._num_of_1cost>=2 or character._num_of_1cost>=2:
                            for j in character._inventory:
                                if i.read_name()==j.read_name():
                                    character_cp=character.character_deepcopy()
                                    character_cp.disable_echo_bonuses()
                                    for k in character_cp._inventory:
                                        if k==j:
                                            character_cp._inventory.remove(k)
                                            break
                                    character_cp._inventory.append(i)
                                    character_cp.enable_echo_bonuses()
                                    damage_old=0
                                    damage_new=0
                                    for k in range(500):
                                        damage_old+=damage_function(character)
                                        damage_new+=damage_function(character_cp)
                                    if damage_old>self._calculated_damage:
                                        self._calculated_damage=damage_old
                                    if damage_new>damage_old:
                                        if damage_new>self._calculated_damage:
                                            print('damage new:',damage_new,'damage old:', damage_old)
                                            character.disable_echo_bonuses()
                                            character._inventory.remove(j)
                                            character._inventory.append(i)
                                            character.enable_echo_bonuses()
                                            #self._equipped_echoes_cost1.remove(j)
                                            character._equipped_echoes_cost1.remove(j)
                                            #self._equipped_echoes_cost1.append(i)
                                            character._equipped_echoes_cost1.append(i)
                                            for l in self._equipped_echoes:
                                                if l==j:
                                                    self._equipped_echoes.remove(l)
                                                    break
                                            self._equipped_echoes.append(i)
                            
                            character_cp_1=character.character_deepcopy()
                            character_cp_2=character.character_deepcopy()

                            character_cp_1.disable_echo_bonuses()
                            for j in character_cp_1._inventory:
                                if j==character._equipped_echoes_cost1[0]:
                                    character_cp_1._inventory.remove(j)
                                    break
                            character_cp_1._inventory.append(i)
                            character_cp_1.enable_echo_bonuses()


                            character_cp_2.disable_echo_bonuses()
                            for j in character_cp_2._inventory:
                                if j==character._equipped_echoes_cost1[1]:
                                    character_cp_2._inventory.remove(j)
                                    break
                            character_cp_2._inventory.append(i)
                            character_cp_2.enable_echo_bonuses()

                            damage_1=0
                            damage_2=0
                            damage_old=0
                            for k in range(500):
                                damage_1+=damage_function(character_cp_1)
                                damage_2+=damage_function(character_cp_2)
                                damage_old+=damage_function(character)
                            if damage_old>self._calculated_damage:
                                self._calculated_damage=damage_old
                            
                            if damage_1>damage_2:
                                if damage_1>damage_old:
                                    if damage_1>self._calculated_damage:
                                        print('damage new 1:',damage_1,'damage old:', damage_old)
                                        rem=copy.deepcopy(character._equipped_echoes_cost1[0])
                                        character.disable_echo_bonuses()
                                        for l in character._inventory:
                                            if l==rem:
                                                character._inventory.remove(l)
                                                break
                                        character._inventory.append(i)
                                        character.enable_echo_bonuses()

                                        for l in character._equipped_echoes_cost1:
                                            if l==rem:
                                                character._equipped_echoes_cost1.remove(l)
                                                break
                                        character._equipped_echoes_cost1.append(i)
                                        for l in self._equipped_echoes:
                                            if l==rem:
                                                self._equipped_echoes.remove(l)
                                                break
                                        self._equipped_echoes.append(i)
                            else:
                                if damage_2>damage_old:
                                    if damage_2>self._calculated_damage:
                                        print('damage new 2:',damage_2,'damage old:', damage_old)
                                        rem=copy.deepcopy(character._equipped_echoes_cost1[1])
                                        character.disable_echo_bonuses()
                                        for l in character._inventory:
                                            if l==rem:
                                                character._inventory.remove(l)
                                                break
                                        character._inventory.append(i)
                                        character.enable_echo_bonuses()
                                        for l in character._equipped_echoes_cost1:
                                            if l==rem:
                                                character._equipped_echoes_cost1.remove(l)
                                                break
                                        character._equipped_echoes_cost1.append(i)
                                        for l in self._equipped_echoes:
                                            if l==rem:
                                                self._equipped_echoes.remove(l)
                                                break
                                        self._equipped_echoes.append(i)

            elif i.read_cost()==3:
                if i.read_set()==self._desired_set:
                    if i.read_mainstats()[1] in self._desired_mainstats[1]:
                        if self._num_of_3cost<2 and character._num_of_3cost<2:
                            character._equipped_echoes_cost3.append(i)
                            self._equipped_echoes.append(i)
                            self._num_of_3cost+=1
                            character._num_of_3cost+=1
                            character.disable_echo_bonuses()
                            character._inventory.append(i)
                            character.enable_echo_bonuses()
                        elif self._num_of_3cost>=2 or character._num_of_3cost>=2:
                            for j in character._inventory:
                                if i.read_name()==j.read_name():
                                    character_cp=character.character_deepcopy()
                                    character_cp.disable_echo_bonuses()
                                    for k in character_cp._inventory:
                                        if k==j:
                                            character_cp._inventory.remove(k)
                                            break
                                    character_cp._inventory.append(i)
                                    character_cp.enable_echo_bonuses()
                                    damage_old=0
                                    damage_new=0
                                    for k in range(500):
                                        damage_old+=damage_function(character)
                                        damage_new+=damage_function(character_cp)
                                    if damage_old>self._calculated_damage:
                                        self._calculated_damage=damage_old
                                    if damage_new>damage_old:
                                        if damage_new>self._calculated_damage:
                                            print('damage new:',damage_new,'damage old:', damage_old)
                                            character.disable_echo_bonuses()
                                            character._inventory.remove(j)
                                            character._inventory.append(i)
                                            character.enable_echo_bonuses()
                                            character._equipped_echoes_cost3.remove(j)
                                            character._equipped_echoes_cost3.append(i)
                                            for l in self._equipped_echoes:
                                                if l==j:
                                                    self._equipped_echoes.remove(l)
                                                    break
                                            self._equipped_echoes.append(i)
                            character_cp_1=character.character_deepcopy()
                            character_cp_2=character.character_deepcopy()

                            character_cp_1.disable_echo_bonuses()
                            for j in character_cp_1._inventory:
                                if j==character._equipped_echoes_cost3[0]:
                                    character_cp_1._inventory.remove(j)
                                    break
                            character_cp_1._inventory.append(i)
                            character_cp_1.enable_echo_bonuses()

                            character_cp_2.disable_echo_bonuses()
                            for j in character_cp_2._inventory:
                                if j==character._equipped_echoes_cost3[1]:
                                    character_cp_2._inventory.remove(j)
                                    break
                            character_cp_2._inventory.append(i)
                            character_cp_2.enable_echo_bonuses()

                            damage_1=0
                            damage_2=0
                            damage_old=0
                            for k in range(500):
                                damage_1+=damage_function(character_cp_1)
                                damage_2+=damage_function(character_cp_2)
                                damage_old+=damage_function(character)
                                if damage_old>self._calculated_damage:
                                    self._calculated_damage=damage_old
                            if damage_1>damage_2:
                                if damage_1>damage_old:
                                    if damage_1>self._calculated_damage:
                                        print('damage new 1:',damage_1,'damage old:', damage_old)
                                        rem=copy.deepcopy(character._equipped_echoes_cost3[0])
                                        character.disable_echo_bonuses()
                                        for l in character._inventory:
                                            if l==rem:
                                                character._inventory.remove(l)
                                                break
                                        character._inventory.append(i)
                                        character.enable_echo_bonuses()
                                        for l in character._equipped_echoes_cost3:
                                            if l==rem:
                                                character._equipped_echoes_cost3.remove(l)
                                                break
                                        character._equipped_echoes_cost3.append(i)
                                        for l in self._equipped_echoes:
                                            if l==rem:
                                                self._equipped_echoes.remove(l)
                                                break
                                        self._equipped_echoes.append(i)
                            else:
                                if damage_2>damage_old:
                                    if damage_2>self._calculated_damage:
                                        print('damage new 2:',damage_2,'damage old:', damage_old)
                                        rem=copy.deepcopy(character._equipped_echoes_cost3[1])
                                        character.disable_echo_bonuses()
                                        for l in character._inventory:
                                            if l==rem:
                                                character._inventory.remove(l)
                                                break
                                        character._inventory.append(i)
                                        character.enable_echo_bonuses()
                                        for l in character._equipped_echoes_cost3:
                                            if l==rem:
                                                character._equipped_echoes_cost3.remove(l)
                                                break
                                        character._equipped_echoes_cost3.append(i)
                                        for l in self._equipped_echoes:
                                            if l==rem:
                                                self._equipped_echoes.remove(l)
                                                break
                                        self._equipped_echoes.append(i)


            elif i.read_cost()==4:
                if i.read_set()==self._desired_set:
                    if i.read_mainstats()[1] in self._desired_mainstats[2]:
                        if self._num_of_4cost==0 and character._num_of_4cost==0:
                            character._equipped_echoes_cost4.append(i)
                            self._equipped_echoes.append(i)
                            self._num_of_4cost+=1
                            character._num_of_4cost+=1
                            character.disable_echo_bonuses()
                            character._inventory.append(i)
                            character.enable_echo_bonuses()
                        elif self._num_of_4cost==1 or character._num_of_4cost==1:
                            for j in character._inventory:
                                if i.read_name()==j.read_name():
                                    character_cp=character.character_deepcopy()
                                    character_cp.disable_echo_bonuses()
                                    for k in character_cp._inventory:
                                        if k==j:
                                            character_cp._inventory.remove(k)
                                            break
                                    character_cp._inventory.append(i)
                                    character_cp.enable_echo_bonuses()
                                    damage_old=0
                                    damage_new=0
                                    for k in range(500):
                                        damage_old+=damage_function(character)
                                        damage_new+=damage_function(character_cp)
                                    if damage_old>self._calculated_damage:
                                        self._calculated_damage=damage_old
                                    if damage_new>damage_old:
                                        if damage_new>self._calculated_damage:
                                            print('damage new:',damage_new,'damage old:', damage_old)
                                            character.disable_echo_bonuses()
                                            character._inventory.remove(j)
                                            character._inventory.append(i)
                                            character.enable_echo_bonuses()
                                            character._equipped_echoes_cost4.remove(j)
                                            character._equipped_echoes_cost4.append(i)
                                            for l in self._equipped_echoes:
                                                if l==j:
                                                    self._equipped_echoes.remove(l)
                                                    break
                                            self._equipped_echoes.append(i)
                            character_cp_1=character.character_deepcopy()
                            character_cp_1.disable_echo_bonuses()
                            for j in character_cp_1._inventory:
                                if j==character._equipped_echoes_cost4[0]:
                                    character_cp_1._inventory.remove(j)
                                    break
                            character_cp_1._inventory.append(i)
                            character_cp_1.enable_echo_bonuses()
                            damage_1=0
                            damage_old=0
                            for k in range(500):
                                damage_1+=damage_function(character_cp_1)
                                damage_old+=damage_function(character)
                            if damage_old>self._calculated_damage:
                                self._calculated_damage=damage_old
                            if damage_1>damage_old:
                                if damage_1>self._calculated_damage:
                                    print('damage new:',damage_1,'damage old:', damage_old)
                                    rem=copy.deepcopy(character._equipped_echoes_cost4[0])
                                    character.disable_echo_bonuses()
                                    for l in character._inventory:
                                            if l==rem:
                                                character._inventory.remove(l)
                                                break
                                    character._inventory.append(i)
                                    character.enable_echo_bonuses()
                                    for l in character._equipped_echoes_cost4:
                                            if l==rem:
                                                character._equipped_echoes_cost4.remove(l)
                                                break
                                    character._equipped_echoes_cost4.append(i)
                                    for l in self._equipped_echoes:
                                            if l==rem:
                                                self._equipped_echoes.remove(l)
                                                break
                                    self._equipped_echoes.append(i)
                
#            num_of_checked+=1
#            if len(character._inventory)>(len(self._equipped_echoes_cost1)+len(self._equipped_echoes_cost3)+len(self._equipped_echoes_cost4)):
#                print('tutaj jest blad')
#                print(num_of_checked)
#                raise(TooManyEchoesError)

            if character._num_of_1cost>2:
                raise(TooManyEchoesError)
            if character._num_of_3cost>2:
                raise(TooManyEchoesError)
            if character._num_of_4cost>1:
                raise(TooManyEchoesError)
        damage_final=0
        if character._basic_dmg<-0.5:
            raise(StatsLowerThanZeroError)
        if character._skill_dmg<-0.5:
            raise(StatsLowerThanZeroError)
        if character._ult_dmg<-0.5:
            raise(StatsLowerThanZeroError)
        if character._heavy_dmg<-0.5:
            raise(StatsLowerThanZeroError)
        character._basic_dmg=max(character._basic_dmg,0)
        character._skill_dmg=max(character._skill_dmg,0)
        character._ult_dmg=max(character._ult_dmg,0)
        character._heavy_dmg=max(character._heavy_dmg,0)
        character.check_set()
        for l in range(100000):
            damage_final+=damage_function(character)
        
        return (damage_final/100000,self._calculated_damage)






def roll_tacet_field(set_:list):
    rand=np.random.random()
    if rand<0.5:
        num_of_echoes=4
    else:
        num_of_echoes=5
    num_of_3cost=[4,3,2,1]
    num_of_3cost_weight=[1/4,1/4,1/4,1/4]
    rolled_3cost=np.random.choice(num_of_3cost,None,False,num_of_3cost_weight)
    rolled_1cost=num_of_echoes-rolled_3cost
    sets=np.random.choice(set_,num_of_echoes,True,[1/2,1/2])
    echo_code_list=[]
    for i in sets:
        while rolled_1cost>0:
            echo_code_list.append(np.random.choice(np.array(list(echo_cost_dict_sets[echo_1_cost].intersection(full_sets_as_sets[i])))
                                                   ,None,False,np.ones(len(echo_cost_dict_sets[echo_1_cost].intersection(full_sets_as_sets[i])))/len(echo_cost_dict_sets[echo_1_cost].intersection(full_sets_as_sets[i]))))
            rolled_1cost-=1
        while rolled_3cost>0:
            echo_code_list.append(np.random.choice(np.array(list(echo_cost_dict_sets[echo_3_cost].intersection(full_sets_as_sets[i])))
                                                   ,None,False,np.ones(len(echo_cost_dict_sets[echo_3_cost].intersection(full_sets_as_sets[i])))/len(echo_cost_dict_sets[echo_3_cost].intersection(full_sets_as_sets[i]))))
            rolled_3cost-=1
    result=[]
    for i in range(num_of_echoes):
        result.append(Echo(sets[i],echo_code_list[i]))
    return result



def simulate_rolling_echoes_n_days(n:int,overworld_farming:bool,sets_to_farm:list,set_of_4cost:str):
    echo_list=[]
    if overworld_farming:  #TODO implement overworld farming
        pass
    for i in range(int(n*4)):
        echo_list.extend(roll_tacet_field(sets_to_farm))
    names_of_4cost=list(echo_cost_dict_sets[echo_4_cost].intersection(full_sets_as_sets[set_of_4cost]))
    for i in range(int((n/7)*15)):
        echo_list.append(Echo(set_of_4cost,np.random.choice(names_of_4cost,None,False,[1/2,1/2])))
    return echo_list

