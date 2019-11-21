import winsound

while(True):
    f = open("./finger1.txt", "r")
    ch = f.read()
    if ch != '' and int(ch) == 1:
        winsound.PlaySound("68441__pinkyfinger__piano-c.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        with open("./finger1.txt", "w") as f:
            f.write("0")