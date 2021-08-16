import time
from auto_controller import AutoController

class ShenNongDongController(AutoController):
    def __init__(self):
        super(ShenNongDongController, self).__init__()

        self.enter_scene_x = self.window_loc_X + self.window_size_W * 0.5
        self.enter_scene_y = self.window_loc_Y + self.window_size_H * 0.4368048533872599

        self.shengnongmap_x = self.window_loc_X + self.window_size_W * 0.49222395023328147
        self.shengnongmap_y = self.window_loc_Y + self.window_size_H * 0.4954499494438827

        self.saving_inside_x = self.window_loc_X + self.window_size_W * 0.5
        self.saving_inside_y = self.window_loc_Y + self.window_size_H * 0.679474216380182

        self.saving_ok_x = self.window_loc_X + self.window_size_W * 0.4214618973561431
        self.saving_ok_y = self.window_loc_Y + self.window_size_H * 0.5116279069767442

        self.saving_x = self.window_loc_X + self.window_size_W * 0.5194401244167963
        self.saving_y = self.window_loc_Y + self.window_size_H * 0.538928210313448

        #self.read_saving_time = 5

    def auto_playing(self):
        time.sleep(3)

        self.move(1)
        self.rotate(86)
        self.move(6)

        self.click(self.saving_x, self.saving_y)
        self.click(self.saving_inside_x, self.saving_inside_y)
        self.click(self.saving_ok_x, self.saving_ok_y)

        self.abord()

        self.move(3)

        for i in range(4):
            self.abord()
            time.sleep(0.2)

        self.rotate(180)

        self.move(8)
        self.rotate(-90)

        self.move(5)

        self.click(self.enter_scene_x, self.enter_scene_y)
        self.click(self.shengnongmap_x, self.shengnongmap_y)
        self.click(self.saving_ok_x, self.saving_ok_y)

        self.read_savings()




if __name__ == '__main__':
    ac = ShenNongDongController()
    for i in range(50):
        ac.auto_playing()

    #print((1206 - ac.window_loc_X)/ac.window_size_W)
    #print((569 - ac.window_loc_Y)/ac.window_size_H)
