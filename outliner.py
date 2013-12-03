import wx
import wx.xrc as xrc
import toXrc


class MyApp(wx.App):
    """docstring for MyApp"""
    def OnInit(self):
        f = open('ui.trc')
        krcString = f.read()
        f.close()
        toxrc = toXrc.toXRC()
        xrcString = toxrc.convert(krcString)
        print xrcString
        self.res = xrc.EmptyXmlResource()
        self.res.LoadFromString(xrcString)
        self.initFrame()
        return True

    def initFrame(self):
        self.frame = self.res.LoadFrame(None, 'mainFrame')
        self.frame.Show()


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
