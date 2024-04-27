import greenhouse2
sensors = greenhouse2.w1_enumerate(4)
for s in sensors:
    print(s)
