# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .effect import Effect2
from mud.events import TakeEvent, TakeEvent2

class TakeEffect(Effect2):
    EVENT = TakeEvent

class TakeEffect2(Effect2):
    EVENT = TakeEvent2