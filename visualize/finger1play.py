import winsound

while(True):
    f = open("./finger1.txt", "r")
    ch = f.read()
    if ch != '' and int(ch) == 100:
        winsound.PlaySound("C.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger1.txt", "w") as f:
            f.write("000")
    if ch != '' and int(ch) == 110:
        winsound.PlaySound("F.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger1.txt", "w") as f:
            f.write("010")
    if ch != '' and int(ch) == 101:
        winsound.PlaySound("AI1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger1.txt", "w") as f:
            f.write("001")
    if ch != '' and int(ch) == 111:
        winsound.PlaySound("AI4.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger1.txt", "w") as f:
            f.write("011")
    