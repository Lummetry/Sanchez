import constants as ct
import math
import random


SIZE = 3


class Actor:
  def __init__(self, name='', color=None,
               x=0, y=0, alpha=0, beta=0,
               speed=0, period=0, steps=0):
    self.name = name
    self.color = color if color is not None else ct.LIGHT_BLUE
    self.x = x
    self.y = y
    self.alpha = alpha
    self.beta = beta
    self.speed = speed
    self.period = period
    self.steps = steps

  def _change_direction(self, h=0, w=0):
    rad = random.uniform(0, 2 * math.pi)
    s, c = math.sin(rad), math.cos(rad)

    alpha = c * self.alpha - s * self.beta
    beta = s * self.alpha + c * self.beta

    if h != 0:
      beta = h * abs(beta)
    if w != 0:
      alpha = w * abs(alpha)

    self.alpha, self.beta = alpha, beta

  def change_direction(self):
    self._change_direction()

  def _step_forward(self):
    self.x = self.x + self.speed * self.alpha
    self.y = self.y + self.speed * self.beta

  def _out_of_map(self, h, w):
    if self.x < 0 or self.y < 0:
      return True

    if h is not None and self.y >= h:
      return True
    if w is not None and self.x >= w:
      return True

    return False

  def forward(self, h=None, w=None):
    if self.steps % self.period < 1:
      self._change_direction()

    self._step_forward()

    while self._out_of_map(h, w):
      if self.y < 0:
        self._change_direction(h=1)
      if h is not None and self.y >= h:
        self._change_direction(h=-1)

      if self.x < 0:
        self._change_direction(w=1)
      if w is not None and self.x >= w:
        self._change_direction(w=-1)

      self._step_forward()  # stepping back into the map

    self.steps += 1

  def matrix_position(self):
    return round(self.x), round(self.y)

  def get_coords(self, h=None, w=None):
    x, y = self.matrix_position()
    xmin, xmax = x - SIZE, x + SIZE
    ymin, ymax = y - SIZE, y + SIZE
    xmin, ymin = max(xmin, 0), max(ymin, 0)

    if h is not None:
      ymax = min(ymax, h)
    if w is not None:
      xmax = min(xmax, w)

    return xmin, xmax, ymin, ymax


  def _head_collision(self, other):
    x1, y1 = self.matrix_position()
    x2, y2 = other.matrix_position()

    return x1 == x2 and y1 == y2

  def check_collision(self, other):
    return self._head_collision(other)

