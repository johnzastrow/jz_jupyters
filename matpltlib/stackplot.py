import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

goodlabels = ["Player 1","Player 2","Player 3"] # optional way to control labels
goodcolors = ['#C4D4ED','#9CB9E5','#BCD8B1'] # optional way to control colors
plt.stackplot(minutes,player2,player2,player3, labels=goodlabels, colors=goodcolors)
# plt.legend(loc='lower left') # hard-coded location

plt.legend(loc='upper left')
plt.title("My Awesome Stack Plot")


# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
# blue gray = #C4D4ED
# bluer gray = #9CB9E5
# green gray = #BCD8B1

plt.grid('True')
plt.tight_layout() # optional to fix certain layout issues.
plt.savefig('stackchart.png')
plt.show()
