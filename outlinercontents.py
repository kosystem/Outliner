
IMAGE_ALIGNMENT_BOTTOM = 0
IMAGE_ALIGNMENT_TOP = 1
IMAGE_ALIGNMENT_LEFT = 2
IMAGE_ALIGNMENT_RIGHT = 3


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

    def __str__(self):
        returnStr = "{\n"
        returnStr += ('"setting": ' + str(self.settings))
        if len(self.contents) > 0:
            returnStr += ', \n'
            returnStr += '"contents": [\n'
            for x in self.contents:
                returnStr += str(x)
                if x != self.contents[-1]:
                    returnStr += ','
                else:
                    returnStr += ']\n'
        else:
            returnStr += '\n'

        returnStr += '}\n'
        return returnStr


class OutlinerContents(object):
    """docstring for olContents"""
    def __init__(self, text=''):
        self.text = text
        self.font = ''
        self.fontSize = -1
        self.check = None
        self.closed = False
        self.parent = None
        self.imageURL = ''
        self.imageAlignments = IMAGE_ALIGNMENT_BOTTOM
        self.subContents = []

    def appendSubContents(self, contents):
        self.subContents.append(contents)
        contents.parent = self

    def insertSubContents(self, index, contents):
        if index >= len(self.subContents):
            self.subContents.append(contents)
        else:
            self.subContents.insert(index, contents)
        contents.parent = self

    def removeSubContetns(self, index):
        if index < len(self.subContents):
            return self.subContents.pop(index)
        else:
            return False

    def __str__(self):
        returnStr = "{\n"
        returnStr += ('"text": "' + self.text + '", \n')
        returnStr += ('"font": "' + self.font + '", \n')
        returnStr += ('"fontSize": ' + str(self.fontSize) + ', \n')
        if self.check is None:
            returnStr += '"check": null,\n'
        else:
            returnStr += ('"check": ' + str(self.check) + ', \n')
        returnStr += ('"closed": ' + str(self.closed).lower() + ', \n')
        returnStr += ('"imageURL": "' + self.imageURL + '", \n')
        returnStr += ('"imageAlignments": ' + str(self.imageAlignments))
        # returnStr += ('"parent": ' + self.parent + ', \n')
        if len(self.subContents) > 0:
            returnStr += ', \n'
            returnStr += '"subContents": [\n'
            for x in self.subContents:
                returnStr += str(x)
                if x != self.subContents[-1]:
                    returnStr += ','
                else:
                    returnStr += ']\n'
        else:
            returnStr += '\n'

        returnStr += '}\n'
        return returnStr


if __name__ == '__main__':
    base = OutlinerBase()
    contents = OutlinerContents('1st contents')
    contents.appendSubContents(OutlinerContents('sub contents 1'))
    contents.appendSubContents(OutlinerContents('sub contents 2'))
    contents.appendSubContents(OutlinerContents('sub contents 3'))
    base.appendContents(contents)
    temp = base.contents[0].removeSubContetns(1)
    contents.insertSubContents(0, temp)
    print base
