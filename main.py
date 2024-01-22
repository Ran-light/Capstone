import numpy as np
# import cv2
from scipy import interpolate

from pathlib import Path

import matplotlib.pyplot as plt

import re

import os

from get_lst import read_all

from function import plot_piecewise_lagrange, plot_piecewise_lagrange_3d, get_bbox

directory = r"D:\Capstone\recording_1\annotated_rgb\labels"
id_time, x_dict, y_dict, id_time_tp, xy_tuple, label, time_list = read_all(directory)

end_list: list[list[int, float, float, float]] = []
intermediate_list: list[int, float, float, float] = []
for i in label:
    for j in range(len(id_time_tp)):
        if i == id_time_tp[j][0]:
            intermediate_list = [i, id_time_tp[j][1], xy_tuple[j][0], xy_tuple[j][1]]
        end_list.append(intermediate_list)
# print(end_list)

# points for 1s time interval for each label
base = 0
interval_point = []
label_ends = []
for i in range(len(end_list)-1):
    for j in label:
        if j == end_list[i][0]:
            if float(end_list[i][1]) - float(end_list[base][1]) > 1:
                base = i
                interval_point.append(i)
        else:
            label_ends.append(j)
# print(interval_point)
# print(label_ends[:len(label)-1])

x_42 = []
x_44 = []
x_65 = []
x_76 = []
y_42 = []
y_44 = []
y_65 = []
y_76 = []
time_42 = []
time_44 = []
time_65 = []
time_76 = []
x: list[list] = []
y: list[list] = []
for i in end_list:
    x_42.append(i[2])
    y_42.append(i[3])
    time_42.append(i[1])
    if end_list.index(i) >= 44:
        x_44.append(i[2])
        y_44.append(i[3])
        time_44.append(i[1])
        if end_list.index(i) >= 65:
            x_65.append(i[2])
            y_65.append(i[3])
            time_65.append(i[1])
            if end_list.index(i) >= 76:
                x_76.append(i[2])
                y_76.append(i[3])
                time_76.append(i[1])

new_42_x = [float(i) for i in x_42]
new_42_y = [float(i) for i in y_42]
new_time_42 = [float(i) for i in time_42]

new_44_x = [float(i) for i in x_44]
new_44_y = [float(i) for i in y_44]
new_time_44 = [float(i) for i in time_44]

x_interpolated = np.interp(new_42_x, new_42_x, new_42_y)

bbox = get_bbox(directory)

