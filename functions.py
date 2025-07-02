"""
functions to be imported into the Bob Ross Flask app
"""

def make_ordinal(num):
    for i in num:
        base = i % 10
        if base in [0,4,5,6,7,8,9] or i in [11,12,13]:
            ext = "th"
        elif base == 1:
            ext = "st"
        elif base == 2:
            ext = "nd"
        else:
            ext = "rd"
    return str(i) + ext





def get_elements(all_elements):
    legal_elements = []
    for i in all_elements:
        if i.aurora_borealis == 1:
            legal_elements.append("the aurora borealis")
        if i.barn == 1:
            legal_elements.append("a barn")
        if i.beach == 1:
            legal_elements.append("a beach")
        if i.boat == 1:
            legal_elements.append("a boat")
        if i.bridge == 1:
            legal_elements.append("a bridge")
        if i.building == 1:
            legal_elements.append("a building")
        if i.bushes == 1:
            legal_elements.append("bushes")
        if i.cabin == 1:
            legal_elements.append("a cabin")
        if i.cactus == 1:
            legal_elements.append("a cactus")
        if i.cliff == 1:
            legal_elements.append("a cliff")
        if i.clouds == 1:
            legal_elements.append("clouds")
        if i.dock == 1:
            legal_elements.append("a dock")
        if i.farm == 1:
            legal_elements.append("a farm")
        if i.fence == 1:
            legal_elements.append("a fence")
        if i.fire == 1:
            legal_elements.append("a fire")
        if i.flowers == 1:
            legal_elements.append("flowers")
        if i.fog == 1:
            legal_elements.append("fog")
        if i.grass == 1:
            legal_elements.append("grass")
        if i.hills == 1:
            legal_elements.append("hills")
        if i.lake == 1:
            if i.lakes == 1:
                legal_elements.append("lakes")
            else:
                legal_elements.append("a lake")
        if i.lighthouse == 1:
            legal_elements.append("a lighthouse")
        if i.mill == 1:
            legal_elements.append("a mill")
        if i.moon == 1:
            legal_elements.append("the moon")
        if i.mountain == 1:
            if i.mountains == 1:
                legal_elements.append("mountains")
            elif i.snowy_mountain == 1:
                legal_elements.append("a snowy mountain")
            else:
                legal_elements.append("a mountain")
        if i.ocean == 1:
            legal_elements.append("an ocean")
        if i.palm_trees == 1:
            legal_elements.append("palm trees")
        if i.pathway == 1:
            legal_elements.append("a path")
        if i.person == 1:
            legal_elements.append("a person")
        if i.river == 1:
            legal_elements.append("a river")
        if i.rocks == 1:
            legal_elements.append("rocks")
        if i.snow == 1:
            legal_elements.append("snow")
        if i.structure == 1:
            legal_elements.append("a structure")
        if i.sun == 1:
            legal_elements.append("the sun")
        if i.tree == 1:
            if i.trees == 1:
                legal_elements.append("trees")
            else:
                legal_elements.append("a tree")
        if i.waterfall == 1:
            legal_elements.append("a waterfall")
        if i.waves == 1:
            legal_elements.append("waves")
        if i.windmill == 1:
            legal_elements.append("a windmill")

    return legal_elements



