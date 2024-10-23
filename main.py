from library.DrawFile import *

pageHeight = 1169


def get_structure(file_name: str):
    el_m = {}
    f = open(file_name).readlines()
    path = ''
    for s in f:
        if s.find("@PATH") != -1:
            path = s[s.find("'") + 1:s.rfind("'")].split('\\/')[1:]
        if s.find('PROGRAM') == 0:
            if "MAIN" not in s:
                name_function = s[s.find(" ") + 1:-1]
                t = el_m
                for p in path:
                    if p not in t:
                        t[p] = {}
                    t = t[p]
                t[name_function] = name_function
    return el_m


def print_dict(draw_file: DrawFile, d: dict, catalog=None, offset=0, block=0, step: int = 10, delta=0):
    if catalog is not None:
        ost = (((12 * step + block * step * 8 + delta) // pageHeight) + 1) * pageHeight - (
                12 * step + block * step * 8 + delta)
        if ost <= 130:
            delta += (ost + 4 * step) // 10 * 10
        draw_file.add_rectangle(12 * step + (offset - 1) * 12 * step, 12 * step + block * step * 8 + delta, 16 * step,
                                4 * step, text=catalog)
        draw_file.add_rectangle(62 * step, 12 * step + block * step * 8 + delta, 4 * step, 4 * step)
        draw_file.add_text(63 * step, 12 * step + block * step * 8 - 1 + delta, 16 * step, 4 * step + 2, text=catalog)
        draw_file.add_line(8 * step + (offset - 1) * 12 * step, 14 * step + block * step * 8 + delta,
                           12 * step + (offset - 1) * 12 * step, 14 * step + block * step * 8 + delta)
        draw_file.add_line(28 * step + (offset - 1) * 12 * step, 14 * step + block * step * 8 + delta, 62 * step,
                           14 * step + block * step * 8 + delta)
        block += 1

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
            draw_file.add_text(63 * step, 12 * step + block * step * 8 - 1 + delta, 16 * step, 4 * step + 2, text=s_e)
            draw_file.add_line(8 * step + offset * 12 * step, 14 * step + block * step * 8 + delta,
                               12 * step + offset * 12 * step, 14 * step + block * step * 8 + delta)
            draw_file.add_line(28 * step + offset * 12 * step, 14 * step + block * step * 8 + delta, 62 * step,
                               14 * step + block * step * 8 + delta)
            block += 1

    f = False
    old_block = block
    for s in d:
        s_e = d[s]
        if s_e.__class__ is dict:
            old_block = block
            old_delta = delta
            block, delta, f_v, _ = print_dict(draw_file, s_e, catalog=s, offset=offset + 1, block=block, delta=delta)
            if f_v:
                draw_file.add_line(14 * step + offset * 12 * step, 16 * step + old_block * step * 8 + old_delta,
                                   14 * step + offset * 12 * step, 14 * step + _ * step * 8 + delta)
            draw_file.add_line(20 * step + offset * 12 * step, 16 * step + old_block * step * 8 + old_delta,
                               20 * step + offset * 12 * step, 14 * step + (block - 1) * step * 8 + delta)
            f = True
    print(f)
    return block, delta, f, old_block


def draw_struct(file_name: str, struct: dict):
    dr = create_file("result", file_name)
    step = 10

    dr.add_rectangle(4 * step, 4 * step, 8 * step, 4 * step, 1, "Main")
    print_dict(dr, struct)

    dr.save_file()
    return


if __name__ == '__main__':
    file_name = 'S.EXP'
    el = get_structure(file_name)

    draw_struct(file_name, el)
