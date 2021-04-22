# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .effect import Effect2, Effect3, Effect1
from mud.events import DropEvent, DropInEvent, ClearEvent

class DropEffect(Effect2):
    EVENT = DropEvent

class DropInEffect(Effect3):
    EVENT = DropInEvent

class ClearEffect(Effect1):
	EVENT = ClearEvent