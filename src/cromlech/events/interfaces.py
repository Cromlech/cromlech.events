# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute
from zope.interface.interfaces import IObjectEvent


class IModifications(Interface):
    """ Marker interface for descriptions of object modifications.
    """


class IAttributes(IModifications):
    """ Describes the modified attributes of an interface.
    """
    interface = Attribute("The involved interface.")
    attributes = Attribute("A sequence of modified attributes.")


class IObjectCreatedEvent(IObjectEvent):
    """An object has been created.
    The location will usually be ``None`` for this event.
    """


class IObjectAddedEvent(IObjectEvent):
    """An object has been added to a container.
    """
    newParent = Attribute("The new location parent for the object.")
    newName = Attribute("The new location name for the object.")


class IObjectMovedEvent(IObjectAddedEvent):
    """An object has been moved.
    """
    oldParent = Attribute("The old location parent for the object.")
    oldName = Attribute("The old location name for the object.")


class IObjectCopiedEvent(IObjectCreatedEvent):
    """An object has been copied.
    """
    original = Attribute("The original from which the copy was made")


class IObjectModifiedEvent(IObjectEvent):
    """An object has been modified.
    """


class IObjectRemovedEvent(IObjectMovedEvent):
    """An object has been removed from a container.
    """
