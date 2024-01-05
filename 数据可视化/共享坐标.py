import  matplotlib.pyplot as plt
#  采用sharex=Ture 来共享x坐标
#  同样sharey=Ture 来共享y坐标
fig,axs= plt.subplots(2,3,figsize=(12,8),sharex=True)
axs[1,0].plot()
axs[0, 2].plot()