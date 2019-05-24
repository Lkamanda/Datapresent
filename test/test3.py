import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# method = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11',
#           'h12', 'h13', 'h14', 'h15', 'h16', 'h17', 'h18', 'h19', 'h20', 'uh']
method = [x for x in range(1,100)]

# ax=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
x_pos = np.arange(99)
ay =  [x for x in range(1,100)]
DF =  [x for x in range(1,100)]
# ay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
# DF = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
# fig=plt.figure()
plt.bar(x_pos, DF, align='center', alpha=1)
# x 轴的个数
plt.xticks(x_pos, method)
plt.xlabel("case")
plt.ylabel("variance")
plt.title("DF")

plt.show()
