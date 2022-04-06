"""
nickname: Sanchez
"""
import threading

from Actor import Actor
from Environment import Environment
from Render import Render

import constants as ct


"""
FUTURE TODO: add from user stones on sandbox that will be obstacles
"""


def demo(render: Render, env: Environment):
  th1 = threading.Thread(target=render.run)
  th2 = threading.Thread(target=env.start, args=(50,))

  th1.start()
  th2.start()

  th1.join()
  print('Render stopped')
  env.stop()
  th2.join()


if __name__ == '__main__':
  actors = [
    Actor('Gica', ct.RED, 50, 50, 1, 1, 2, 10),
    Actor('Radu', ct.GREEN, 22, 53, -2, 3, 5, 7)
  ]

  env = Environment('Scena', h=400, w=400, actors=actors, seconds_per_turn=0.2)
  render = Render(env, 'TV', frame_rate=1)

  # th = threading.Thread(target=render.run)
  #
  # th.start()
  # env.start(200)
  # th.join()
  demo(render, env)

