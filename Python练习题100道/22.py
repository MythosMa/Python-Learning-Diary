# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
order = ["x", "y", "z"]

for a in range(3):
    for b in range(3):
        if a!= b:
            for c in range(3):
                if (a != c) and (b != c):
                    if (order[a] != "x") and (order[c] != "x") and (order[c] != "z"):
                        print(f"a->{order[a]}, b->{order[b]}, c->{order[c]}") 