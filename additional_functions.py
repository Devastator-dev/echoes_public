import echoes_main as ech
import damage_functions as dmgfun
import characters as char
import simulation_rules as simrules

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

class DamageIsLowerError(Exception):
    def __init__(self, *args):
        super().__init__(*args)










def simulate_echo_farming(character:ech.Character,tacet_field_sets:list,character_dmgfun):
    """
    Simulates echo rolling and damage or build quality for character passed as parameter

    Parameters
    ----------

    character : Character
        character that you want to simulate
    
    tacet_field_sets : list
        list of 2 sets from tacet field that you want to farm


    character_dmgfun : function
        Function that calculates damage for specific character


    """

    discarded=[]
    list_of_days=np.ones(simrules.GSR._weeks_to_simulate)*7
    damages_through_days=[]
    average_damages_through_days=np.zeros(simrules.GSR._weeks_to_simulate)
    damage_at_day=0
    previous_rolled_damage=0
    dmg=0
    tuners_lst=[]
    exp_lst=[]

    exps_costs=np.zeros((simrules.GSR._n,np.size(list_of_days)))
    tuners_costs=np.zeros((simrules.GSR._n,np.size(list_of_days)))
    all_damages=np.zeros((simrules.GSR._n,np.size(list_of_days)))
    all_tuners=np.zeros((simrules.GSR._n,np.size(list_of_days)))
    all_exp=np.zeros((simrules.GSR._n,np.size(list_of_days)))
    if not character._is_support:
        perfect_dmg_max=0
        for i in range(100):
            perfect_dmg_max+=character_dmgfun(char.maxes_dict[character._name])
        perfect_dmg_max=perfect_dmg_max/100
        




    for k in range(simrules.GSR._n):
        character_cpy=character.character_deepcopy()
        character_cpy._apply_weapon_conditional_bonuses()
        echo_lst=[]
        total_exp=0
        total_tuners=0
        exp_since_last_upgrade=0
        tuners_since_last_upgrade=0
        count=0
        for i in list_of_days:
            rolled_echoes_and_exp=ech.simulate_rolling_echoes_n_days(int(i),tacet_field_sets,character._desired_echo_set,simrules.GSR._do_overworld_farming,simrules.GSR._do_tacet_field_farming,
                                                                     simrules.GSR._do_boss_farming,simrules.GSR._amount_of_overworld_farming,
                                                                     simrules.GSR._amount_of_tacet_field_farming,simrules.GSR._amount_of_boss_farming)
            echo_lst=echo_lst+rolled_echoes_and_exp[0]
            total_exp+=rolled_echoes_and_exp[1]
            exp_since_last_upgrade+=rolled_echoes_and_exp[1]
            total_tuners+=rolled_echoes_and_exp[2]
            tuners_since_last_upgrade+=rolled_echoes_and_exp[2]
            inv=ech.Inventory(character._desired_mainstats_list,character._desired_echo_set,previous_rolled_damage)
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
            if simrules.GSR._stop_after_goal_damage and (not character._is_support): 
                if damage_at_day/perfect_dmg_max>simrules.GSR._goal_damage_percent:
                    print('Goal damage reached')    
                    damage_at_day=0
                    discarded+=echo_lst
                    echo_lst=[]
                    count+=1
                    exps_costs[k,count-1] = -exp_since_last_upgrade
                    tuners_costs[k,count-1] = -tuners_since_last_upgrade
                    exp_since_last_upgrade=0
                    tuners_since_last_upgrade=0
                    break
            damage_at_day=0
            discarded+=echo_lst
            echo_lst=[]
            count+=1
            if count==np.size(list_of_days):
                exps_costs[k,count-1] = -exp_since_last_upgrade
                tuners_costs[k,count-1] = -tuners_since_last_upgrade
                exp_since_last_upgrade=0
                tuners_since_last_upgrade=0



        if not simrules.GSR._stop_after_goal_damage:
            average_damages_through_days+=np.array(damages_through_days)
            all_damages[k,:]=np.array(damages_through_days)
            all_tuners[k,:]=np.array(tuners_lst)
            all_exp[k,:]=np.array(exp_lst)

        if simrules.GSR._stop_after_goal_damage and (not character._is_support):
            damages_resized=np.array(damages_through_days)
            damages_resized=np.pad(damages_resized, (0, np.size(average_damages_through_days) - len(damages_resized)), 'constant',constant_values=0)
            tuners_resized=np.array(tuners_lst)
            tuners_resized=np.pad(tuners_resized, (0, np.size(average_damages_through_days) - len(tuners_resized)), 'constant',constant_values=0)
            exps_resized=np.array(exp_lst)
            exps_resized=np.pad(exps_resized, (0, np.size(average_damages_through_days) - len(exps_resized)), 'constant',constant_values=0)
            average_damages_through_days+=damages_resized
            all_tuners[k,:]=tuners_resized
            all_exp[k,:]=exps_resized
            all_damages[k,:]=damages_resized
            



        exp_lst=[]
        tuners_lst=[]
        damages_through_days=[]
        print((k/simrules.GSR._n)*100,'%',' done')
        if simrules.GSR._print_character:
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
                
    average_damages_through_days=average_damages_through_days/simrules.GSR._n
    cummming=np.cumsum(list_of_days)
    
    if simrules.GSR._stop_after_goal_damage and (not character._is_support):
        average_damages_through_days=average_damages_through_days[average_damages_through_days!=0]
        cummming=cummming[:np.size(average_damages_through_days)]
        list_of_days=list_of_days[:np.size(average_damages_through_days)]
        all_damages = all_damages[:, all_damages[0,:] != 0]
        all_tuners = all_tuners[:, all_tuners[0,:] != 0]
        all_exp = all_exp[:, all_exp[0,:] != 0]
        exps_costs = exps_costs[:, exps_costs[0,:] != 0]
        tuners_costs = tuners_costs[:, tuners_costs[0,:] != 0]
    remaining_days=np.sum(list_of_days)
    percentages_of_max=[i/max(average_damages_through_days) for i in average_damages_through_days]
    if not character._is_support:
        percentages_of_perfection=[i/perfect_dmg_max for i in average_damages_through_days]



    
    fig,ax=plt.subplots()
    ax.plot(cummming,average_damages_through_days,'.')
    if character._is_support:
        titstr='Simulation of build quality during echo farming for '+str(remaining_days)+'days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
        ylabel='average build quality at specific day'
    else:
        titstr='Simulation of damage during echo farming for '+str(remaining_days)+' days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
        ylabel='average damage at specific day'
    ax.set(title=titstr ,xlabel='day',ylabel=ylabel)
    if not character._is_support:
        ax.legend(['average damage'])
    else:
        ax.legend(['average build quality'])
    ax.grid()
    if simrules.GSR._save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr,format='png')
    






    if character._is_support:
        ylabel='percentage of max build quality'
        titstr2='Percentage of max build quality during '+str(remaining_days)+' days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
    else:
        ylabel='percentage of max dmg and perfect dmg'
        titstr2='Percentage of max dmg and perfect dmg during '+str(remaining_days)+' days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
    
    fig,ax=plt.subplots()
    ax.plot(cummming,percentages_of_max,'-.',marker='.')
    if not character._is_support:
        ax.plot(cummming,percentages_of_perfection,'-.',marker='.')
        ax.legend(['% of max dmg achieved','% of perfect dmg'])
    else:
        ax.legend(['% of max build quality'])
    ax.set(title=titstr2,xlabel='day',ylabel=ylabel)
    ax.grid()
    if simrules.GSR._save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr2+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr2,format='png')
    
    



    if character._is_support:
        ylabel='build quality at specific day'
        titstr3='All build qualities during '+str(remaining_days)+' days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
    else:
        ylabel='damage at specific day'
        titstr3='All damages during '+str(remaining_days)+' days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(all_damages,0))):
        ax.plot(cummming,all_damages[i],'.')
    ax.set(title=titstr3,xlabel='day',ylabel=ylabel)
    if simrules.GSR._save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr3+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr3,format='png')






    titstr4='Tuner and exp costs during '+str(remaining_days)+' days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(all_tuners,0))):
        ax.plot(cummming,all_tuners[i],color='y')
        ax.plot(cummming,all_exp[i],color='m')
    ax.set(title=titstr4,xlabel='day',ylabel='amount')
    ax.legend(['tuners','exp'])
    if simrules.GSR._save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr4+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr4,format='png')


    exps_costs = np.pad(exps_costs, (0, np.size(average_damages_through_days) - len(exps_costs[0])), 'constant',constant_values=0)
    tuners_costs = np.pad(tuners_costs, (0, np.size(average_damages_through_days) - len(tuners_costs[0])), 'constant',constant_values=0)
    titstr5='Tuner and exp costs per dmg increase for '+str(remaining_days)+' days for '+character._name+' '+str(simrules.GSR._n)+' iterations'
    fig,ax=plt.subplots()
    for i in range(int(np.size(exps_costs,0))):
        ax.plot(cummming,exps_costs[i],'.',color='m')
        ax.plot(cummming,tuners_costs[i],'.',color='y')
    ax.set(title=titstr5,xlabel='day',ylabel='cost')
    ax.grid(True, which='both', linestyle='-', linewidth=0.5)
    ax.semilogy()
    ax.minorticks_on()
    ax.legend(['exp','tuners'])
    if simrules.GSR._save_plots:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Output/Graphs/'+character._name+'/')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        titstr5+='.png'
        plt.savefig('Output/Graphs/'+character._name+'/'+titstr5,format='png')

    return average_damages_through_days,percentages_of_max,list_of_days