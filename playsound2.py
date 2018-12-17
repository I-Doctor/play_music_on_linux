#!/usr/bin/env python
# coding: utf-8
# sudo apt-get install mplayer

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import os

can_fly_path = 'I_believe_I_can_fly.mp3'	# I believe I can fly
cant_fly_path = 'falling_from_cloud.mp3'	# Wide Awake

os.system('mplayer %s' % can_fly_path)

os.system('mplayer %s' % cant_fly_path)

