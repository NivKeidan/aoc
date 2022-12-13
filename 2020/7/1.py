import regex
bags = {}
# final_holders = set()

def get_holding_num(bag_color):
    # print("checking", bag_color)
    cnt = 1
    if bag_color not in bags:
        print(bag_color, "holding %d" % cnt)
        return cnt

    holds = bags[bag_color]
    for h in holds:
        n = h[0]
        c = h[1]
        print(bag_color, "holds %d %s" % (n, c))
        cnt += n*get_holding_num(c)
    print(bag_color, "holding %d" % cnt)
    return cnt


with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()

        m = regex.match(r"^(?P<holder>[\w ]+) bags contain (?:(?P<num_holds>[0-9]+) (?P<holds>[\w ]+) bag[s]?(?:, )?)*.$", l)
        if m is None:
            continue
        
        holder = m.capturesdict()["holder"][0]
        holds = m.capturesdict()["holds"]
        numbers = m.capturesdict()["num_holds"]
        bags[holder] = []
        for i, h in enumerate(holds):
            bags[holder].append((int(numbers[i]), h))
# print(bags)
print(get_holding_num("shiny gold")-1)


# def get_all_holders(bag_color):
#     holders = set()
#     for holder, holds in bags.items():
#         if bag_color in holds:
#             holders.add(holder)
#     return holders

# shiny_gold_holders = get_all_holders("shiny gold")
# while len(shiny_gold_holders) > 0:
#     final_holders = final_holders | shiny_gold_holders

#     new_holders = set()
#     for gold_holder in shiny_gold_holders:
#         new_holders = new_holders | get_all_holders(gold_holder)
#     shiny_gold_holders =  new_holders


