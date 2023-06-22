import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.backends.backend_qt5agg
import PyQt5
import matplotlib as mpl
# import latex 
mpl.use('Qt5Agg')
# plt.rcParams['text.usetex'] = True

location = r'C:\Users\erikn\OneDrive - Chalmers\Computational Biology\CB HW 3'
task = 1

b_list = np.array([0.1, 1, 10])
d_list = np.array([0.2, 2, 5])
dt = 0.01
no_runs = 5*10**4
tb = np.zeros((len(b_list), no_runs))
td = np.zeros_like(tb)

for i in range(len(b_list)):

    b = b_list[i]
    d = d_list[i]

    for j in range(no_runs):

        if (j % 1000 == 0): print(i, j, no_runs)

        # for b
        t = 0
        flag = True

        while flag == True:
            r = np.random.uniform(0,1)
            if r < b*dt:
                tb[i,j] = t
                flag = False
            else:
                t = t + dt

        # for d
        t = 0
        flag = True

        while flag == True:
            r = np.random.uniform(0,1)
            if r < d*dt:
                td[i,j] = t
                flag = False
            else:
                t = t + dt

# np.save('tb.npy', tb)
# np.save('td.npy', td)
tb = np.load('tb.npy')
td = np.load('td.npy')

task = 0
fontsize = 15
bins = 100
figsize = 7
inf = 60
location = r'C:\Users\erikn\OneDrive - Chalmers\Computational Biology\CB HW 3'


# Plotting tb
plt.figure()
hist1 = plt.hist(tb[task,:], bins=bins, density=True)

tb_shift = (hist1[1][1] - hist1[1][0]) / 2
tb_list = np.zeros_like(hist1[0])

for i in range(len(hist1[1])-1):
    tb_list[i] = hist1[1][i] + tb_shift

bt_list = b_list[task]*np.exp(-tb_list*b_list[task])

coef1 = np.polyfit(tb_list[0:inf], np.log(hist1[0][0:inf]), 1)
poly1 = np.poly1d(coef1) 
y1_fitted = np.exp(coef1[1]) * np.exp(coef1[0] * tb_list)

fig1, ax1 = plt.subplots(figsize=(figsize,figsize))
ax1.plot(tb_list, hist1[0], '.', color='black', label='Sampled dist. density=true')
ax1.plot(tb_list, bt_list, '-', color='blue', lw=2, label='$\\lambda e(-\\lambda t)$, $\\lambda =b_n$')
ax1.plot(tb_list, y1_fitted, '--', color="red", lw=2, label='Regression line')
ax1.set_title('$b_n = {}$'.format(b_list[task]), fontsize=fontsize)
ax1.set_yscale('log')
ax1.set_ylabel('$logP(t_b)$', fontsize=fontsize)
ax1.set_xlabel('$t_b$', fontsize=fontsize)
ax1.set_box_aspect(1) 
ax1.legend(loc="upper right", prop={'size': 11})

# plt.legend(loc="upper right", prop={'size': 11})
title = '/3.1b_bn_{}'.format(b_list[task])
plt.savefig(location+title+'.png')

# Plotting td
plt.figure()
hist2 = plt.hist(td[task,:], bins=bins, density=True)

td_shift = (hist2[1][1] - hist2[1][0]) / 2
td_list = np.zeros_like(hist2[0])

for i in range(len(hist2[1])-1):
    td_list[i] = hist2[1][i] + td_shift

dt_list = d_list[task]*np.exp(-td_list*d_list[task])

coef2 = np.polyfit(td_list[0:inf], np.log(hist2[0][0:inf]), 1)
y2_fitted = np.exp(coef2[1]) * np.exp(coef2[0] * td_list)

fig1, ax2 = plt.subplots(figsize=(figsize,figsize))
ax2.plot(td_list, hist2[0], '.', color='black', label='Sampled dist. density=true')
ax2.plot(td_list, dt_list, '-', color='blue', lw=2, label='$\\lambda e(-\\lambda t)$, $\\lambda =d_n$')
ax2.plot(td_list, y2_fitted, '--', color="red", lw=2, label='Regression line')
ax2.set_title('$d_n = {}$'.format(d_list[task]),  fontsize=fontsize)
ax2.set_yscale('log')
ax2.set_ylabel('$logP(t_d)$', fontsize=fontsize)
ax2.set_xlabel('$t_d$', fontsize=fontsize)
ax2.set_box_aspect(1) 
ax2.legend(loc="upper right", prop={'size': 11})

# plt.legend(loc="upper right", prop={'size': 11})
title = '/3.1b_dn_{}'.format(d_list[task])
plt.savefig(location+title+'.png')

plt.show()