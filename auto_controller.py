import pyautogui
import win32gui
import pyautogui as pat
import time
class AutoController():
    def __init__(self):
        self.find_pal4_hwnd()

        self.rotate_mouse_start_x = int(self.window_loc_X + self.window_size_W * 0.2)
        self.rotate_neg_mouse_start_x = int(self.window_loc_X + self.window_size_W * 0.8)
        self.rotate_mouse_end_x = int(self.window_loc_X + self.window_size_W * 0.8)
        self.rotate_neg_mouse_end_x = int(self.window_loc_X + self.window_size_W * 0.2)
        self.rotate_mouse_start_y = int(self.window_loc_Y + self.window_size_H * 0.3)

        self.move_mouse_click_x = int(self.window_loc_X + self.window_size_W * 0.5)
        self.move_mouse_click_y = int(self.window_loc_Y + self.window_size_H * 0.3)

        self.abord_click_x = int(self.window_loc_X + self.window_size_W * 0.7)
        self.abord_click_y = int(self.window_loc_Y + self.window_size_H * 0.7)

        self.time_per_step = 2.5 / 8  # move 8 step using 2.5 seconds
        self.pixel_per_angle = 427 / 90 # rotate 90 degree using 427 pixels

        self.read_saving_time = 4

    def find_pal4_hwnd(self):
        hwnd = win32gui.FindWindow(None, "PAL4-Application")
        rect = win32gui.GetWindowRect(hwnd)
        self.window_loc_X = rect[0]
        self.window_loc_Y = rect[1]
        self.window_size_W = rect[2] - self.window_loc_X
        self.window_size_H = rect[3] - self.window_loc_Y


    def move(self, step):
        pat.moveTo(self.move_mouse_click_x, self.move_mouse_click_y)

        sleep_time = step * self.time_per_step

        pat.mouseDown()
        time.sleep(sleep_time)
        pat.mouseUp()

    def rotate(self, angle):
        pixels = int(self.pixel_per_angle * angle)

        if angle < 0:
            max_drag_pixel = self.rotate_neg_mouse_end_x - self.rotate_neg_mouse_start_x
        else:
            max_drag_pixel = self.rotate_mouse_end_x - self.rotate_mouse_start_x

        drag_time = int(pixels / max_drag_pixel)

        start_y = self.rotate_mouse_start_y
        end_y = self.rotate_mouse_start_y

        if angle < 0:
            start_x = self.rotate_neg_mouse_start_x
        else:
            start_x = self.rotate_mouse_start_x

        rest_pixels = pixels

        for i in range(drag_time):
            end_x = int(start_x + max_drag_pixel)

            rest_pixels = rest_pixels - (end_x - start_x)

            pat.moveTo(start_x, start_y)

            duration = abs((end_x - start_x)) / 500  ## 500 pixels per seconds
            pat.dragTo(end_x, end_y, duration, button="right")

        end_x = int(start_x + rest_pixels)
        pat.moveTo(start_x, start_y)
        duration = abs((end_x - start_x)) / 500  ## 500 pixels per seconds
        pat.dragTo(end_x, end_y, duration, button="right")

    def read_savings(self):
        time.sleep(self.read_saving_time)

    def click(self, x, y):
        pat.moveTo(x, y)
        pat.click()
        time.sleep(0.1)
        pat.mouseUp()

    def abord(self):
        pat.moveTo(self.abord_click_x, self.abord_click_y)
        pat.click(button="right")
        time.sleep(0.1)
        pat.mouseUp(button="right")

    def auto_playing(self):
        pass

    def screen_shot(self, region="default"):
        if region == "default":
            return pyautogui.screenshot(region=(self.window_loc_X, self.window_loc_Y, self.window_size_W, self.window_size_H))
        else:
            pass

if __name__ == '__main__':
    time.sleep(2)
    ac = AutoController()
    ac.rotate(360)