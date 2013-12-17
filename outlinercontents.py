

class OutlinerBase(object):
    def __init__(self):
        self.settings = {}
        self.contents = []

    def appendContents(self, contents):
        self.contents.append(contents)

    def insertContents(self, index, contents):
        if index >= len(self.subContents):
            self.appendContents(contents)
        else:
            self.contents.insert(index, contents)

    def removeContents(self, index):
        if index < len(self.contents):
            self.contents.pop(index)


class OutlinerContents(object):
    """docstring for olContents"""
    def __init__(self):
        self.text = ''
        self.font = ''
        self.fontSize = ''
        self.check = None
        self.imageURL = ''
        self.imageAlignments = 0  # bottom / top / L / R
        self.closed = False
        self.parent = None
        self.subContents = []

    def appendSubContents(self, contents):
        self.subContents.append(contents)

    def insertSubContents(self, index, contents):
        if index >= len(self.subContents):
            self.appendSubContents(contents)
        else:
            self.appendSubContents.insert(index, contents)

    def removeSubContetns(self, index):
        if index < len(self.subContents):
            self.subContents.pop(index)


if __name__ == '__main__':
    base = OutlinerBase()
    base.appendContents(OutlinerContents())

