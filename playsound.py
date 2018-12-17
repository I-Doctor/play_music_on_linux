#!/usr/bin/env python
# coding: utf-8
# sudo pip install pygame

import pygame
import time

pygame.mixer.init()
can_fly_path = 'I_believe_I_can_fly.mp3'	# I believe I can fly
cant_fly_path = 'falling_from_cloud.mp3'	# Wide Awake

pygame.mixer.music.load(can_fly_path)
pygame.mixer.music.play()
time.sleep(8)

pygame.mixer.music.load(cant_fly_path)
pygame.mixer.music.play()
time.sleep(8)
