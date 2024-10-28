import echoes_main as ech
import damage_functions as dmgfun

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class DamageIsLowerError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def simulate_rover_echo_farming(weeks:int,n:int,save_plots=False,print_character=False):
    discarded=[]
    list_of_days=np.ones(weeks)*7
    damages_through_days=[]
    average_damages_through_days=np.zeros(weeks)
    damage_at_day=0
    previous_rolled_damage=0
    dmg=0
    all_damages=np.zeros((n,np.size(list_of_days)))
    for k in range(n):
        Rover_Havoc=ech.Character(ech.set_sse,10825,413,1259,125,5,150,ech.weapon_emerald_of_genesis,'Havoc Rover',ech.main_ha_dmg,0,12,12)
        Rover_Havoc._apply_weapon_conditional_bonuses()
        echo_lst=[]
        for i in list_of_days:
            echo_lst=echo_lst+ech.simulate_rolling_echoes_n_days(int(i),False,[ech.set_sse,ech.set_mc],ech.set_sse)
            inv=ech.Inventory(ech.desired_mainstats_list_havoc_dps,ech.set_sse,previous_rolled_damage)
            dmg,previous_rolled_damage=inv.pick_best_echoes(echo_lst,Rover_Havoc,dmgfun.calculate_hrover_combo_damage)
            damage_at_day+=dmg
            try:
                if damage_at_day<damages_through_days[-1]:
                    if np.isclose(damage_at_day,damages_through_days[-1],500):
                        damage_at_day=damages_through_days[-1]
                    else:
                        raise DamageIsLowerError
            except(IndexError):
                pass
            damages_through_days.append(damage_at_day)
            damage_at_day=0
            discarded+=echo_lst
            echo_lst=[]
        average_damages_through_days+=np.array(damages_through_days)
        all_damages[k,:]=np.array(damages_through_days)
        damages_through_days=[]
        print((k/n)*100,'%',' done')
        if print_character:
            Rover_Havoc.print_character_stats()
            for i in Rover_Havoc._inventory:
                i.print_stats()
        previous_rolled_damage=0
    average_damages_through_days=average_damages_through_days/n
    percentages_of_max=[i/max(average_damages_through_days) for i in average_damages_through_days]

    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),average_damages_through_days,'.')
    titstr='Simulation of damage during echo farming for '+str(np.sum(list_of_days))+' days for hrover, '+str(n)+' iterations'
    ax.set(title=titstr ,xlabel='day',ylabel='average damage at specific day')
    ax.grid()
    if save_plots:
        titstr+='.png'
        plt.savefig('Output/Graphs/hrover/'+titstr,format='png')


    titstr2='Percentage of max dmg during '+str(np.sum(list_of_days))+' days for hrover, '+str(n)+' iterations'
    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),percentages_of_max,'-.',marker='.')
    ax.set(title=titstr2,xlabel='day',ylabel='percentage of max')
    ax.grid()
    if save_plots:
        titstr2+='.png'
        plt.savefig('Output/Graphs/hrover/'+titstr2,format='png')
    

    titstr3='All damages during '+str(np.sum(list_of_days))+' days for hrover, '+str(n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(all_damages,0))):
        ax.plot(np.cumsum(list_of_days),all_damages[i],'.')
    ax.set(title=titstr3,xlabel='day',ylabel='damage')
    if save_plots:
        titstr3+='.png'
        plt.savefig('Output/Graphs/hrover/'+titstr3,format='png')
    return average_damages_through_days,percentages_of_max,list_of_days





def simulate_xiangli_echo_farming(weeks:int,n:int,save_plots=False,print_character=False):
    discarded=[]
    list_of_days=np.ones(weeks)*7
    damages_through_days=[]
    average_damages_through_days=np.zeros(weeks)
    damage_at_day=0
    previous_rolled_damage=0
    dmg=0
    all_damages=np.zeros((n,np.size(list_of_days)))
    for k in range(n):
        Xiangli_Yao=ech.Character(ech.set_vt,10625,425,1222,125,5,166,ech.weapon_abyss_surges,'Xiangli Yao',ech.main_el_dmg,0,0,12)
        Xiangli_Yao._apply_weapon_conditional_bonuses()
        echo_lst=[]
        for i in list_of_days:
            echo_lst=echo_lst+ech.simulate_rolling_echoes_n_days(int(i),False,[ech.set_ff,ech.set_vt],ech.set_vt)
            inv=ech.Inventory(ech.desired_mainstats_list_electro_dps,ech.set_vt,previous_rolled_damage)
            dmg,previous_rolled_damage=inv.pick_best_echoes(echo_lst,Xiangli_Yao,dmgfun.calculate_xiangli_yao_combo_damage)
            damage_at_day+=dmg
            try:
                if damage_at_day<damages_through_days[-1]:
                    if np.isclose(damage_at_day,damages_through_days[-1],500):
                        damage_at_day=damages_through_days[-1]
                    else:
                        raise DamageIsLowerError
            except(IndexError):
                pass
            damages_through_days.append(damage_at_day)
            damage_at_day=0
            discarded+=echo_lst
            echo_lst=[]
        average_damages_through_days+=np.array(damages_through_days)
        all_damages[k,:]=np.array(damages_through_days)
        damages_through_days=[]
        print((k/n)*100,'%',' done')
        if print_character:
            Xiangli_Yao.print_character_stats()
            for i in Xiangli_Yao._inventory:
                i.print_stats()
        previous_rolled_damage=0
    average_damages_through_days=average_damages_through_days/n
    percentages_of_max=[i/max(average_damages_through_days) for i in average_damages_through_days]

    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),average_damages_through_days,'.')
    titstr='Simulation of damage during echo farming for '+str(np.sum(list_of_days))+' days for xiangli, '+str(n)+' iterations'
    ax.set(title=titstr ,xlabel='day',ylabel='average damage at specific day')
    ax.grid()
    if save_plots:
        titstr+='.png'
        plt.savefig('Output/Graphs/xiangli/'+titstr,format='png')


    titstr2='Percentage of max dmg during '+str(np.sum(list_of_days))+' days for xiangli, '+str(n)+' iterations'
    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),percentages_of_max,'-.',marker='.')
    ax.set(title=titstr2,xlabel='day',ylabel='percentage of max')
    ax.grid()
    if save_plots:
        titstr2+='.png'
        plt.savefig('Output/Graphs/xiangli/'+titstr2,format='png')
    

    titstr3='All damages during '+str(np.sum(list_of_days))+' days for xiangli, '+str(n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(all_damages,0))):
        ax.plot(np.cumsum(list_of_days),all_damages[i],'.')
    ax.set(title=titstr3,xlabel='day',ylabel='damage')
    if save_plots:
        titstr3+='.png'
        plt.savefig('Output/Graphs/xiangli/'+titstr3,format='png')
    return average_damages_through_days,percentages_of_max,list_of_days




def simulate_jinshi_echo_farming(weeks:int,n:int,save_plots=False,print_character=False):
    discarded=[]
    list_of_days=np.ones(weeks)*7
    damages_through_days=[]
    average_damages_through_days=np.zeros(weeks)
    damage_at_day=0
    previous_rolled_damage=0
    dmg=0
    all_damages=np.zeros((n,np.size(list_of_days)))
    for k in range(n):
        Jinshi=ech.Character(ech.set_cl,10825,413,1259,125,13,150,ech.weapon_ages_of_harvest,'Jinshi',ech.main_sp_dmg,0,32,12)
        Jinshi._apply_weapon_conditional_bonuses()
        echo_lst=[]
        for i in list_of_days:
            echo_lst=echo_lst+ech.simulate_rolling_echoes_n_days(int(i),False,[ech.set_cl,ech.set_lt],ech.set_cl)
            inv=ech.Inventory(ech.desired_mainstats_list_spectro_dps,ech.set_cl,previous_rolled_damage)
            dmg,previous_rolled_damage=inv.pick_best_echoes(echo_lst,Jinshi,dmgfun.calculate_jinshi_combo_damage)
            damage_at_day+=dmg
            try:
                if damage_at_day<damages_through_days[-1]:
                    if np.isclose(damage_at_day,damages_through_days[-1],500):
                        damage_at_day=damages_through_days[-1]
                    else:
                        raise DamageIsLowerError
            except(IndexError):
                pass
            damages_through_days.append(damage_at_day)
            damage_at_day=0
            discarded+=echo_lst
            echo_lst=[]
        average_damages_through_days+=np.array(damages_through_days)
        all_damages[k,:]=np.array(damages_through_days)
        damages_through_days=[]
        print((k/n)*100,'%',' done')
        if print_character:
            Jinshi.print_character_stats()
            for i in Jinshi._inventory:
                i.print_stats()
        previous_rolled_damage=0
    average_damages_through_days=average_damages_through_days/n
    percentages_of_max=[i/max(average_damages_through_days) for i in average_damages_through_days]

    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),average_damages_through_days,'.')
    titstr='Simulation of damage during echo farming for '+str(np.sum(list_of_days))+' days for jinshi, '+str(n)+' iterations'
    ax.set(title=titstr ,xlabel='day',ylabel='average damage at specific day')
    ax.grid()
    if save_plots:
        titstr+='.png'
        plt.savefig('Output/Graphs/jinshi/'+titstr,format='png')


    titstr2='Percentage of max dmg during '+str(np.sum(list_of_days))+' days for jinshi, '+str(n)+' iterations'
    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),percentages_of_max,'-.',marker='.')
    ax.set(title=titstr2,xlabel='day',ylabel='percentage of max')
    ax.grid()
    if save_plots:
        titstr2+='.png'
        plt.savefig('Output/Graphs/jinshi/'+titstr2,format='png')
    

    titstr3='All damages during '+str(np.sum(list_of_days))+' days for jinshi, '+str(n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(all_damages,0))):
        ax.plot(np.cumsum(list_of_days),all_damages[i],'.')
    ax.set(title=titstr3,xlabel='day',ylabel='damage')
    if save_plots:
        titstr3+='.png'
        plt.savefig('Output/Graphs/jinshi/'+titstr3,format='png')
    return average_damages_through_days,percentages_of_max,list_of_days