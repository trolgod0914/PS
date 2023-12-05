V_Kappa, J_Kappa = map(int, input().split())
V_Lambda, J_Lambda = map(int, input().split())
V, D, J = map(int, input().split())
print((V_Kappa*J_Kappa+V_Lambda*J_Lambda)*V*D*J)