import numpy as np
import matplotlib.pyplot as plt
# imports needed packages


def hex_to_rgb(value):  # converts hex codes into a tuple of RGB values
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


f = open("data.txt", "r")
data_lines = f.readlines()
# reads info from the data file

R_x = []
G_x = []
B_x = []
scores_y = []
# creates empty lists to store RGB and score information

for line in data_lines:  # adds data from file to lists in percentage form
    line_data = line.rstrip("\n").split("\t")
    hex_data = hex_to_rgb(line_data[0])

    hex_sum = sum(hex_data)

    if hex_sum > 0:  # converts RGB values to percentages
        hex_data = tuple([round(hex_value / hex_sum, 3) for hex_value in hex_data])
    else:
        hex_data = tuple(hex_data)

    R_x.append(hex_data[0] * 100)
    G_x.append(hex_data[1] * 100)
    B_x.append(hex_data[2] * 100)
    scores_y.append(float(line_data[1]))
    # adds data to the lists used

R_x = np.array(R_x)
G_x = np.array(G_x)
B_x = np.array(B_x)
scores_y = np.array(scores_y)
# formats lists into numpy arrays

m1, b1 = np.polyfit(R_x, scores_y, 1)
m2, b2 = np.polyfit(G_x, scores_y, 1)
m3, b3 = np.polyfit(B_x, scores_y, 1)
# finds slope and y-intercept values for a regression line

r1 = np.corrcoef(R_x, scores_y)[0][1]
r2 = np.corrcoef(G_x, scores_y)[0][1]
r3 = np.corrcoef(B_x, scores_y)[0][1]
# finds correlation coefficients for regression lines

print("Figure 1")

if b1 > 0:
    print(f"Equation: y = {round(m1, 4)}x + {round(b1, 4)}")
else:
    print(f"Equation: y = {round(m1, 4)}x - {round(b1, 4)}")

print(f"Correlation Coefficient: {round(r1, 4)}")
fig = plt.gcf()
fig.canvas.set_window_title('Figure 1 of 3')
plt.title('Red Color Percentage Effect on Happiness')
plt.xlabel('Percentage of Red Color (%)')
plt.ylabel('Happiness Score')
plt.plot(R_x, scores_y, 'o')
plt.plot(R_x, m1 * R_x + b1)
plt.show()
# displays plot for red color and related information

print("\nFigure 2")

if b2 > 0:
    print(f"Equation: y = {round(m2, 4)}x + {round(b2, 4)}")
else:
    print(f"Equation: y = {round(m2, 4)}x - {round(b2, 4)}")

print(f"Correlation Coefficient: {round(r2, 4)}")
fig = plt.gcf()
fig.canvas.set_window_title('Figure 2 of 3')
plt.title('Green Color Percentage Effect on Happiness')
plt.xlabel('Percentage of Green Color (%)')
plt.ylabel('Happiness Score')
plt.plot(G_x, scores_y, 'o')
plt.plot(G_x, m2 * G_x + b2)
plt.show()
# displays plot for green color and related information

print("\nFigure 3")

if b3 > 0:
    print(f"Equation: y = {round(m3, 4)}x + {round(b3, 4)}")
else:
    print(f"Equation: y = {round(m3, 4)}x - {round(b3, 4)}")

print(f"Correlation Coefficient: {round(r3, 4)}")
fig = plt.gcf()
fig.canvas.set_window_title('Figure 3 of 3')
plt.title('Blue Color Percentage Effect on Happiness')
plt.xlabel('Percentage of Blue Color (%)')
plt.ylabel('Happiness Score')
plt.plot(B_x, scores_y, 'o')
plt.plot(B_x, m3 * B_x + b3)
plt.show()
# displays plot for blue color and related information