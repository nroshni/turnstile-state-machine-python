import os
import sys
import pytest
sys.path.append(os.path.dirname(__file__))

import test_state
import test_events
import test_actions
from turnstile_states import LockedState, UnlockedState, BrokenState


@pytest.fixture(scope='module')
def locked_object():
    locked = LockedState()
    return locked


@pytest.fixture(scope='module')
def unlocked_object():
    unlocked = UnlockedState()
    return unlocked


@pytest.fixture(scope='module')
def broken_object():
    broken = BrokenState()
    return broken


def test_locked_instance_class(locked_object):
    # Testing for inheritance
    assert isinstance(locked_object, LockedState)
    test_state.test_instance_class(locked_object)
    test_actions.test_instance_class(locked_object)
    test_events.test_instance_class(locked_object)


def test_unlocked_instance_class(unlocked_object):
    # Testing for inheritance
    assert isinstance(unlocked_object, UnlockedState)
    test_state.test_instance_class(unlocked_object)
    test_actions.test_instance_class(unlocked_object)
    test_events.test_instance_class(unlocked_object)


def test_broken_instance_class(broken_object):
    # Testing for inheritance
    assert isinstance(broken_object, BrokenState)
    test_state.test_instance_class(broken_object)
    test_actions.test_instance_class(broken_object)
    test_events.test_instance_class(broken_object)


def test_lockedstate_events(locked_object):
    assert isinstance(locked_object.fixed_event(), LockedState)
    assert isinstance(locked_object.pass_event(), LockedState)
    assert isinstance(locked_object.failed_event(), BrokenState)
    assert isinstance(locked_object.coin_event(0.5), LockedState)
    assert isinstance(locked_object.coin_event(10), UnlockedState)


def test_lockedstate_actions(locked_object):
    test_actions.test_alarm_msg(locked_object)
    test_actions.test_thank_you_msg(locked_object)
    test_actions.test_out_of_order_msg(locked_object)
    test_actions.test_in_order_msg(locked_object)


def test_unlockedstate_events(unlocked_object):
    assert isinstance(unlocked_object.fixed_event(), UnlockedState)
    assert isinstance(unlocked_object.pass_event(), LockedState)
    assert isinstance(unlocked_object.failed_event(), BrokenState)
    assert isinstance(unlocked_object.coin_event(10), UnlockedState)


def test_unlockedstate_actions(unlocked_object):
    test_actions.test_alarm_msg(unlocked_object)
    test_actions.test_thank_you_msg(unlocked_object)
    test_actions.test_out_of_order_msg(unlocked_object)
    test_actions.test_in_order_msg(unlocked_object)


def test_brokenstate_events(broken_object):
    assert isinstance(broken_object.fixed_event(), LockedState)
    assert isinstance(broken_object.pass_event(), BrokenState)
    assert isinstance(broken_object.failed_event(), BrokenState)
    assert isinstance(broken_object.coin_event(10), BrokenState)


def test_brokenstate_actions(broken_object):
    test_actions.test_alarm_msg(broken_object)
    test_actions.test_thank_you_msg(broken_object)
    test_actions.test_out_of_order_msg(broken_object)
    test_actions.test_in_order_msg(broken_object)
