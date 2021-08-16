### Pal4-auto
- 自制简易仙剑奇侠传4 自动刷怪脚本

### 环境

- python 3.7
- pyautogui

### demo - 狐仙居
进入狐仙居场景并从狐仙居出到即墨，运行`python huxianju.py`

<img src="https://github.com/lstcutong/Pal4-auto/blob/main/gifs/2~1%2000_00_00-00_00_30.gif?raw=true"/>

### demo - 神农洞
进入神农洞，并从神农洞御剑飞行到神农洞，运行`python shengnongdong.py`

<img src="https://github.com/lstcutong/Pal4-auto/blob/main/gifs/1~1%2000_00_00-00_00_30.gif?raw=true"/>



### 使用

```python
from auto_controller import AutoController

class YourController(AutoController):
    def _init_(self)
        super(YourController, self).__init__()
    	# your parameters here
        pass
    def auto_playing(self):
        self.rotate(30)     # 人物顺时针旋转30度
        self.rotate(-30)    # 人物逆时针旋转30度
        self.move(10)       # 人物向前移动10步
        self.click((100, 30))     # 鼠标点击屏幕坐标 (100, 30)处
        self.abord()        # 退出。例如存完档退出存档界面，或者是打怪结束快速结算
        self.read_savings() # 加载场景需调用此进行等待，否则可能会出现累积误差导致自动刷怪失败
        
ac = YourController()
# 开始10000次刷怪
for i in range(10000):
    ac.auto_playing()
```
