import winsound
while(True):
    f = open("./finger3.txt", "r")
    ch = f.read()
    if ch != '' and int(ch) == 1:
        winsound.PlaySound("68443__pinkyfinger__piano-e.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger3.txt", "w") as f:
            f.write("0")