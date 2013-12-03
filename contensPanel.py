import wx


class LeftPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)

        self.text = parent.GetParent().rightPanel.text

        button1 = wx.Button(self, -1, '+', (10, 10))
        button2 = wx.Button(self, -1, '-', (10, 60))

        self.Bind(wx.EVT_BUTTON, self.OnPlus, id=button1.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnMinus, id=button2.GetId())

    def OnPlus(self, event):
        value = int(self.text.GetLabel())
        value = value + 1
        self.text.SetLabel(str(value))

    def OnMinus(self, event):
        value = int(self.text.GetLabel())
        value = value - 1
        self.text.SetLabel(str(value))


class RightPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        self.text = wx.StaticText(self, -1, '0', (40, 60))
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        # anti aliasing
        pdc = wx.PaintDC(self)
        try:
            dc = wx.GCDC(pdc)
        except:
            dc = pdc

        dc.SetPen(wx.Pen('blue'))
        for i in range(10):
            y = 20*i + 1
            dc.DrawLine(0, y, 200, y)
        for i in range(11):
            x = 20*i
            dc.DrawLine(x, 0, x, 180)
        dc.SetPen(wx.Pen('red'))
        dc.DrawLine(0, 0, 200, 180)


class Communicate(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(380, 200))

        panel = wx.Panel(self, -1)
        self.rightPanel = RightPanel(panel, -1)

        leftPanel = LeftPanel(panel, -1)

        hbox = wx.BoxSizer()
        hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(hbox)
        self.Centre()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()
    Communicate(None, -1, 'communicate.py')
    app.MainLoop()
