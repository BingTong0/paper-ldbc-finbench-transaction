import csv
sf = 0.1
file_path = "out_sf" + str(sf) + "/snapshot/AccountTransferAccount.csv"
# file_path = "test.csv"

# Degree distribution
v2outdeg = dict()
v2indeg = dict()
# Global edge timestamp distribution
num_edge_by_hour = [0] * 24

# header = ['fromId', 'toId', 'amount', 'createTime', 'orderNum', 'comment', 'payType', 'goodsType']
colname2idx = dict()
with open(file_path, 'r') as f:
    reader = csv.reader(f, delimiter='|')
    first_line = True
    for row in reader:
        if first_line:
            first_line = False
            colname2idx = {row[i]: i for i in range(len(row))}
            continue
        fromId = int(row[colname2idx['fromId']])
        toId = int(row[colname2idx['toId']])
        if fromId not in v2outdeg:
            v2outdeg[fromId] = 1
        else:
            v2outdeg[fromId] += 1
        if toId not in v2indeg:
            v2indeg[toId] = 1
        else:
            v2indeg[toId] += 1
        time_str = row[colname2idx['createTime']]
        hour = int(time_str[time_str.find(' ')+1:time_str.find(':')])
        num_edge_by_hour[hour] += 1
# print(num_edge_by_hour)
# print("v2outdeg:", v2outdeg)
# print("v2indeg:", v2indeg)

max_indeg = 0
max_outdeg = 0
max_indeg_v = -1
max_outdeg_v = -1
for v, indeg in v2indeg.items():
    if indeg > max_indeg:
        max_indeg = indeg
        max_indeg_v = v
for v, outdeg in v2outdeg.items():
    if outdeg > max_outdeg:
        max_outdeg = outdeg
        max_outdeg_v = v
print("max_indeg_v:", max_indeg_v, "max_indeg:", max_indeg)
print("max_outdeg_v:", max_outdeg_v, "max_outdeg:", max_outdeg)

# Edge multiplicity of top-1 hub node
out_mp = dict()
in_mp = dict()

with open(file_path, 'r') as f:
    reader = csv.reader(f, delimiter='|')
    first_line = True
    for row in reader:
        if first_line:
            first_line = False
            continue
        fromId = int(row[colname2idx['fromId']])
        toId = int(row[colname2idx['toId']])
        if fromId == max_outdeg_v:
            if toId not in out_mp:
                out_mp[toId] = 1
            else:
                out_mp[toId] += 1
        if toId == max_indeg_v:
            if fromId not in in_mp:
                in_mp[fromId] = 1
            else:
                in_mp[fromId] += 1
# print("out_mp:", out_mp)
# print("in_mp:", in_mp)

indeg2nodenum = dict()
outdeg2nodenum = dict()
for v, indeg in v2indeg.items():
    if indeg not in indeg2nodenum:
        indeg2nodenum[indeg] = 1
    else:
        indeg2nodenum[indeg] += 1
for v, outdeg in v2outdeg.items():
    if outdeg not in outdeg2nodenum:
        outdeg2nodenum[outdeg] = 1
    else:
        outdeg2nodenum[outdeg] += 1
# print("indeg2nodenum:", indeg2nodenum)
# print("outdeg2nodenum:", outdeg2nodenum)

inmp2nodenum = dict()
outmp2nodenum = dict()
for v, mp in in_mp.items():
    if mp not in inmp2nodenum:
        inmp2nodenum[mp] = 1
    else:
        inmp2nodenum[mp] += 1
for v, mp in out_mp.items():
    if mp not in outmp2nodenum:
        outmp2nodenum[mp] = 1
    else:
        outmp2nodenum[mp] += 1
        
# Write collated statistics to file
out_path = "profile_sf" + str(sf) + ".out"
with open(out_path, 'w') as f:
    # Degree distribution
    for indeg in indeg2nodenum.keys():
        f.write(str(indeg) + ' ')
    f.write('\n')
    for nodenum in indeg2nodenum.values():
        f.write(str(nodenum) + ' ')
    f.write('\n')
    for outdeg in outdeg2nodenum.keys():
        f.write(str(outdeg) + ' ')
    f.write('\n')
    for nodenum in outdeg2nodenum.values():
        f.write(str(nodenum) + ' ')
    f.write('\n')
    # Edge multiplicity of top-1 hub node
    for inmp in inmp2nodenum.keys():
        f.write(str(inmp) + ' ')
    f.write('\n')
    for nodenum in inmp2nodenum.values():
        f.write(str(nodenum) + ' ')
    f.write('\n')
    for outmp in outmp2nodenum.keys():
        f.write(str(outmp) + ' ')
    f.write('\n')
    for nodenum in outmp2nodenum.values():
        f.write(str(nodenum) + ' ')
    f.write('\n')
    # Global edge timestamp distribution
    for num in num_edge_by_hour:
        f.write(str(num) + ' ')
    f.write('\n')