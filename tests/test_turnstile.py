import os
import sys
import pytest
sys.path.append(os.path.dirname(__file__))

from turnstile import Turnstile
from turnstile_states import LockedState, UnlockedState, BrokenState


@pytest.fixture(scope='function')
def turnstile_object():
    turnstile = Turnstile()
    return turnstile


def test_turnstile_class_and_state(turnstile_object):
    assert isinstance(turnstile_object, Turnstile)
    assert isinstance(turnstile_object.state, LockedState)


def test_turnstile_flow(turnstile_object):
    turnstile_object.pass_event()
    assert isinstance(turnstile_object.get_state(), LockedState)

    turnstile_object.failed_event()
    assert isinstance(turnstile_object.get_state(), BrokenState)

    turnstile_object.pass_event()
    assert isinstance(turnstile_object.get_state(), BrokenState)

    turnstile_object.coin_event(2)
    assert isinstance(turnstile_object.get_state(), BrokenState)

    turnstile_object.failed_event()
    assert isinstance(turnstile_object.get_state(), BrokenState)

    turnstile_object.fixed_event()
    assert isinstance(turnstile_object.get_state(), LockedState)

    turnstile_object.coin_event(0.5)
    assert isinstance(turnstile_object.get_state(), LockedState)

    turnstile_object.coin_event(0.4)
    assert isinstance(turnstile_object.get_state(), LockedState)

    turnstile_object.coin_event(1)
    assert isinstance(turnstile_object.get_state(), UnlockedState)

    turnstile_object.failed_event()
    assert isinstance(turnstile_object.get_state(), BrokenState)

    turnstile_object.fixed_event()
    assert isinstance(turnstile_object.get_state(), LockedState)

    turnstile_object.coin_event(2)
    assert isinstance(turnstile_object.get_state(), UnlockedState)

    turnstile_object.coin_event(2)
    assert isinstance(turnstile_object.get_state(), UnlockedState)

    turnstile_object.pass_event()
    assert isinstance(turnstile_object.get_state(), LockedState)
