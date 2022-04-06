import cv2 as cv


class Render:
  def __init__(self, env=None, window_name='', frame_rate=1):
    self.environment = env
    self.window_name = window_name
    self.frame_rate = frame_rate
    self._running = False

  def is_running(self):
    return self._running

  def stop(self):
    self._running = False

  def run(self):
    wait_time = 1000 / self.frame_rate
    self._running = True

    while self._running:
      print('Iteration on Render loop')
      curr_map = self.environment.get_map()
      if curr_map is not None:
        cv.imshow(self.window_name, self.environment.get_map())

        if cv.waitKey(int(wait_time)) & 0xFF == 27:
          self.stop()

    cv.destroyAllWindows()
    # self.environment.stop()

