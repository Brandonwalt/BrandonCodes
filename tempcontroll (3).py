import greenhouse2
sensors = greenhouse2.w1_enumerate()
for s in sensors:
    print(s)
