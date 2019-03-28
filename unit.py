from offset import Offset
from math import sqrt

offset = Offset()


def is_unit(obj, process):
    if process.readuint4(obj + offset.ObjectManager.ObjType) == 3:
        return True
    else:
        return False


def is_player(obj, process):
    if process.readuint4(obj + offset.ObjectManager.ObjType) == 4:
        return True
    else:
        return False


def position(unit, process):
    if is_unit(unit, process):
        x = process.readfloat(unit + offset.Unit.PosX)
        y = process.readfloat(unit + offset.Unit.PosY)
        z = process.readfloat(unit + offset.Unit.PosZ)
    elif is_player(unit, process):
        x = process.readfloat(unit + offset.Unit.PosX)
        y = process.readfloat(unit + offset.Unit.PosY)
        z = process.readfloat(unit + offset.Unit.PosZ)
    else:
        return False
    return [x, y, z]


def distance_ato_b(unit_a, unit_b, process):
    if not is_unit(unit_a, process) and not is_player(unit_a, process):
        return False
    if not is_unit(unit_b, process) and not is_player(unit_b, process):
        return False
    a = position(unit_a, process)
    b = position(unit_b, process)
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)


def name(unit, process):
    if not is_unit(unit, process):
        return False
    return process.readuint4(offset.Unit.NameBase)