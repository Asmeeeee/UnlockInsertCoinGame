# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .effect import Effect2, Effect3
from mud.events import OpenEvent, OpenWithEvent, OpenWithEvent2

class OpenEffect(Effect2):
    EVENT = OpenEvent

class OpenWithEffect(Effect3):
    EVENT = OpenWithEvent

class OpenWithEffect2(Effect3):
    EVENT = OpenWithEvent