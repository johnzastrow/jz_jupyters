# import matplotlib and numpy as usual
import matplotlib.pyplot as plt
import numpy as np

# now import pylustrator
import pylustrator

# activate pylustrator
pylustrator.start()


# build plots as you normally would
np.random.seed(1)
t = np.arange(0.0, 2, 0.001)
y = 2 * np.sin(np.pi * t)
a, b = np.random.normal(loc=(5., 3.), scale=(2., 4.), size=(100,2)).T
b += a

plt.figure(1)
plt.subplot(131)
plt.plot(t, y)

plt.subplot(132)
plt.plot(a, b, "o")

plt.subplot(133)
plt.bar(0, np.mean(a))
plt.bar(1, np.mean(b))

# show the plot in a pylustrator window
#% start: automatic generated code from pylustrator
fig = plt.figure(1)
import matplotlib as mpl
fig.ax_dict = {ax.get_label(): ax for ax in fig.axes}
fig.set_edgecolor("#ff2c7dff")
fig.set_facecolor("#fcf3ffff")
fig.axes[1].get_xaxis().get_label().set_weight("normal")
fig.text(0.5, 0.5, 'Where does this appear?', transform=fig.transFigure)  # id=fig.texts[0].new
fig.texts[0].set_position([0.162064, 0.022639])
fig.texts[0].set_text("This is interesting. I wonder how many characters I can fit into this sectgion. ")
fig.texts[0].set_weight("bold")
fig.texts[0].set_fontsize(7)
fig.texts[0].set_color("#0055ffff")
fig.axes[0].set_position([0.083923, 0.416067, 0.227941, 0.463933])
fig.axes[0].set_facecolor("#ffff7fff")
fig.axes[0].spines['right'].set_visible(False)
fig.axes[0].spines['top'].set_visible(False)
fig.axes[1].get_xaxis().get_label().set_text("Middle chart, x axis")
fig.axes[1].get_yaxis().get_label().set_weight("bold")
fig.axes[1].set_xlim(0.8454055139811809, 12.495282170738111)
fig.axes[1].set_xticks([2.5, 4.0, 7.0], minor=True)
fig.axes[1].set_xticklabels(["5", "10", "11"])
fig.axes[1].set_xlabel("This was werer")
fig.axes[1].set_position([0.345404, 0.385392, 0.281066, 0.494608])
fig.axes[1].spines['right'].set_visible(False)
fig.axes[1].spines['top'].set_visible(False)
fig.axes[1].set_xticklabels(["2.5", "4", "Yay"], minor=True)
fig.axes[1].set_xticks([5.0, 10.0, 11.0])
fig.axes[1].xaxis.labelpad = 8.0
#% end: automatic generated code from pylustrator
plt.show()