# -*- coding: utf-8 -*-

class Actions:
    '''
    Provides Utility functions for the actions 
    performed by the Turnstile machine
    '''
    
    def alarm_msg(self):
        '''
        Utility function to genrate an alarm when encountered with
        a pass event in Locked State
        '''
        msg = "Alarm! Sorry, You are not allowed to pass."
        return msg
    
    def thank_you_msg(self):
        ''' Utility function to print Thank you message '''
        msg = "Thank you!"
        return msg
    
    def out_of_order_msg(self):
        ''' Utility function to print Out-of-Order message '''
        msg = "Turnstile is out-of-order"
        return msg
    
    def in_order_msg(self):
        ''' Utility function to print In-Order message '''
        msg = "Turnstile is back in order"
        return msg
