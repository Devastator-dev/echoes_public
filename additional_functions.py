import echoes_main as ech
import damage_functions as dmgfun
import characters as char

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

class DamageIsLowerError(Exception):
    def __init__(self, *args):
        super().__init__(*args)



def simulate_echo_farming(weeks:int,n:int,character:ech.Character,tacet_field_sets:list,desired_set:str,
                          desired_mainstats_list:list,character_dmgfun,is_support:bool,do_overworld_farming:bool=False,
                          do_tacet_field_farming:bool=True,do_boss_farming:bool=True,
                          amount_of_overworld_farming:float=0.5,amount_of_tacet_field_farming:int=4,
                          amount_of_boss_farming:int=15,save_plots=False,print_character=False,goal_damage_percent:float=0.7):
    """
    Simulates echo rolling and damage or build quality for character passed as parameter

    Parameters
    ----------
    weeks : int
        Number of weeks to simulate.

    n : int
        Number of tries to take average from

    character : Character
        character that you want to simulate
    
    tacet_field_sets : list
        list of 2 sets from tacet field that you want to farm

    desired_set : str
        set that you want to equip on character

    desired_mainstats_list : list
        list of mainstats on 1, 3 and 4 cost echoes that you want on your character

    character_name : str
        name of character used for saving plots

    character_dmgfun : function
        Function that calculates damage for specific character

    is_support : bool
        True if you want to calculate build quality

    do_overworld_farming : bool, default:False
        True if you want to simulate overworld farming

    do_tacet_field_farming : bool,  default:True
        True if you want to simulate tacet field farming

    do_boss_farming : bool, default:True
        True if you want to simulate boss farming

    amount_of_overworld_farming : float, default:0.5
        Amount of mobs to kill in overwolrd (1 means all, 0.5 means half)
    
    amount_of_tacet_field_farming : int, default:4
        Number of Tacet Field runs per day (max 4)

    amount_of_boss_farming : int, default:15
        Number of boss runs per week (max 15)

    save_plots : bool, default:False
        True if you want to save graphs

    print_character : bool, default:False
        True if you want to print character stats and equipment after every try



    """
    discarded=[]
    list_of_days=np.ones(weeks)*7
    damages_through_days=[]
    average_damages_through_days=np.zeros(weeks)
    damage_at_day=0
    previous_rolled_damage=0
    dmg=0
    tuners_lst=[]
    exp_lst=[]
    exps_costs=np.zeros((n,np.size(list_of_days)))
    tuners_costs=np.zeros((n,np.size(list_of_days)))
    all_damages=np.zeros((n,np.size(list_of_days)))
    all_tuners=np.zeros((n,np.size(list_of_days)))
    all_exp=np.zeros((n,np.size(list_of_days)))
    if not is_support:
        perfect_dmg_max=0
        for i in range(100):
            perfect_dmg_max+=character_dmgfun(char.maxes_dict[character._name])
        perfect_dmg_max=perfect_dmg_max/100
        




    for k in range(n):
        character_cpy=character.character_deepcopy()
        character_cpy._apply_weapon_conditional_bonuses()
        echo_lst=[]
        total_exp=0
        total_tuners=0
        exp_since_last_upgrade=0
        tuners_since_last_upgrade=0
        count=0
        for i in list_of_days:
            rolled_echoes_and_exp=ech.simulate_rolling_echoes_n_days(int(i),tacet_field_sets,desired_set,do_overworld_farming,do_tacet_field_farming,
                                                                     do_boss_farming,amount_of_overworld_farming,amount_of_tacet_field_farming,amount_of_boss_farming)
            echo_lst=echo_lst+rolled_echoes_and_exp[0]
            total_exp+=rolled_echoes_and_exp[1]
            exp_since_last_upgrade+=rolled_echoes_and_exp[1]
            total_tuners+=rolled_echoes_and_exp[2]
            tuners_since_last_upgrade+=rolled_echoes_and_exp[2]
            inv=ech.Inventory(desired_mainstats_list,desired_set,previous_rolled_damage)
            dmg,previous_rolled_damage,echo_mats_used,tuners_used=inv.pick_best_echoes(echo_lst,character_cpy,character_dmgfun)
            damage_at_day+=dmg
            total_exp-=echo_mats_used
            exp_since_last_upgrade-=echo_mats_used
            total_tuners-=tuners_used
            tuners_since_last_upgrade-=tuners_used
            if total_exp<0:
                exp_lst.append(-total_exp)
            if total_tuners<0:
                tuners_lst.append(-total_tuners)

            try:
                if damage_at_day<damages_through_days[-1]:
                    if np.isclose(damage_at_day,damages_through_days[-1],500):
                        damage_at_day=damages_through_days[-1]
                    else:
                        raise DamageIsLowerError
            except(IndexError):
                pass
            try:
                if abs(damage_at_day-damages_through_days[-1])>5000:
                    exps_costs[k,count] = -exp_since_last_upgrade
                    tuners_costs[k,count] = -tuners_since_last_upgrade
                    exp_since_last_upgrade=0
                    tuners_since_last_upgrade=0
            except(IndexError):
                pass
            damages_through_days.append(damage_at_day)
            if damage_at_day/perfect_dmg_max>goal_damage_percent:
                pass    #TODO add a stopping point for simulation
            damage_at_day=0
            discarded+=echo_lst
            echo_lst=[]
            count+=1
            if count==np.size(list_of_days):
                exps_costs[k,count-1] = -exp_since_last_upgrade
                tuners_costs[k,count-1] = -tuners_since_last_upgrade
                exp_since_last_upgrade=0
                tuners_since_last_upgrade=0
        average_damages_through_days+=np.array(damages_through_days)
        all_damages[k,:]=np.array(damages_through_days)
        all_tuners[k,:]=np.array(tuners_lst)
        all_exp[k,:]=np.array(exp_lst)
        exp_lst=[]
        tuners_lst=[]
        damages_through_days=[]
        print((k/n)*100,'%',' done')
        if print_character:
            character_cpy.print_character_stats()
            for i in character_cpy._inventory:
                i.print_stats()
        previous_rolled_damage=0
        if total_exp<0:
            print('Echo exp materials needed (golden): ',-total_exp)
            print('Estimated tacet field runs needed for exp: ', -total_exp/4.18)
            print('Estimated days to get that exp: ', (-total_exp/4.18)/4)
        else:
            print('Echo materials obtained (golden): ',total_exp)
        if total_tuners<0:
            print('\nTuners needed: ', -total_tuners)
            print('Estimated tacet field runs needed for tuners: ', -total_tuners/25)
            print('Estimated days to get that tuners: ', (-total_tuners/25)/4)

        else:
            print('Tuners obtained: ',total_tuners)
    average_damages_through_days=average_damages_through_days/n
    percentages_of_max=[i/max(average_damages_through_days) for i in average_damages_through_days]
    percentages_of_perfection=[i/perfect_dmg_max for i in average_damages_through_days]



    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),average_damages_through_days,'.')
    if is_support:
        titstr='Simulation of build quality during echo farming for '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
        ylabel='average build quality at specific day'
    else:
        titstr='Simulation of damage during echo farming for '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
        ylabel='average damage at specific day'
    ax.set(title=titstr ,xlabel='day',ylabel=ylabel)
    if not is_support:
        ax.legend(['average damage'])
    else:
        ax.legend(['average build quality'])
    ax.grid()
    if save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr,format='png')





    if is_support:
        ylabel='percentage of max build quality'
        titstr2='Percentage of max build quality during '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
    else:
        ylabel='percentage of max dmg and perfect dmg'
        titstr2='Percentage of max dmg and perfect dmg during '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
    fig,ax=plt.subplots()
    ax.plot(np.cumsum(list_of_days),percentages_of_max,'-.',marker='.')
    if not is_support:
        ax.plot(np.cumsum(list_of_days),percentages_of_perfection,'-.',marker='.')
        ax.legend(['% of max dmg achieved','% of perfect dmg'])
    else:
        ax.legend(['% of max build quality'])
    ax.set(title=titstr2,xlabel='day',ylabel=ylabel)
    ax.grid()
    if save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr2+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr2,format='png')
    
    



    if is_support:
        ylabel='build quality at specific day'
        titstr3='All build qualities during '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
    else:
        ylabel='damage at specific day'
        titstr3='All damages during '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(all_damages,0))):
        ax.plot(np.cumsum(list_of_days),all_damages[i],'.')
    ax.set(title=titstr3,xlabel='day',ylabel=ylabel)
    if save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr3+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr3,format='png')






    titstr4='Tuner and exp costs during '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(all_tuners,0))):
        ax.plot(np.cumsum(list_of_days),all_tuners[i],color='y')
        ax.plot(np.cumsum(list_of_days),all_exp[i],color='m')
    ax.set(title=titstr4,xlabel='day',ylabel='amount')
    ax.legend(['tuners','exp'])
    if save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr4+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr4,format='png')


    titstr5='Tuner and exp costs per dmg increase for '+str(np.sum(list_of_days))+' days for '+character._name+' '+str(n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(exps_costs,0))):
        ax.plot(np.cumsum(list_of_days),exps_costs[i],'.',color='m')
        ax.plot(np.cumsum(list_of_days),tuners_costs[i],'.',color='y')
    ax.set(title=titstr5,xlabel='day',ylabel='cost')
    ax.grid(True, which='both', linestyle='-', linewidth=0.5)
    ax.semilogy()
    ax.minorticks_on()
    ax.legend(['exp','tuners'])
    if save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr5+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr5,format='png')

    return average_damages_through_days,percentages_of_max,list_of_days