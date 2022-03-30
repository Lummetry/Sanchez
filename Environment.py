import numpy as np
import time
import cv2 as cv

import constants as ct
from Actor import Actor


class Environment:
  def __init__(self, name='', h=720, w=1280, actors=None, seconds_per_turn=1, background=None):
    self._last_map = None
    self.name = name
    self.h = h
    self.w = w
    self.actors = actors if actors is not None else []
    self.background = background if background is not None else ct.WHITE
    self.seconds_per_turn = seconds_per_turn
    self.running = False

    self._map = np.full((h, w, 3), self.background, np.uint8)
    self._last_map = self._map

    self.img = None

  def add_actor(self, actor):
    self.actors.append(actor)

  def _check_collisions(self):
    N = len(self.actors)
    for i in range(N):
      for j in range(i + 1, N):
        if self.actors[i].check_collision(self.actors[j]):
          self.actors[i].change_direction()
          self.actors[j].change_direction()

  def _reset_map(self):
    for actor in self.actors:
      xmin, xmax, ymin, ymax = actor.get_coords()
      self._map[xmin: xmax, ymin: ymax] = self.background

  def _update_map(self):
    for actor in self.actors:
      xmin, xmax, ymin, ymax = actor.get_coords()
      self._map[xmin: xmax, ymin: ymax] = actor.color

    self._last_map = self._map

  def get_map(self):
    return self._last_map

  def stop(self):
    self.running = False
    print('Env should stop')

  def start(self, turn_limit=None):
    self._update_map()

    self.running = True
    turn_count = 0
    while self.running and (turn_limit is None or turn_count < turn_limit):
      self._reset_map()

      for actor in self.actors:
        actor.forward(self.h, self.w)

      self._check_collisions()

      self._update_map()
      turn_count += 1
      time.sleep(self.seconds_per_turn)
      print(f'Done turn #{turn_count}')

    print(f'Environment {self.name} stopped after {turn_count} turns.')










