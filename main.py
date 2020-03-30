# Copyright (c) 2020 Copyright Mathis POTEAU (delincta) All Rights Reserved.

# estimate_pi(n) from Joma Tech

import random
import matplotlib.pyplot as plt
import numpy as np


def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    x = np.linspace(-1.0, 1.0, 100)
    y = np.linspace(-1.0, 1.0, 100)
    X, Y = np.meshgrid(x,y)
    F = X**2 + Y**2 - 1.0

    fig, ax = plt.subplots()

    ax.contour(X,Y,F,[0])

    ax.set_aspect(1)
    plt.xlim(-1,1)
    plt.ylim(-1,1)

    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
            plt.scatter(x,y, color="blue")
        else :
            plt.scatter(x,y, color="red")
        num_point_total += 1
    plt.axis('off')
    plt.show()
    return 4 * num_point_circle / num_point_total
