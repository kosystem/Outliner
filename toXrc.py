import re


class toXRC(object):
    """docstring for toXRC"""
    def __init__(self):
        super(toXRC, self).__init__()

    def convert(self, src):
        src += '</resource>\n'

        # comment
        for x in reversed(list(re.finditer(r'\s*#.*?$', src, re.MULTILINE))):
            src = src[:x.start()] + '\n' + src[x.end():]

        dist = ''
        # object close
        prev = 0
        for x in re.finditer(r'(.*)\n', src, 0):
            n = re.search(r'\w', x.group(1), 0)
            if n:
                while prev > n.start():
                    space = ''
                    for i in xrange(0, prev-4):
                        space = space + ' '
                    dist += space + '</object>\n'
                    prev -= 4
                prev = n.start()
                dist += x.group()

        # object class with name and subclass
        objectWithName = re.compile(
            r'^\s*(\w+):\n\s*name: (.+)\n\s*subclass: (.+)\n',
            re.MULTILINE)
        for n in reversed(list(objectWithName.finditer(dist))):
            dist = (
                dist[:n.start(1)] +
                '<object class="' + n.group(1) +
                '" name="' + n.group(2) +
                '" subclass="' + n.group(3) + '">\n' + dist[n.end():])

        # object class with name
        objectWithName = re.compile(
            r'^\s*(\w+):\n(\s*)name: (.+)\n',
            re.MULTILINE)
        for n in reversed(list(objectWithName.finditer(dist))):
            dist = (
                dist[:n.start(1)] + '<object class="' + n.group(1) +
                '" name="' + n.group(3) + '">\n' + dist[n.end():])

        # object class
        objectOnly = re.compile(
            r'^\s*(\w+):\n',
            re.MULTILINE)
        for n in reversed(list(objectOnly.finditer(dist))):
            dist = (
                dist[:n.start(1)] + '<object class="' + n.group(1) + '">\n' +
                dist[n.end():])

        # parameter
        for n in reversed(list(re.finditer(r'(\w+): (.+)\n', dist, 0))):
            # print n.groups()
            dist = (
                dist[:n.start()] + '<' + n.group(1) + '>' +
                n.group(2) + '</' + n.group(1) + '>\n' + dist[n.end():])

        # objectClose = re.compile(r'(class="\w+")(>\n\s*</*object)')
        # for n in reversed(list(objectClose.finditer(dist))):
        #     # print n.groups()
        #     dist = (
        #         dist[:n.end(1)] + '/' + dist[n.start(2):])

        dist = (
            '<?xml version="1.0" encoding="utf-8"?>\n' +
            '<!-- design layout in a separate XML file -->\n' +
            '<resource>\n' + dist)

        return dist


if __name__ == '__main__':
    src = '''# test
wxFrame: # test comment
    name: mainFrame
    subclass: MyFrame
    title: My Frame
    wxPanel:
        name: panel
        wxFlexGridSizer:
            cols: 2
            rows: 3
            vgap: 5
            hgap: 5

            sizeritem:
                wxStaticText:
                    name: label1
                    label: First name:
            sizeritem:
                wxTextCtrl:
                    name: text1

            sizeritem:
                wxStaticText:
                    name: label2
                    label: Last name:
            sizeritem:
                wxTextCtrl:
                    name: text2

            spacer:
                size: 0, 0

            sizeritem:
                wxButtion:
                    name: button
                    label: Submit
'''
    print toXRC().convert(src)
