import sys; input = sys.stdin.readline

def Triangle_Area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2

def Cross_Product(x1, y1, x2, y2):
    return y1*x2-y2*x1

def PiP(x1, y1, x2, y2, x3, y3, x4, y4):
    ADx, ADy = x4-x1, y4-y1
    BDx, BDy = x4-x2, y4-y2
    CDx, CDy = x4-x3, y4-y3
    DAx, DAy = x1-x4, y1-y4
    DBx, DBy = x2-x4, y2-y4
    DCx, DCy = x3-x4, y3-y4
    ADB = Cross_Product(ADx, ADy, DBx, DBy)
    ADC = Cross_Product(ADx, ADy, DCx, DCy)
    BDA = -ADB
    BDC = Cross_Product(BDx, BDy, DCx, DCy)
    CDA = -ADC
    CDB = -BDC
    if ADB * ADC <= 0 and BDA * BDC <= 0 and CDA * CDB <=0:
        return True
    return False

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
Count = 0
for _ in range(int(input())):
    x4, y4 = map(int, input().split())
    if PiP(x1, y1, x2, y2, x3, y3, x4, y4):
        Count += 1
print("{:.1f}".format(Triangle_Area(x1, y1, x2, y2, x3, y3)))
print(Count)