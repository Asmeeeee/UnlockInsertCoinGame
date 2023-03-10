# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2, Action3
from mud.events import OpenEvent, OpenWithEvent, OpenWithEvent2


class OpenAction(Action2):
    EVENT = OpenEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "open"


class OpenWithAction(Action3):
    EVENT = OpenWithEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"
    ACTION = "open-with"

class OpenWithAction2(Action3):

    def __init__(self, subject, object, object2):
        Action3.__init__(self, subject, object2, object)

    EVENT = OpenWithEvent2
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"
    ACTION = "open-with2"