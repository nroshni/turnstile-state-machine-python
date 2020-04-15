import os
import sys
import pytest
sys.path.append(os.path.dirname(__file__))
from events import Events


@pytest.fixture(scope='module')
def event_object():
    event = Events()
    return event


def test_instance_class(event_object):
    assert isinstance(event_object, Events)


def test_pass_event(event_object):
    obj = event_object.pass_event()
    assert isinstance(obj, Events)


def test_coin_event(event_object):
    obj = event_object.coin_event(10)
    assert isinstance(obj, Events)


def test_failed_event(event_object):
    obj = event_object.failed_event()
    assert isinstance(obj, Events)


def test_fixed_event(event_object):
    obj = event_object.fixed_event()
    assert (isinstance(obj, Events))
