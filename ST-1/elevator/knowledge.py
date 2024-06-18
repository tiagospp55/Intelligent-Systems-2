from pyke import knowledge_engine

def control_elevator():
    #cria uma instância do motor de inferência da biblioteca Pyke e associa-o ao arquivo atual
    engine = knowledge_engine.engine(__file__)

    #dados do estado atual
    CurrentFloor = int(input("Enter current floor: "))
    PassengersInside = int(input("Enter number of passengers inside: "))
    PassengersWaiting = int(input("Enter number of passengers waiting: "))
    WhereTo = int(input("Enter destination floor: "))
    WhereWaiting = int(input("Enter floor where passengers are waiting: "))
    Door = int(input("Is the door open? (S-1/N-0)?"))
    print()

    # ativa a base de conhecimento chamada 'elevator_control' no motor de inferência Pyke, utiliza as regras definidas no elevator_control.krb
    engine.activate('elevator_control')
  
    #adiciona factos a base de conhecimento
    engine.assert_('current_floor', 'current_floor', (CurrentFloor,))
    engine.assert_('passengers_inside', 'passengers_inside', (PassengersInside,))
    engine.assert_('passengers_waiting', 'passengers_waiting', (PassengersWaiting,))
    engine.assert_('where_to', 'where_to', (WhereTo,))
    engine.assert_('where_waiting','where_waiting',(WhereWaiting,))
    engine.assert_('door','door',(Door,))

    
    try:
        #tentar provar um objetivo no sistema
        vals,plans = engine.prove_1_goal('elevator_control.actions($CurrentFloor,$PassengersInside,$PassengersWaiting,$WhereTo,$WhereWaiting,$Door,$Action)', CurrentFloor = CurrentFloor, PassengersInside = PassengersInside, PassengersWaiting = PassengersWaiting, WhereTo = WhereTo, WhereWaiting = WhereWaiting,Door= Door)
        print('The elevator should: ' + vals['Action'])
        print()
        print("Plan: ")
        plans(CurrentFloor,WhereTo,WhereWaiting)
        print()
    except knowledge_engine.CanNotProve:
        print('No action possible')
        print()

    #reinicia o motor de inferencia para limpar os factos definidos
    engine.reset()
 


while True:
    control_elevator()
    user_input = input("Do you want to test again? (yes/no): ").lower()
    if user_input != 'yes':
        break


