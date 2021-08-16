import pyautogui as pat
import sys
import os
import time
from auto_controller import AutoController

class HuXianJuController(AutoController):
    def __init__(self):
        super(HuXianJuController, self).__init__()

        self.enter_scene_x = self.window_loc_X + self.window_size_W * 0.5
        self.enter_scene_y = self.window_loc_Y + self.window_size_H * 0.4398382204246714

        self.saving_x = self.window_loc_X + self.window_size_W * 0.47200622083981336
        self.saving_y = self.window_loc_Y + self.window_size_H * 0.6086956521739131

        self.saving_inside_x = self.window_loc_X + self.window_size_W * 0.5
        self.saving_inside_y = self.window_loc_Y + self.window_size_H * 0.679474216380182

        self.saving_ok_x = self.window_loc_X + self.window_size_W * 0.4214618973561431
        self.saving_ok_y = self.window_loc_Y + self.window_size_H * 0.5116279069767442

    def auto_playing(self):
        time.sleep(3)

        self.rotate(-160)
        self.move(3)

        self.click(self.enter_scene_x, self.enter_scene_y)

        self.read_savings()

        self.move(7)
        self.rotate(42)

        self.move(3)

        for i in range(2):
            self.abord()
            time.sleep(0.2)

        self.rotate(184)

        self.move(9)

        self.click(self.saving_x, self.saving_y)

        self.click(self.saving_inside_x, self.saving_inside_y)
        self.click(self.saving_ok_x, self.saving_ok_y)

        self.abord()

        self.rotate(-70)
        self.move(5)

        self.click(self.enter_scene_x, self.enter_scene_y)


if __name__ == '__main__':
    ac = HuXianJuController()

    #print((1054 - ac.window_loc_X)/ac.window_size_W)
    #print((541 - ac.window_loc_Y)/ac.window_size_H)
    for i in range(10000):
        print(i)
        ac.auto_playing()