def equilateral(sides):
    if len(sides) != 3:
        return False
    elif ((sides[0]) + (sides[1]) < (sides[2])) or (
            (sides[1]) + (sides[2]) < (sides[0]) or (sides[0]) + (sides[2]) < (sides[1])):
        return False
    elif sides[0] != 0 or sides[1] != 0 or sides[2] != 0:
        return sides[0] == sides[1] == sides[2]
    else:
        return False

    # return (sides[0] == sides[1]) and (sides[0] == sides[2]) and (sides[1] == sides[2])


def isosceles(sides):
    if len(sides) != 3:
        return False
    elif ((sides[0]) + (sides[1]) < (sides[2])) or (
            (sides[1]) + (sides[2]) < (sides[0]) or (sides[0]) + (sides[2]) < (sides[1])):
        return False
    elif sides[0] != 0 or sides[1] != 0 or sides[2] != 0:
        return (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2])
    else:
        return False


def scalene(sides):
    if len(sides) != 3:
        return False
    elif ((sides[0]) + (sides[1]) < (sides[2])) or (
            (sides[1]) + (sides[2]) < (sides[0]) or (sides[0]) + (sides[2]) < (sides[1])):
        return False
    elif sides[0] != 0 or sides[1] != 0 or sides[2] != 0:
        return sides[0] != sides[1] != sides[2] != sides[0]
    else:
        return False
