import numpy as np  # knihovna pro numerické výpočty
import matplotlib.pyplot as plt  # knihovna pro grafiku
import pandas as pd # knihovna pro práci s tabulkami

fig, axs = plt.subplots(1,2, figsize=(12,4))

ax =axs[0]
x = np.linspace(0,10,100)
a = 2
df = pd.DataFrame(index=x)

df["Holling II"] = x/(x+a)
df["Holling III"] = x**2/(x**2+a**2)

df.plot(ax=ax)
ax.grid();

ax = axs[1]

b = 2
S = 1
x = np.linspace(-b,0)
ax.plot(x,S*x/(x+b), color="C0")
x = np.linspace(-6*b,-b)
ax.plot(x,S*x/(x+b), color="C0")
x = np.linspace(0,10)
ax.plot(x,S*x/(x+b), color="C1", lw=4)
ax.grid()
ax.vlines(-b,-4,4, color='gray', ls='--', lw=1)
ax.set(ylim=(-2,4))
