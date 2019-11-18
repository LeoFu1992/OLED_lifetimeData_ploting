import matplotlib.pyplot as plt
import pandas as pd
import os
if os.path.isfile('LifetimeA.csv'):
    Lifetime = pd.read_csv('LifetimeA.csv')
    x = Lifetime[['TestTime(sec)']]/3600
    y = Lifetime[[' B(%) ']]
else:
    print('LifetimeA file loss')
if os.path.isfile('LifetimeB.csv'):
    Lifetime2 = pd.read_csv('LifetimeB.csv')
    x2 = Lifetime2[['TestTime(sec)']]/3600
    y2 = Lifetime2[[' B(%) ']]
else:
    print('LifetimeB file loss')
if os.path.isfile('LifetimeC.csv'):
    Lifetime3 = pd.read_csv('LifetimeC.csv')
    x3 = Lifetime3[['TestTime(sec)']]/3600
    y3 = Lifetime3[[' B(%) ']]
else:
    print('LifetimeC file loss')
if os.path.isfile('LifetimeD.csv'):
    Lifetime4 = pd.read_csv('LifetimeD.csv')
    x4 = Lifetime4[['TestTime(sec)']]/3600
    y4 = Lifetime4[[' B(%) ']]
else:
    print('LifetimeD file loss')
def location():
    plt.legend(loc='upper right')
    plt.style.use('bmh')
    plt.show()
if os.path.isfile('LifetimeA.csv'):
    plt.style.use('bmh')
    if os.path.isfile('LifetimeB.csv'):
        if os.path.isfile('LifetimeC.csv'):
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x, y, label='A')
                plt.plot(x2, y2, label='B')
                plt.plot(x3, y3, label='C')
                plt.plot(x4, y4, label='D')        
                location()
            else:
                plt.plot(x, y, label='A')
                plt.plot(x2, y2, label='B')
                plt.plot(x3, y3, label='C')
                location()
        else:
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x, y, label='A')
                plt.plot(x2, y2, label='B')
                plt.plot(x4, y4, label='D')
                location()
            else:
                plt.plot(x, y, label='A')
                plt.plot(x2, y2, label='B')
                location()
    else:
        if os.path.isfile('LifetimeC.csv'):
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x, y, label='A')
                plt.plot(x3, y3, label='C')
                plt.plot(x4, y4, label='D')
                location()
            else:
                plt.plot(x, y, label='A')
                plt.plot(x3, y3, label='C')
                plt.style.use('bmh')
                location()
        else:
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x, y, label='A')
                plt.plot(x4, y4, label='D')
                plt.style.use('bmh')
                location()
            else:
                plt.plot(x, y, label='A')
                plt.style.use('bmh')
                location()
else:
    plt.style.use('bmh')
    if os.path.isfile('LifetimeB.csv'):
        if os.path.isfile('LifetimeC.csv'):
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x2, y2, label='B')
                plt.plot(x3, y3, label='C')
                plt.plot(x4, y4, label='D')
                location()
            else:
                plt.plot(x2, y2, label='B')
                plt.plot(x3, y3, label='C')
                location()
        else:
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x2, y2, label='B')
                plt.plot(x4, y4, label='D')
                location()
            else:
                plt.plot(x2, y2, label='B')
                location()
    else:
        if os.path.isfile('LifetimeC.csv'):
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x3, y3, label='C')
                plt.plot(x4, y4, label='D')
                location()
            else:
                plt.plot(x3, y3, label='C')
                location()
        else:
            if os.path.isfile('LifetimeD.csv'):
                plt.plot(x4, y4, label='D')
                location()