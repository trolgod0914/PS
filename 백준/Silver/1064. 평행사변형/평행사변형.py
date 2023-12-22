Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())
Vabx, Vaby = Xb-Xa, Yb-Ya
Vbcx, Vbcy = Xc-Xb, Yc-Yb
if Vabx*Vbcy == Vaby*Vbcx: print(-1); exit()
AB = ((Xa-Xb)**2+(Ya-Yb)**2)**(0.5)
BC = ((Xb-Xc)**2+(Yb-Yc)**2)**(0.5)
CA = ((Xc-Xa)**2+(Yc-Ya)**2)**(0.5)
MAX = (AB+BC+CA-min(AB, BC, CA))*2
MIN = (AB+BC+CA-max(AB, BC, CA))*2
print(MAX-MIN)