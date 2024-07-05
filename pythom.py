import sys, subprocess, os
if len(sys.argv) == 2:
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
        lines = [line.replace("n", "m") for line in lines]
    except:
        print("...what?")
        sys.exit()
    with open(sys.argv[1]+"-temp", "w") as file:
        for line in lines:
            file.write(line)
    try:
        subprocess.call(["python3", sys.argv[1]+"-temp"])
    except:
        try:
            subprocess.call(["python", sys.argv[1]+"-temp"])
        except:
            subprocess.call(["py", sys.argv[1]+"-temp"])
    os.remove(sys.argv[1]+"-temp")
else:
    print("...huh?")