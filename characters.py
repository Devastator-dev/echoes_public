import echoes_main as ech

Rover_Havoc=ech.Character(ech.set_sse,10825,413,1259,125,5,150,ech.weapon_emerald_of_genesis,'Havoc Rover',ech.main_ha_dmg,0,12,12)
'''
Havoc rover with basic stats and standard 5* weapon. You can change weapon or prefered elemental bonus here
'''

Rover_Havoc_max=ech.Character(ech.set_sse,10825,413,1259,125,5,150,ech.weapon_emerald_of_genesis,'Havoc Rover',ech.main_ha_dmg,0,12,12)
'''
Havoc rover with max stats and standard 5* weapon.  Impossible to achieve in game, used for theoretical calculations
'''
Rover_Havoc_max._apply_weapon_conditional_bonuses()
Rover_Havoc_max._total_attack+=(94/100)*Rover_Havoc_max._base_atk
Rover_Havoc_max._total_cd+=149
Rover_Havoc_max._total_cr+=52.5
Rover_Havoc_max._total_attack+=700
Rover_Havoc_max._ult_dmg+=58
Rover_Havoc_max._total_elem_dmg=112




Xiangli_Yao=ech.Character(ech.set_vt,10625,425,1222,125,5,166,ech.weapon_abyss_surges,'Xiangli Yao',ech.main_el_dmg,0,0,12)
'''
Xiangli Yao with basic stats and standard 5* weapon. You can change weapon or prefered elemental bonus here
'''

Xiangli_Yao_max=ech.Character(ech.set_vt,10625,425,1222,125,5,166,ech.weapon_abyss_surges,'Xiangli Yao',ech.main_el_dmg,0,0,12)
'''
Xiangli Yao with max stats and standard 5* weapon.  Impossible to achieve in game, used for theoretical calculations
'''
Xiangli_Yao_max._apply_weapon_conditional_bonuses()
Xiangli_Yao_max._total_attack+=(94/100)*Xiangli_Yao_max._base_atk
Xiangli_Yao_max._total_cd+=149
Xiangli_Yao_max._total_cr+=52.5
Xiangli_Yao_max._total_attack+=700
Xiangli_Yao_max._ult_dmg+=58
Xiangli_Yao_max._total_elem_dmg=112


Jinshi=ech.Character(ech.set_cl,10825,413,1259,125,13,150,ech.weapon_ages_of_harvest,'Jinshi',ech.main_sp_dmg,0,32,12)
'''
Jinshi with basic stats and banner 5* weapon. You can change weapon or prefered elemental bonus here
'''

Jinshi_max=ech.Character(ech.set_cl,10825,413,1259,125,13,150,ech.weapon_ages_of_harvest,'Jinshi',ech.main_sp_dmg,0,32,12)
'''
Jinshi with max stats and banner 5* weapon.  Impossible to achieve in game, used for theoretical calculations
'''
Jinshi_max._apply_weapon_conditional_bonuses()
Jinshi_max._total_attack+=(94/100)*Jinshi_max._base_atk
Jinshi_max._total_cd+=149
Jinshi_max._total_cr+=52.5
Jinshi_max._total_attack+=700
Jinshi_max._skill_dmg+=58
Jinshi_max._total_elem_dmg=112


Shorekeeper=ech.Character(ech.set_rg,16713,288,1100,125,5,150,ech.weapon_variation,'Shorekeeper',ech.main_er,12,0,0,12)
'''
Shorekeeper with basic stats and 4* weapon. You can change weapon or prefered elemental bonus here
'''


maxes_dict={'Havoc Rover':Rover_Havoc_max,'Xiangli Yao':Xiangli_Yao_max,'Jinshi':Jinshi_max}
