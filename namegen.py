import random 
elem = [["Nex","Xex","Pex","Dex","Hex","Zy","Sy","Gy","Xy","Dox","Seq","Mod","Tyl",
        "AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO",
        "PP","QQ","RR","SS","TT","UU","VV","XX","YY","ZZ","Phy","Eco","Exo","Eso",
        "Iso","Exe","1","2","3","4","5","6","7","8","9","0","Omni","Auto","Anti",
        "Bi","Tri","Quad","Hyper","Inter","Micro","Pre","Re","Sub","Trans","Sub",
        "Meta","Arch","Epi","Ecto"],
        ["Nex","Xex","Pex","Dex","Hex","Zy","Sy","Gy","Xy","Dox","Seq","Mod","Tyl",
        "AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO",
        "PP","QQ","RR","SS","TT","UU","VV","XX","YY","ZZ","Phy","Eco","Exo","Eso",
        "Iso","Exe","1","2","3","4","5","6","7","8","9","0","Omni","Auto","Anti",
        "Bi","Tri","Quad","Hyper","Inter","Micro","Pre","Re","Sub","Trans","Sub",
        "Meta","Arch","Epi","Ecto"],
        ["iel","uel","fu","1","2","3","4","5","6","7","8","9","0",
        "Nex","Xex","Pex","Dex","Hex","Zy","Sy","Gy","Xy","Dox","Seq","Mod","Tyl",
        "AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO",
        "PP","QQ","RR","SS","TT","UU","VV","XX","YY","ZZ","Phy","Eco","Exo","Eso",
        "Iso","Exe","Omni","Auto","Anti",
        "Bi","Tri","Quad","Hyper","Inter","Micro","Pre","Re","Sub","Trans","Sub",
        "Meta","Arch","Epi","Ecto"],
        ["iel","uel","fu","1","2","3","4","5","6","7","8","9","0"]
        ]

full = ""

for i in range(10):
    for j in range(len(elem)):
        arr_len = len(elem[j])
        rand_elem = random.randint(0, arr_len - 1)
        # print(elem[j][rand_elem])    
        full = full + elem[j][rand_elem]
    print(full)
    full = ""