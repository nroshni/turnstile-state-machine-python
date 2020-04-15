# -*- coding: utf-8 -*-

from turnstile_states import LockedState


class Turnstile():
    '''
    A turnstile machine with its capabilities
    '''
    def __init__(self):
        ''' Initialize the state '''
        self.state = LockedState()

    def coin_event(self, amount):
        ''' Performs a coin insertion event '''
        self.state = self.state.coin_event(amount)

    def pass_event(self):
        ''' Performs a Turnstile passing event '''
        self.state = self.state.pass_event()

    def failed_event(self):
        ''' Performs a Turnstile failing event '''
        self.state = self.state.failed_event()

    def fixed_event(self):
        ''' Performs a Turnstile fixing event '''
        self.state = self.state.fixed_event()

    def get_state(self):
        ''' Returns the current state of the Turnstile '''
        print("\nCurrent State (after event): ", self.state)
        return self.state


if __name__ == "__main__":
    ts = Turnstile()
    print(ts, ts.state)
