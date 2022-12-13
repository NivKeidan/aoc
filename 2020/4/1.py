import re

passport = {}
valids = 0
debug = False

def isValid():
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for r in required:
        if r not in passport:
            # print("missing field", r)
            return False
    
    byr = int(passport["byr"])
    if byr < 1920 or (byr > 2002 and byr <= 9999):
        # print("year", byr)
        return False
    
    iyr = int(passport["iyr"])
    if iyr < 2010 or (iyr > 2020 and iyr <= 9999):
        # print("iyr", iyr)
        return False
    
    eyr = int(passport["eyr"])
    if eyr < 2020 or (eyr > 2030 and eyr <= 9999):
        # print("eyr", eyr)
        return False
    
    hgt = passport["hgt"]
    x = re.search("^([0-9]+)(cm|in)$", hgt)
    if x is None:
        # print("hgt", hgt)
        return False
    height = int(x.group(1))
    unit = x.group(2)
    if unit == "in":
        if height < 59 or height > 76:
            # print("hgt", hgt)
            return False
    if unit == "cm":
        if height < 150 or height > 193:
            # print("hgt", hgt)
            return False
    
    hcl = passport["hcl"]
    x = re.search("^#[0-9a-f]{6}$", hcl)
    if x is None:
        # print("hcl", hcl)
        return False
    
    ecl = passport["ecl"]
    x = re.search("^(amb|blu|brn|gry||grn|hzl|oth)$", ecl)
    if x is None:
        # print("ecl", ecl)
        return False
    
    pid = passport["pid"]
    x = re.search("^[0-9]{9}$", pid)
    if x is None:
        # print("pid", pid)
        return False

    return True

with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()

        if l == "":
            if isValid():
                print(passport)
                valids += 1
            passport = {}
            continue

        entries = l.split(" ")
        for e in entries:
            parts = e.split(":")
            k = parts[0]
            v = parts[1]
            passport[k] = v

# for last paassport
if isValid():
    valids += 1
print(valids)