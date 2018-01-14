# -*- coding: utf-8 -*-

from crom import subscription, sources, target
from zope.event import subscribers as event_subscribers
from zope.interface import Interface
from zope.interface.interfaces import IObjectEvent


def dispatch(*events):
    for sub in Interface.subscription(*events):
        sub(*events)


def setup_dispatcher():
    if dispatch not in event_subscribers:
        event_subscribers.append(dispatch)


def teardown_dispatcher():
    if dispatch in event_subscribers:
        event_subscribers.remove(dispatch)


@subscription
@sources(IObjectEvent)
@target(Interface)
def objectEventNotify(event):
    """Dispatch ObjectEvents to interested adapters.
    """
    for handler in Interface.subscription(event.object, event):
        handler(event.object, event)
