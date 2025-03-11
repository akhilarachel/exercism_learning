def score(x, y):
    distance = ((x ** 2) + (y ** 2)) ** 0.5
    print(distance)
    print(x ** 2)
    print(y ** 2)
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0


print(score(0, 10))
