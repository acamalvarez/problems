import base64
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def get_image():
    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as its 'file
    plt.savefig(buffer, format="png")
    # set the cursor at the begining of the stream
    buffer.seek(0)
    # retreive the entire content of the 'file
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")

    # free the memory of the buffer
    buffer.close()

    return graph


def solve_problem(k1A, k2A, k3B, k4C, CA0, CB0):

    C0 = [CA0, CB0, 0.0, 0.0, 0.0, 0.0]
    Vspan = np.linspace(0, 10, 51)
    C = odeint(equations, C0, Vspan, args=(k1A, k2A, k3B, k4C))

    plt.switch_backend("AGG")
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(Vspan, C)
    ax.set_xlabel(r"Volume / dm$^3$")
    ax.set_ylabel(r"Concentration / mol / dm$^3$")
    plt.legend("ABCDEF", loc="best")

    plt.tight_layout()

    graph = get_image()

    return graph


def equations(C, V, k1A, k2A, k3B, k4C):

    cA = C[0]
    cB = C[1]
    cC = C[2]

    r1A = -k1A * cA * cB ** 2
    r2A = -k2A * cA * cB
    r3B = -k3B * cC ** 2 * cB
    r4C = -k4C * cC * cA ** (2 / 3)

    C = (
        r1A + r2A + (2 / 3) * r4C,
        1.25 * r1A + 0.75 * r2A + r3B,
        -r1A + 2 * r3B + r4C,
        -1.5 * r1A - 1.5 * r2A - r4C,
        -0.5 * r2A - (5 / 6) * r4C,
        -2 * r3B,
    )

    return C
