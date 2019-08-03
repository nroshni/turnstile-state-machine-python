# -*- coding: utf-8 -*-

from actions import Actions
from events import Events

class State(Actions, Events):
    '''
    Provides utility functions for the individual states of the state machine
    '''
    
    def __init__(self):
        '''
        Entry function of each state
        '''
        print('Updating state to : ', str(self))
    
    def __str__(self):
        '''
        Returns the name of the state
        '''
        return self.__class__.__name__
    
    def __repr__(self):
        '''
        Uses the __str__ method to describe the State.
        '''
        return self.__str__()
