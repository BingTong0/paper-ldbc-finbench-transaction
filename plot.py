res_dir = "results/"
sf = 1
res_path = res_dir + "/profile_sf" + str(sf) + ".out"

# Degree distribution
indeg_ls = []
indeg_nodenum_ls = []
outdeg_ls = []
outdeg_nodenum_ls = []
# Edge multiplicity of top-1 hub node
inmp_ls = []
inmp_nodenum_ls = []
outmp_ls = []
outmp_nodenum_ls = []
# Global edge timestamp distribution
num_edge_by_hour = []
with open(res_path, "r") as f:
    line = f.readline()
    indeg_ls = line.split()
    indeg_ls = [int(x) for x in indeg_ls]
    line = f.readline()
    indeg_nodenum_ls = line.split()
    indeg_nodenum_ls = [int(x) for x in indeg_nodenum_ls]
    line = f.readline()
    outdeg_ls = line.split()
    outdeg_ls = [int(x) for x in outdeg_ls]
    line = f.readline()
    outdeg_nodenum_ls = line.split()
    outdeg_nodenum_ls = [int(x) for x in outdeg_nodenum_ls]
    line = f.readline()
    inmp_ls = line.split()
    inmp_ls = [int(x) for x in inmp_ls]
    line = f.readline()
    inmp_nodenum_ls = line.split()
    inmp_nodenum_ls = [int(x) for x in inmp_nodenum_ls]
    line = f.readline()
    outmp_ls = line.split()
    outmp_ls = [int(x) for x in outmp_ls]
    line = f.readline()
    outmp_nodenum_ls = line.split()
    outmp_nodenum_ls = [int(x) for x in outmp_nodenum_ls]
    line = f.readline()
    num_edge_by_hour = line.split()
    num_edge_by_hour = [int(x) for x in num_edge_by_hour]

import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)
plt.rcParams["figure.figsize"] = [4, 2]
plt.rcParams["font.size"] = 11
fig_path = "fig/" + str(sf) + '/'

plt.figure(1)
plt.scatter(indeg_ls, indeg_nodenum_ls)
plt.xlabel("In-degree")
plt.ylabel("Number of nodes")
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig(fig_path + "/indeg_dist.pdf")

plt.figure(2)
plt.scatter(outdeg_ls, outdeg_nodenum_ls)
plt.xlabel("Out-degree")
plt.ylabel("Number of nodes")
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig(fig_path + "/outdeg_dist.pdf")

plt.figure(3)
plt.scatter(inmp_ls, inmp_nodenum_ls)
plt.xlabel("In-edge multiplicity")
plt.ylabel("Number of nodes")
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig(fig_path + "/inmp_dist.pdf")

plt.figure(4)
plt.scatter(outmp_ls, outmp_nodenum_ls)
plt.xlabel("Out-edge multiplicity")
plt.ylabel("Number of nodes")
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig(fig_path + "/outmp_dist.pdf")

plt.figure(5)
hours_of_day = list(range(24))
plt.bar(hours_of_day, num_edge_by_hour, color='blue')
plt.xlabel('Hour of the Day')
plt.ylabel('\#Transfer edges')
plt.tight_layout()
plt.savefig(fig_path + "/edge_timestamp.pdf")

plt.show()