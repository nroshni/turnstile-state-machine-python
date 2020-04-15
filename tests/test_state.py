import os
import sys
import pytest
sys.path.append(os.path.dirname(__file__))

import test_events
import test_actions
from state import State


@pytest.fixture(scope='module')
def state_object():
    state = State()
    return state


def test_instance_class(state_object):
    # Testing for inheritance
    assert isinstance(state_object, State)
    test_actions.test_instance_class(state_object)
    test_events.test_instance_class(state_object)


def test_action_functions(state_object):
    test_actions.test_alarm_msg(state_object)
    test_actions.test_thank_you_msg(state_object)
    test_actions.test_out_of_order_msg(state_object)
    test_actions.test_in_order_msg(state_object)


def test_event_functions(state_object):
    test_events.test_pass_event(state_object)
    test_events.test_coin_event(state_object)
    test_events.test_failed_event(state_object)
    test_events.test_fixed_event(state_object)
