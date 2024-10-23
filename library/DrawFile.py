import os.path
import random
import string

s_line = '''        <mxCell id="{}-{}" value="" style="endArrow=none;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="{}" y="{}" as="sourcePoint" />
            <mxPoint x="{}" y="{}" as="targetPoint" />
          </mxGeometry>
        </mxCell>'''
s_rectangle = '''        <mxCell id="{}-{}" value="{}" style="rounded={};whiteSpace=wrap;html=1;" parent="1" vertex="1">
          <mxGeometry x="{}" y="{}" width="{}" height="{}" as="geometry" />
        </mxCell>'''
s_text = '''        <mxCell id="{}-{}" value="{}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;strokeColor=none;fillColor=default;" vertex="1" parent="1">
          <mxGeometry x="{}" y="{}" width="{}" height="{}" as="geometry" />
        </mxCell>'''
s_ellipse = '''        <mxCell id="{}-{}" value="{}" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;" vertex="1" parent="1">
          <mxGeometry x="{}" y="{}" width="{}" height="{}" as="geometry" />
        </mxCell>'''


def create_file(path, name):
    file = open('library/StartPage.drawio', encoding="utf-8").readlines()
    id_end_header = -1
    id_start_footer = -1
    for i in range(len(file)):
        if id_end_header == -1 and file[i].find("root") != -1:
            id_end_header = i + 1
        elif id_start_footer == -1 and file[i].find("/root") != -1:
            id_start_footer = i
    new_diagram = DrawFile(path, name, file[:id_end_header], file[id_end_header:id_start_footer], file[id_start_footer:])
    return new_diagram


class DrawFile:
    def __init__(self, path, name, header, body, footer):
        self.path = path
        self.name = name
        self.header = header
        self.body = body
        self.footer = footer
        self.id = ''.join(random.choices(string.ascii_letters, k=10))
        self.id_element = 0

    def save_file(self):
        None if os.path.exists(self.path) else os.mkdir(self.path)
        file = open(self.path + "/" + self.name + ".drawio", "w", encoding="utf-8")
        file.writelines(self.header)
        file.writelines(self.body)
        file.writelines(self.footer)

    def add_line(self, x_start, y_start, x_end, y_end):
        self.id_element += 1
        self.body.append(s_line.format(self.id, self.id_element, x_start, y_start, x_end, y_end))

    def add_rectangle(self, x_start, y_start, width, height, rounded=0, text=""):
        self.id_element += 1
        self.body.append(s_rectangle.format(self.id, self.id_element, text, rounded, x_start, y_start, width, height))

    def add_text(self, x_start, y_start, width, height, text):
        self.id_element += 1
        self.body.append(s_text.format(self.id, self.id_element, text, x_start, y_start, width, height))

    def add_ellipse(self, x_start, y_start, width, height=None, text=''):
        self.id_element += 1
        self.body.append(s_ellipse.format(self.id, self.id_element, text, x_start, y_start, width, height))
        return
