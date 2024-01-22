import numpy as np
# import cv2
from scipy import interpolate

from pathlib import Path

import matplotlib.pyplot as plt

import re

import os

# try to work with all in a dict with tuple

directory = r"D:\Capstone\recording_1\annotated_rgb\labels"
directory_recording_3 = r"D:\Capstone\recording_3\annotated_rgb\labels"
directory_3 = r"D:\Capstone\recording_4\annotated_rgb\labels"


def read_all(directory: object) -> object:
    url_list = []
    time_list = []
    x_coordinate = []
    y_coordinate = []
    label = []
    x_dict: dict[float: float] = dict()
    y_dict: dict[float: float] = dict()
    id_time: dict[int: float] = dict()

    id_time_tp: list[tuple(int, float)] = []
    xy_tuple: list[tuple(float, float)] = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            url_list.append(filepath)
            numeric_part = re.search(r'(\d+(\.\d+)?)', filename).group(1)
            time_list.append(float(numeric_part))
            with open(filepath) as f:
                items = f.read().strip().split("\n")
                for i in range(len(items) - 1):
                    coordinate = items[i].split(" ")
                    id, x_center, y_center, width, height = coordinate
                    if id in label:
                        id_time_tp.append(([id, numeric_part]))
                    else:
                        label.append(id)
                        id_time_tp.append(([id, numeric_part]))
                    x_coordinate.append(float(x_center))
                    y_coordinate.append(float(y_center))
                    id_time[numeric_part] = id
                    x_dict[x_center] = numeric_part
                    y_dict[y_center] = numeric_part
                    xy_tuple.append(([x_center, y_center]))

    return id_time, x_dict, y_dict, id_time_tp, xy_tuple, label, time_list


id_time, x_dict, y_dict, id_time_tp, xy_tuple, label, time_list = read_all(directory_recording_3)

# x_interpolated = np.interp(new_42_x, new_42_x, new_42_y)
# # x_cubic_spline = interpolate.CubicSpline(new_42_x, new_42_y)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")
# # ax.plot(x_coordinate[:len(time_list)], time_list, y_coordinate[:len(time_list)], color = 'b')
# # ax.plot(x_interpolated, time_list, new_44_y, color = 'r')
#
# ax.plot(new_42_x, new_time_42, new_42_x, color = 'b')
# ax.plot(x_interpolated, new_time_42, new_42_y, color = 'r')
#
# plt.show()