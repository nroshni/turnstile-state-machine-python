# -*- coding: utf-8 -*-

class Events:
    '''
    Provides Utility functions for the events occuring in a Turnstile
    '''
    
    def pass_event(self):
        '''
        Utility function to handle the event of a person passing the
        turnstile machine
        '''
        return self
    
    def coin_event(self, amount):
        '''
        Utility function to handle the event of coin insertion
        '''
        return self
    
    def failed_event(self):
        '''
        Utility function to handle the event of machine failure
        '''
        return self
    
    def fixed_event(self):
        '''
        Utility function to handle the event of machine fixture
        '''
        return self
