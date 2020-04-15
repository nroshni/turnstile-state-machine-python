import os
import sys
import pytest
sys.path.append(os.path.dirname(__file__))
from actions import Actions


@pytest.fixture(scope='module')
def action_object():
    action = Actions()
    return action


def test_instance_class(action_object):
    assert isinstance(action_object, Actions)


def test_alarm_msg(action_object):
    msg = action_object.alarm_msg()
    assert (msg == 'Alarm! Sorry, You are not allowed to pass.')
    assert isinstance(msg, str)


def test_thank_you_msg(action_object):
    msg = action_object.thank_you_msg()
    assert (msg == 'Thank you!')
    assert isinstance(msg, str)


def test_out_of_order_msg(action_object):
    msg = action_object.out_of_order_msg()
    assert (msg == 'Turnstile is out-of-order')
    assert isinstance(msg, str)


def test_in_order_msg(action_object):
    msg = action_object.in_order_msg()
    assert (msg == 'Turnstile is back in order')
    assert isinstance(msg, str)
