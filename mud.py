#! /usr/bin/env python3
import mud.game
import mud.server
mud.game.GAME = mud.game.Game("Insert-Coin")
mud.game.GAME.load()
mud.game.GAME.start()