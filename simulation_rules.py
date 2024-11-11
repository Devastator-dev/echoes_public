import echoes_main as ech

GSR=ech.GlobalSimulationRules(weeks_to_simulate=50,
                              n=5,
                              do_overworld_farming=True,
                              do_tacet_field_farming=True,
                              do_boss_farming=True,
                              amount_of_overworld_farming=0.5,
                              amount_of_tacet_field_farming=4,
                              amount_of_boss_farming=15,
                              save_plots=True,
                              print_character=False,
                              goal_damage_percent=0.75,
                              stop_after_goal_damage=True)