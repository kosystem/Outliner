import wx
from wx.lib.agw import ultimatelistctrl as ULC


class TestUltimateListCtrl(ULC.UltimateListCtrl):
    def __init__(self, parent, log):
        ULC.UltimateListCtrl.__init__(self, parent, -1,
                                      agwStyle=wx.LC_REPORT |
                                      wx.LC_VIRTUAL |
                                      wx.LC_HRULES |
                                      wx.LC_VRULES)

        self.InsertColumn(0, "First")
        self.InsertColumn(1, "Second")
        self.InsertColumn(2, "Third")
        self.SetColumnWidth(0, 175)
        self.SetColumnWidth(1, 175)
        self.SetColumnWidth(2, 175)

        # After setting the column width you can specify that
        # this column expands to fill the window. Only one
        # column may be specified.
        self.SetColumnWidth(2, ULC.ULC_AUTOSIZE_FILL)

        self.SetItemCount(1000)

    #---------------------------------------------------
    # These methods are callbacks for implementing the
    # "virtualness" of the list...  Normally you would
    # determine the text, attributes and/or image based
    # on values from some external data source, but for
    # this demo we'll just calculate them

    def OnGetItemText(self, item, col):
        return "Item%d, column %d" % (item, col)

    def OnGetItemToolTip(self, item, col):
        return None

    def OnGetItemTextColour(self, item, col):
        return None

    def OnGetItemColumnImage(self, item, column):
        return []

#---------------------------------------------------------------------------


class TestFrame(wx.Frame):
    def __init__(self, parent, log):
        wx.Frame.__init__(self, parent, -1, "Ultimate", size=(700, 600))
        panel = wx.Panel(self, -1)
        sizer = wx.BoxSizer(wx.VERTICAL)

        listCtrl = TestUltimateListCtrl(panel, log)

        sizer.Add(listCtrl, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        sizer.Layout()

        self.CenterOnScreen()
        self.Show()


#---------------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    app = wx.App(0)
    frame = TestFrame(None, sys.stdout)
    frame.Show(True)
    app.MainLoop()
