import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.distplot([0, 1, 2, 3, 4, 5])

sns.distplot(random.normal(size=1000), hist=False)

plt.show()