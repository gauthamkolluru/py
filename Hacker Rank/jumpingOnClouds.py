# def jumpingOnClouds(c):
#     SAFE = 0
#     jumps = 0
#     i = 0
#     if len(c) == 1:
#         return 1
#     for i in range(len(c)):
#         if i < len(c):
#             if i+2 < len(c) and c[i+2] == SAFE:
#                 i += 2
#                 jumps += 1
#             elif i+1 < len(c) and c[i+1] == SAFE:
#                 i += 1
#                 jumps += 1
#
#     return jumps

def jumpingOnClouds(c):
    SAFE = 0
    jumps = []
    var = True
    i = 0
    while var:
        if i == 0:
            pass
        if i+2 < len(c) and c[i+2] == SAFE:
            jumps.append(i+2)
            i += 2
        elif i+1 < len(c) and c[i+1] == SAFE:
            jumps.append(i + 1)
            i += 1
        else:
            var = False
    return len(set(jumps))

print(jumpingOnClouds([0,0,1,0,0,1,0]))