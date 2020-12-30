import os
import argparse
import glob
import re

parser = argparse.ArgumentParser(description='rename')
parser.add_argument("--ABC", type=eval, default=True)
parser.add_argument("--title", type=str, default="100")
args = parser.parse_args()

if args.ABC:
    path = "./AtCoder_Beginner_Contest/ABC" + args.title
else:
    path = "./AtCoder_Regular_Contest/ARC" + args.title 

for c, s, sf in os .walk(path):
    count = 0
    for i in sf:
        if "png" in i:
            count += 1
            os.rename(c + "/" + i, c + "/" + "question{:01d}.png".format(count))
        p = c + "/" + "README.md"
        f = open(p, "w")
        for j in range(1, count + 1):
            f.write("![question](https://github.com/kimura-12/AtCoder_Training/blob/master/" + c[2:] + "/question{:01d}.png".format(j))