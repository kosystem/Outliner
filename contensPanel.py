import wx
from wx.lib.expando import ExpandoTextCtrl, EVT_ETC_LAYOUT_NEEDED


class LeftPanel(wx.Panel):
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
        textPanel = LeftPanel(self, -1)

        hbox = wx.BoxSizer()
        hbox.Add(rulerPanel, 0, wx.EXPAND, 0)
        hbox.Add(textPanel, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.SetSizer(hbox)

        self.Bind(EVT_ETC_LAYOUT_NEEDED, self.OnRefit)
        self.OnRefit(EVT_ETC_LAYOUT_NEEDED)

    def OnRefit(self, evt):
        self.Fit()
        print 'Contents:' , self.Size


class Communicate(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(380, 200))

        panel = wx.Panel(self, -1)

        ContentsPanel(panel, -1, pos=(0, 0), size=(200, -1))
        ContentsPanel(panel, -1, pos=(200, 0), size=(100, -1), style=1)
        contentsPanel = ContentsPanel(panel, -1, style=2)
        contentsPanel.SetPosition((200, 50))
        ContentsPanel(panel, -1, pos=(200, 100), size=(100, -1), style=3)

        # hbox = wx.BoxSizer()
        # hbox.Add(rightPanel, 1, wx.EXPAND | wx.ALL, 0)
        # hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 0)

        # panel.SetSizer(hbox)
        self.Centre()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()
    Communicate(None, -1, 'communicate.py')
    app.MainLoop()
