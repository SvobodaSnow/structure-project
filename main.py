import os
from os.path import isfile
from tkinter import *

from library.DictionaryWork import *
from library.DrawFile import *

pageHeight = 1169

paths_TC3 = {"ЩУ-П2.5_1": r'C:\Users\user\Desktop\Работа\Исток\Выкаченные шкафы\ЩУ-П2.5_1\PLC\SCHU_P2_5\POUs'}

w = Tk()
w.title("Генерация структур проектов TwinCat")
w.minsize(1200, 250)
frame = Frame(w, padx=20, pady=20)
frame.pack(expand=True)
function_is_add_check_button = BooleanVar()
# function_is_add = function_is_add_check_button.get()


def get_structure_TC2(file_name: str):
    el_m = {}
    f = open(file_name).readlines()
    path = ''
    for s in f:
        if s.find("@PATH") != -1:
            path = s[s.find("'") + 1:s.rfind("'")].split('\\/')[1:]
        if s.find('PROGRAM') == 0 or s.find("FUNCTION_BLOCK") == 0:
            if "MAIN" not in s:
                name_function = s[s.find(" ") + 1:-1]
                t = el_m
                for p in path:
                    if p not in t:
                        t[p] = {}
                    t = t[p]
                t[name_function] = name_function
    return el_m


def get_structure_TC3(path: str):
    el_m = {}
    for name_file in os.listdir(path):
        if "MAIN" not in name_file:
            file = os.path.join(path, name_file)
            if isfile(file):
                name = name_file[:name_file.rfind(".")]
                el_m[name] = name
            else:
                el_m[name_file] = get_structure_TC3(file)
    return el_m


def connect_blocks(draw_file: DrawFile, x_start: int, y_start: int, x_end: int, y_end: int, number_start: int, step=10):
    page_start = (y_start // pageHeight) + 1
    page_end = (y_end // pageHeight) + 1
    while page_start != page_end:
        y_end_p = (page_start * pageHeight) // 10 * 10 - 8 * step
        draw_file.add_line(x_start, y_start, x_end, y_end_p)
        draw_file.add_ellipse(x_start - 2 * step, y_end_p, 4 * step, text=str(number_start))
        y_start = (page_start * pageHeight) // 10 * 10 + 8 * step
        draw_file.add_ellipse(x_start - 2 * step, y_start - 4 * step, 4 * step, text=str(number_start))
        number_start += 1
        page_start = (y_start // pageHeight) + 1
    else:
        draw_file.add_line(x_start, y_start, x_end, y_end)
    return number_start


def print_dict(draw_file: DrawFile, d: dict, catalog=None, offset=0, block=0, step: int = 10, delta=0, number_start: int=1):
    last_block = 6 * step
    if catalog is not None:
        ost = (((12 * step + block * step * 8 + delta) // pageHeight) + 1) * pageHeight - (
                12 * step + block * step * 8 + delta)
        if ost <= 130:
            delta += (ost + 4 * step) // 10 * 10 + 4 * step
        draw_file.add_rectangle(12 * step + (offset - 1) * 12 * step, 12 * step + block * step * 8 + delta, 16 * step,
                                4 * step, text=catalog)
        draw_file.add_rectangle(62 * step, 12 * step + block * step * 8 + delta, 4 * step, 4 * step)
        draw_file.add_text(63 * step, 12 * step + block * step * 8 - 1 + delta, 16 * step, 4 * step + 2, text=get_description_path(catalog.upper()))
        draw_file.add_line(8 * step + (offset - 1) * 12 * step, 14 * step + block * step * 8 + delta,
                           12 * step + (offset - 1) * 12 * step, 14 * step + block * step * 8 + delta)
        draw_file.add_line(28 * step + (offset - 1) * 12 * step, 14 * step + block * step * 8 + delta, 62 * step,
                           14 * step + block * step * 8 + delta)
        last_block = 14 * step + block * step * 8 + delta
        block += 1

    if function_is_add_check_button.get() or catalog is None:
        for s in d:
            s_e = d[s]
            if s_e.__class__ is not dict:
                ost = (((12 * step + block * step * 8 + delta) // pageHeight) + 1) * pageHeight - (
                        12 * step + block * step * 8 + delta)
                if ost <= 130:
                    delta += (ost + 4 * step) // 10 * 10 + 4 * step

                draw_file.add_rectangle(12 * step + offset * 12 * step, 12 * step + block * step * 8 + delta, 16 * step,
                                        4 * step, text=s_e)
                draw_file.add_rectangle(62 * step, 12 * step + block * step * 8 + delta, 4 * step, 4 * step)
                draw_file.add_text(63 * step, 12 * step + block * step * 8 - 1 + delta, 16 * step, 4 * step + 2, text=get_description_function(s_e.upper()))
                draw_file.add_line(8 * step + offset * 12 * step, 14 * step + block * step * 8 + delta,
                                   12 * step + offset * 12 * step, 14 * step + block * step * 8 + delta)
                draw_file.add_line(28 * step + offset * 12 * step, 14 * step + block * step * 8 + delta, 62 * step,
                                   14 * step + block * step * 8 + delta)
                block += 1

    f = False
    last_y = None
    for s in d:
        s_e = d[s]
        if s_e.__class__ is dict:
            block, delta, f_v, last_y, number_start = print_dict(draw_file, s_e, catalog=s, offset=offset + 1, block=block,
                                                   delta=delta, number_start=number_start)
            if not f_v and function_is_add_check_button.get():
                number_start = connect_blocks(draw_file, 20 * step + offset * 12 * step, last_y + 2 * step,
                               20 * step + offset * 12 * step, 14 * step + (block - 1) * step * 8 + delta, number_start)
            f = True

    if last_y:
        number_start = connect_blocks(draw_file, 8 * step + offset * 12 * step, last_block + 2 * step,
                       8 * step + offset * 12 * step, last_y, number_start)

    return block, delta, f, last_block, number_start


def draw_struct(file_name: str, struct: dict):
    dr = create_file("result", file_name)
    step = 10

    dr.add_rectangle(4 * step, 4 * step, 8 * step, 4 * step, 1, "Main")
    print_dict(dr, struct)

    dr.save_file()
    return


def get_all_struct_TC2():
    for name_file_exp in os.listdir('sources'):
        file_name = "sources/" + name_file_exp
        el = get_structure_TC2(file_name)
        dob = ''
        if not function_is_add_check_button.get():
            dob = " (без функций)"
        draw_struct(file_name[file_name.rfind('/'):file_name.rfind('.')] + dob, el)
    return


def get_all_struct_TC3():
    for name_stand_TC3 in paths_TC3:
        name_path_TC3 = paths_TC3[name_stand_TC3]
        el = get_structure_TC3(name_path_TC3)
        dob = ''
        if not function_is_add_check_button.get():
            dob = " (без функций)"
        draw_struct(name_stand_TC3 + dob, el)
    return


def zag():

    return


cal_btn = Button(
    frame,
    text='Сформировать структуры для проектов TC2',
    command=get_all_struct_TC2,
    pady = 10,
    padx=10
)
cal_btn.grid(row=5, column=2)
cal_btn = Button(
    frame,
    text='Сформировать структуры для проектов TC3',
    command=get_all_struct_TC3,
    pady=10,
    padx=10
)
cal_btn.grid(row=5, column=3)
Checkbutton(frame, text="Учитывать в структуре функции?", variable=function_is_add_check_button).grid(row=0, column=3)
Label(frame, text="").grid(row=4, column=2)
Label(frame, text="").grid(row=1, column=2)

#Кнопки работы со словарями
#Выгрузка
cal_btn = Button(
    frame,
    text='Выгрузить словарь с экземплярами\nпапок',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=3, column=1)
cal_btn = Button(
    frame,
    text='Выгрузить словарь с экземплярами\nфункций',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=3, column=2)
cal_btn = Button(
    frame,
    text='Выгрузить словарь с экземплярами\nрегулярных выражений папок',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=3, column=3)
cal_btn = Button(
    frame,
    text='Выгрузить словарь с экземплярами\nрегулярных выражений функций',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=3, column=4)

#Загрузка
cal_btn = Button(
    frame,
    text='Загрузить словарь с экземплярами\nпапок',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=2, column=1)
cal_btn = Button(
    frame,
    text='Загрузить словарь с экземплярами\nфункций',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=2, column=2)
cal_btn = Button(
    frame,
    text='Загрузить словарь с экземплярами\nрегулярных выражений папок',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=2, column=3)
cal_btn = Button(
    frame,
    text='Загрузить словарь с экземплярами\nрегулярных выражений функций',
    command=zag,
    pady=10,
    padx=10
)
cal_btn.grid(row=2, column=4)

if __name__ == '__main__':
    w.mainloop()
