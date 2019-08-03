# -*- coding: utf-8 -*-

from turnstile import Turnstile

ts = Turnstile()

event_1 = [['coin',0.2], ['coin', 0.2], ['pass'], ['coin', 0.6], ['pass']]

event_2 = [['coin',0.2], ['coin', 0.2], ['failed'], ['fixed']]

event_3 = [['coin', 0.5], ['coin', 0.5], ['failed'], ['fixed']]

event_4 = [['coin',0.2], ['coin', 0.2], ['coin', 0.7], ['coin',0.1], ['pass']]

flows = [event_1, event_2, event_3, event_4]

for flow in flows:
    print("*****************************************************")
    print("New flow")  # Continues with current state of the turnstile
    
    for event in flow:
        print("\n****")
        print("Event : ", event)
        event_name = event[0]
        
        if event_name == 'coin':
            ts.coin_event(event[1])
        
        elif event_name == 'pass':
            ts.pass_event()
        
        elif event_name == 'failed':
            ts.failed_event()
        
        elif event_name == 'fixed':
            ts.fixed_event()
        
        else:
            print("Improper event name")
        
        ts.get_state()
    
    v = input("\n >>>>>>>>>>>>>>>>>>> Press enter for next flow >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ")
