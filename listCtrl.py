import wx


class Communicate(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(380, 200))

        listCtrl = wx.ListCtrl(self, style=wx.LC_REPORT)

        listCtrl.InsertColumn(0, "LackyStar")
        listCtrl.InsertColumn(1, "Familyname")
        listCtrl.SetColumnWidth(0, -2)
        listCtrl.SetColumnWidth(1, -2)

        self.Centre()
        self.Show(True)


if __name__ == '__main__':
    app = wx.App()
    Communicate(None, -1, 'communicate.py')
    app.MainLoop()
