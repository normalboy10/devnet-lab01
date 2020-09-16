def chia2so(x, y):
    if y != 0:
        return x/y
    else:
        return None

x = input("Nhap so 1:")
y = input("Nhap so 2:")
print("KQ: %s" % chia2so(int(x), int(y)))