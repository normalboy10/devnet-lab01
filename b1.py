
hs1 = dict(ten="Minh", tuoi=23, dv="Viettel")
hs2 = dict(ten="Nam", tuoi=24, dv="Viettel")
hs3 = dict(ten="Long", tuoi=25, dv="Viettel")
hs4 = dict(ten="Hoang", tuoi=26, dv="Viettel")
hs5 = dict(ten="Hau", tuoi=27, dv="Viettel")
hs_lst = [hs1, hs2, hs3, hs4, hs5]
print("---------------------")
for x in hs_lst:
    print("Ten:" + x['ten'])
    print("Tuoi:" + str(x['tuoi']))
    print("Don vi:" + x['dv'])
    print("---------------------")