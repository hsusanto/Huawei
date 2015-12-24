import sys
import os
import json
import glob



def combine():
    result = []
    for f in glob.glob("mr20load40/Host*/flow_log.json"):
        with open(f, "rb") as infile:
            result += json.load(infile)

    with open("merged_file.json", "wb") as outfile:
        json.dump(result, outfile)


combine()
