# -*- coding: utf-8 -*-

from state import State

class LockedState(State):
    '''
    The state in which the turnstile remains locked until the user inserts sufficient coins.
    '''
    correct_amount = 1  # The amount above which a person is allowed to pass the turnstile
    amount = 0
    
    def __init__(self):
        print("Updating state to : ", str(self))
        print("Please insert coins to pass")
    
    def coin_event(self, amount):
        self.accumulate(amount)
        if self.amount >= self.correct_amount:
            return self.unlock()
        
        return self
    
    def failed_event(self):
        self.exit_state()
        print(self.out_of_order_msg())
        return BrokenState()
    
    def pass_event(self):
        print(self.alarm_msg())
        return self
    
    def accumulate(self, amount):
        ''' Accumulates the coin amounts inserted '''
        self.amount += amount
        print("Added amount : ", amount)
        print("Total accumulated amount : ", self.amount)
        print("Required amount : ", self.correct_amount)
    
    def unlock(self):
        ''' Unlocks the Turnstile '''
        self.exit_state()
        return UnlockedState()
    
    def exit_state(self):
        ''' Flushed the value of amount '''
        self.amount = 0


class UnlockedState(State):
    '''
    The state in which the turnstile remains unlocked until the user passes it or an event of failure occurs.
    '''
    
    def coin_event(self, amount):
        print(self.thank_you_msg())
        return self
    
    def failed_event(self):
        print(self.out_of_order_msg())
        return BrokenState()
    
    def pass_event(self):
        return self.lock()
    
    def lock(self):
        ''' Locks the Turnstile '''
        return LockedState()


class BrokenState(State):
    '''
    The state in which the turnstile remains broken until fixed by a mechanic
    '''
    
    def fixed_event(self):
        print(self.in_order_msg())
        return LockedState()
