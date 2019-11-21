import winsound
while(True):
    f = open("./finger2.txt", "r")
    ch = f.read()
    if ch != '' and int(ch) == 1:
        winsound.PlaySound("68442__pinkyfinger__piano-d.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger2.txt", "w") as f:
            f.write("0")