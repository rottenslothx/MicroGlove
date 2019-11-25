import winsound
while(True):
    f = open("./finger2.txt", "r")
    ch = f.read()
    if ch != '' and int(ch) == 100:
        winsound.PlaySound("D.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger2.txt", "w") as f:
            f.write("000")
    if ch != '' and int(ch) == 110:
        winsound.PlaySound("G.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger2.txt", "w") as f:
            f.write("010")
    if ch != '' and int(ch) == 101:
        winsound.PlaySound("AI2.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger2.txt", "w") as f:
            f.write("001")
    if ch != '' and int(ch) == 111:
        winsound.PlaySound("AI5.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger2.txt", "w") as f:
            f.write("011")