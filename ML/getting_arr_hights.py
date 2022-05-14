import pitch
import os
from statistics import mean
import numpy as np


p = pitch.find_pitch('test_audio.wav')
file_list = os.listdir('/home/olga/Project/audio')
sorted_file_list = sorted(file_list)

number_of_elements = len(sorted_file_list)
print("Number of elements in the list: ", number_of_elements)

arr = []

j = 1
for elem in sorted_file_list:
    p = pitch.find_pitch('audio/' + elem)
    arr.append(p)
    print(j)
    j += 1

i = 1
for elem in arr:
    print(i, 'pitch = ', elem)
    i += 1

print('max: ', max(arr))
print('min: ', min(arr))
print('mean: ', mean(arr))
print('std: ', np.std(arr))