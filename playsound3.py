#!/usr/bin/env python
# coding: utf-8
# sudo apt-get install sox
# sudo apt-get install libsox-fmt-all

import os
import time

music_player = "./music_player" 

if os.path.exists(music_player):
	print "   play can fly"
	os.system(music_player + ' y')

if os.path.exists(music_player):
	print "   play can fly"
	os.system(music_player + ' n')
