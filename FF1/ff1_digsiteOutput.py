import os

text = open("ff1_digsiteOutput.txt", "wt")
text.close()
text = open("ff1_digsiteOutput.txt", "at")
for root, dirs, files in os.walk("m/bin"):
    for file in files:
        if (file == "0.bin"):
            f = open(os.path.join(root, file), "rb")
            r = f.read()
            f.close()
            point = int.from_bytes(r[0x54:0x58], "little")
            mapN = os.path.join(root, file).split("\\")[-2]
            mf = open("Map IDs.txt", "rt")
            lines = list(mf.read().split("\n")).copy()
            for t in lines:
                if (t != ""):
                    nums = list(t.split(":")[0].replace(", ", ",").split(",")).copy()
                    for n in nums:
                        if (int(mapN.split(" [")[0]) == int(n)):
                            mapN = mapN + " [" + t.split(": ")[1] + "]"
            f = open("ff1_vivoNames.txt", "rt")
            vivoNames = [""] + list(f.read().split("\n")).copy()
            f.close()
            realP = [ int.from_bytes(r[point:(point + 4)], "little") ]
            loc = point + 4
            while (realP[-1] > 0):
                realP.append(int.from_bytes(r[loc:(loc + 4)], "little"))
                loc = loc + 4
            realP = realP[0:-1]
            check = 0
            for val in realP:
                index = int.from_bytes(r[(val + 4):(val + 8)], "little")
                if (index == 0):
                    continue
                else:
                    if (check == 0):
                        check = 1
                        text.write(mapN + ":\n")
                text.write("Zone " + str(index).zfill(2) + ":\n")
                maxFos = int.from_bytes(r[(val + 12):(val + 16)], "little")
                text.write("\tMax Spawns: " + str(maxFos) + "\n")
                numSpawns = int.from_bytes(r[(val + 0x28):(val + 0x2C)], "little")
                point3 = int.from_bytes(r[(val + 0x2C):(val + 0x30)], "little")
                for i in range(numSpawns):
                    point4 = int.from_bytes(r[(val + point3 + (i * 4)):(val + point3 + (i * 4) + 4)], "little")
                    vivoNum = int.from_bytes(r[(val + point4):(val + point4 + 4)], "little")
                    chance = int.from_bytes(r[(val + point4 + 4):(val + point4 + 8)], "little")
                    text.write("\t"+ vivoNames[vivoNum] + ": " + str(chance) + "%\n")
            if (check == 1):
                text.write("\n")
text.close()
                
                