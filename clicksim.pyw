import wx
import pyautogui
import time

def get_pos():
    time.sleep(1)
    x, y = pyautogui.position()
    return x, y

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(240, 150))
        
        self.pos1 = (0,0)
        self.pos2 = (0,0)
        self.pos3 = (0,0)
        
        panel = wx.Panel(self)
        
        self.button1 = wx.Button(panel, label="Get Pos 1", pos=(50, 0))
        self.button2 = wx.Button(panel, label="Get Pos 2", pos=(50, 30))
        self.button3 = wx.Button(panel, label=">>", pos=(50, 60))

        self.button1.Bind(wx.EVT_BUTTON, self.on_button1_click)
        self.button2.Bind(wx.EVT_BUTTON, self.on_button2_click)
        self.button3.Bind(wx.EVT_BUTTON, self.on_button3_click)

    def on_button1_click(self, event):
        x, y = get_pos()
        self.pos1 = (x,y)
        self.button1.SetLabel("%d, %d" %(x,y))

    def on_button2_click(self, event):
        x, y = get_pos()
        self.pos2 = (x,y)
        self.button2.SetLabel("%d, %d" %(x,y))

    def on_button3_click(self, event):
        x, y = pyautogui.position()
        self.pos3 = (x, y)
        pyautogui.click(x = self.pos1[0], y = self.pos1[1])
        pyautogui.click(x = self.pos2[0], y = self.pos2[1])
        pyautogui.moveTo(self.pos3[0],self.pos3[1])

app = wx.App()
frame = MyFrame(None, "clicksim")
frame.Show()
app.MainLoop()