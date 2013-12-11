import wx
import random
from wx.lib.expando import ExpandoTextCtrl, EVT_ETC_LAYOUT_NEEDED


def randColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


class TextPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)

        self.textCtrl = ExpandoTextCtrl(self, size=(parent.Size[0]-20, -1))
        # self.Bind(EVT_ETC_LAYOUT_NEEDED, self.OnRefit, self.textCtrl)
        self.textCtrl.SetBackgroundColour((240, 240, 240))

        box = wx.BoxSizer()
        box.Add(self.textCtrl, 1, wx.EXPAND, 0)
        self.SetSizer(box)
        self.textCtrl.AppendText('1234 56 7890123 45678901234567912345679')


class RulerPanel(wx.Panel):
    def __init__(self, parent, id, style=0):
        wx.Panel.__init__(self, parent, id)
        self.style = style
        self.text = wx.StaticText(self, -1, '0', (40, 60))
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetMinSize((20, 30))

    def OnPaint(self, event):
        # anti aliasing
        pdc = wx.PaintDC(self)
        try:
            dc = wx.GCDC(pdc)
        except:
            dc = pdc

        dc.SetPen(wx.Pen('blue'))

        if self.style == 1:  # Top
            dc.DrawLine(0, 15, self.Size[0], 15)
            dc.DrawLine(self.Size[0]/2, 15, self.Size[0]/2, self.Size[1])
        elif self.style == 2:  # Mid
            dc.DrawLine(self.Size[0]/2, 0, self.Size[0]/2, self.Size[1])
            dc.DrawLine(self.Size[0]/2, 15, self.Size[0], 15)
        elif self.style == 3:  # Bottom
            dc.DrawLine(self.Size[0]/2, 0, self.Size[0]/2, 15)
            dc.DrawLine(self.Size[0]/2, 15, self.Size[0], 15)
        else:  # Single
            dc.DrawLine(0, 15, self.Size[0], 15)


class ContentsPanel(wx.Panel):
    def __init__(self, parent, id, pos=(0, 0), size=(100, 50), style=0):
        wx.Panel.__init__(self, parent, id, pos=pos, size=size)

        rulerPanel = RulerPanel(self, -1, style=style)
        textPanel = TextPanel(self, -1)

        hbox = wx.BoxSizer()
        hbox.Add(rulerPanel, 0, wx.EXPAND, 0)
        hbox.Add(textPanel, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.SetSizer(hbox)

        self.Bind(EVT_ETC_LAYOUT_NEEDED, self.OnRefit)
        self.OnRefit(EVT_ETC_LAYOUT_NEEDED)

    def OnRefit(self, evt):
        self.Fit()
        print 'Contents:' , self.Size



class TreeLayout(wx.Panel):
    def __init__(self, parent, id, text):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour('#ededed')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(hbox)

        contentPanel = ContentsPanel(self, -1, size=(200, -1))

        self.subPanel = wx.Panel(self, -1)
        self.subPanel.SetBackgroundColour(randColor())

        hbox.Add(contentPanel, 0, wx.EXPAND | wx.ALL, 2)
        hbox.Add(self.subPanel, 1, wx.EXPAND | wx.ALL, 2)

        self.contents = wx.BoxSizer(wx.VERTICAL)
        self.subPanel.SetSizer(self.contents)


class TreeLayoutFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 400))

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
