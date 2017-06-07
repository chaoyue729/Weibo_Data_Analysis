import graph_tool as gt
import graph_tool.stats
import numpy as np
import matplotlib.pyplot as plt

g=gt.load_graph("../data/graphAll.xml.gz")

res=gt.stats.distance_histogram(g)	#May cost much time.

fig=plt.figure()
plt.plot(res[0],label="Distance distribution")
plt.legend(loc="upper right")
plt.xlabel("Distance")
plt.ylabel("Count")
fig.savefig("../pic/distance.svg")

fig=plt.figure()
res[0][0]=1
plt.plot(np.log10(res[0]),label="Log-distance distribution")
plt.legend(loc="upper right")
plt.xlabel("Distance")
plt.ylabel("Log-count")
fig.savefig("../pic/log-distance.svg")

