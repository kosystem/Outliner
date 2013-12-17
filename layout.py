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

        self.textCtrl = ExpandoTextCtrl(
            self,
            size=(parent.Size[0]-20, -1),
            style=wx.BORDER_NONE |
            wx.TE_NO_VSCROLL)
        # self.Bind(EVT_ETC_LAYOUT_NEEDED, self.OnRefit, self.textCtrl)
        self.textCtrl.SetBackgroundColour('#e0e0e0')

        box = wx.BoxSizer()
        box.Add(self.textCtrl, 1, wx.EXPAND, 0)
        self.SetSizer(box)
        self.textCtrl.AppendText('1234 56 7890123 45678901234567912')


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

        dc.SetPen(wx.Pen('#a0a0a0'))

        heightMargin = 10
        width, height = self.Size[0], self.Size[1]
        if self.style == 1:  # Top
            dc.DrawLine(0, heightMargin, width, heightMargin)
            dc.DrawLine(width/2, heightMargin, width/2, height)
        elif self.style == 2:  # Mid
            dc.DrawLine(width/2, 0, width/2, height)
            dc.DrawLine(width/2, heightMargin, width, heightMargin)
        elif self.style == 3:  # Bottom
            dc.DrawLine(width/2, 0, width/2, heightMargin)
            dc.DrawLine(width/2, heightMargin, width, heightMargin)
        else:  # Single
            dc.DrawLine(0, heightMargin, width, heightMargin)


class ContentsPanel(wx.Panel):
    def __init__(self, parent, id, pos=(0, 0), size=(100, 50), style=0):
        wx.Panel.__init__(self, parent, id, pos=pos, size=size)
        self.SetBackgroundColour('#e0e0e0')

        rulerPanel = RulerPanel(self, -1, style=style)
        textPanel = TextPanel(self, -1)

        hbox = wx.BoxSizer()
        hbox.Add(rulerPanel, 0, wx.EXPAND, 0)
        hbox.Add(textPanel, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 2)

        self.SetSizer(hbox)

        self.Bind(EVT_ETC_LAYOUT_NEEDED, self.OnRefit, textPanel.textCtrl)
        self.OnRefit(EVT_ETC_LAYOUT_NEEDED)

    def OnRefit(self, evt):
        self.Fit()
        # print 'Contents:', self.Size


class TreeLayout(wx.Panel):
    def __init__(self, parent, id, text, style=0):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour('#ededed')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(hbox)

        contentPanel = ContentsPanel(self, -1, size=(200, -1), style=style)

        self.subPanel = wx.Panel(self, -1)
        self.subPanel.SetBackgroundColour(randColor())

        hbox.Add(contentPanel, 0, wx.EXPAND | wx.ALL, 0)
        hbox.Add(self.subPanel, 1, wx.EXPAND | wx.ALL, 0)

        self.contents = wx.BoxSizer(wx.VERTICAL)
        self.subPanel.SetSizer(self.contents)


class TreeLayoutFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 400))

        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour(randColor())
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan1 = TreeLayout(panel, -1, '1', style=1)
        midPan2 = TreeLayout(panel, -1, '2', style=3)
        midPan11 = TreeLayout(midPan1.subPanel, -1, '11')
        midPan21 = TreeLayout(midPan2.subPanel, -1, '21', style=1)
        midPan22 = TreeLayout(midPan2.subPanel, -1, '22', style=2)
        midPan23 = TreeLayout(midPan2.subPanel, -1, '23', style=2)
        midPan24 = TreeLayout(midPan2.subPanel, -1, '24', style=3)
        midPan1.contents.Add(midPan11, 1, wx.EXPAND | wx.ALL, 0)
        midPan2.contents.Add(midPan21, 1, wx.EXPAND | wx.ALL, 0)
        midPan2.contents.Add(midPan22, 1, wx.EXPAND | wx.ALL, 0)
        midPan2.contents.Add(midPan23, 1, wx.EXPAND | wx.ALL, 0)
        midPan2.contents.Add(midPan24, 1, wx.EXPAND | wx.ALL, 0)

        vbox.Add(midPan1, 0, wx.EXPAND | wx.ALL, 0)
        vbox.Add(midPan2, 0, wx.EXPAND | wx.ALL, 0)
        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)


if __name__ == '__main__':
    app = wx.App()
    TreeLayoutFrame(None, -1, 'layout.py')
    app.MainLoop()
