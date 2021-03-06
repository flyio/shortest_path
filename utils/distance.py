import math

# constants
a2 = 6378137.0 ** 2
b2 = 6356752.314140 ** 2
e2 = (a2 - b2) / a2

def hubeny(p1, p2):  # distance hubeny in meter
    def d2r(deg):
        return deg * (2 * math.pi) / 360
    (lon1, lat1, lon2, lat2) = map(d2r, p1 + p2)
    w = 1 - e2 * math.sin((lat1 + lat2) / 2) ** 2
    c2 = math.cos((lat1 + lat2) / 2) ** 2
    return math.sqrt((b2 / w ** 3) * (lat1 - lat2) ** 2 + (a2 / w) * c2 * (lon1 - lon2) ** 2) * 1000

def hubeny_seg(p):  # total length of a sequence of points
    dist = 0.0
    for p1, p2 in zip(p[0:(len(p)-1)],p[1:len(p)]):
        dist += hubeny(p1, p2)
    return dist
