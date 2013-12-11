import wx
import random


def randColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


class TreeLayout(wx.Panel):
    def __init__(self, parent, id, text):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour('#ededed')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(hbox)

        contentPanel = wx.StaticText(self, -1, text, size=(50, 50))

        self.subPanel = wx.Panel(self, -1)
        self.subPanel.SetBackgroundColour(randColor())

        hbox.Add(contentPanel, 0, wx.EXPAND | wx.ALL, 2)
        hbox.Add(self.subPanel, 1, wx.EXPAND | wx.ALL, 2)

        self.contents = wx.BoxSizer(wx.VERTICAL)
        self.subPanel.SetSizer(self.contents)


class TreeLayoutFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(380, 200))

        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour(randColor())
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan1 = TreeLayout(panel, -1, '1')
        midPan2 = TreeLayout(panel, -1, '2')
        midPan11 = TreeLayout(midPan1.subPanel, -1, '11')
        midPan21 = TreeLayout(midPan2.subPanel, -1, '21')
        midPan22 = TreeLayout(midPan2.subPanel, -1, '22')
        midPan23 = TreeLayout(midPan2.subPanel, -1, '22')
        midPan24 = TreeLayout(midPan2.subPanel, -1, '22')
        midPan1.contents.Add(midPan11, 1, wx.EXPAND | wx.ALL, 2)
        midPan2.contents.Add(midPan21, 1, wx.EXPAND | wx.ALL, 2)
        midPan2.contents.Add(midPan22, 1, wx.EXPAND | wx.ALL, 2)
        midPan2.contents.Add(midPan23, 1, wx.EXPAND | wx.ALL, 2)
        midPan2.contents.Add(midPan24, 1, wx.EXPAND | wx.ALL, 2)

        vbox.Add(midPan1, 0, wx.EXPAND | wx.ALL, 2)
        vbox.Add(midPan2, 0, wx.EXPAND | wx.ALL, 2)
        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)


if __name__ == '__main__':
    app = wx.App()
    TreeLayoutFrame(None, -1, 'layout.py')
    app.MainLoop()
