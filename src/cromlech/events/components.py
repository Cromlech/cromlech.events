# -*- coding: utf-8 -*-

from cromlech.events import interfaces
from zope.interface import implementer
from zope.interface.interfaces import ObjectEvent


@implementer(interfaces.IAttributes)
class Attributes(object):
    """
    Describes modified attributes of an interface.

        >>> from cromlech.events.interfaces import IObjectMovedEvent
        >>> desc = Attributes(IObjectMovedEvent, "newName", "newParent")
        >>> desc.interface == IObjectMovedEvent
        True
        >>> 'newName' in desc.attributes
        True
    """

    def __init__(self, interface, *attributes):
        self.interface = interface
        self.attributes = attributes


@implementer(interfaces.IObjectCreatedEvent)
class ObjectCreatedEvent(ObjectEvent):
    """An object has been created.
    """


@implementer(interfaces.IObjectAddedEvent)
class ObjectAddedEvent(ObjectEvent):
    """An object has been added to a container.
    """
    def __init__(self, object, newParent=None, newName=None):
        ObjectEvent.__init__(self, object)
        if newParent is None:
            newParent = getattr(object, '__parent__', None)
        if newName is None:
            newName = getattr(object, '__name__', None)


@implementer(interfaces.IObjectModifiedEvent)
class ObjectModifiedEvent(ObjectEvent):
    """An object has been modified.
    """
    def __init__(self, object, *descriptions):
        super(ObjectModifiedEvent, self).__init__(object)
        self.descriptions = descriptions


@implementer(interfaces.IObjectCopiedEvent)
class ObjectCopiedEvent(ObjectCreatedEvent):
    """An object has been copied.
    """
    def __init__(self, object, original):
        super(ObjectCopiedEvent, self).__init__(object)
        self.original = original


@implementer(interfaces.IObjectMovedEvent)
class ObjectMovedEvent(ObjectAddedEvent):
    """An object has been moved.
    """
    def __init__(self, object, oldParent, oldName, newParent, newName):
        ObjectAddedEvent.__init__(self, object, newParent, newName)
        self.oldParent = oldParent
        self.oldName = oldName


@implementer(interfaces.IObjectRemovedEvent)
class ObjectRemovedEvent(ObjectEvent):
    """An object has been removed.
    """
    def __init__(self, object, oldParent, oldName):
        ObjectEvent.__init__(self, object)
        self.oldParent = oldParent
        self.oldName = oldName


__all__ = ['Attributes',
           'ObjectCreatedEvent',
           'ObjectAddedEvent',
           'ObjectModifiedEvent',
           'ObjectCopiedEvent',
           'ObjectMovedEvent',
           'ObjectRemovedEvent']
