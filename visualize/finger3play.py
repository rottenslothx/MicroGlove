import winsound
while(True):
    f = open("./finger3.txt", "r")
    ch = f.read()
    if ch != '' and int(ch) == 100:
        winsound.PlaySound("E.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger3.txt", "w") as f:
            f.write("000")
    if ch != '' and int(ch) == 110:
        winsound.PlaySound("A.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger3.txt", "w") as f:
            f.write("010")        
    if ch != '' and int(ch) == 101:
        winsound.PlaySound("AI3.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger3.txt", "w") as f:
            f.write("001")
    if ch != '' and int(ch) == 111:
        winsound.PlaySound("cheer.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger3.txt", "w") as f:
            f.write("011")