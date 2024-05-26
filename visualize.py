#!/usr/bin/env python3

import matplotlib.pyplot as plt
import wave
import sys
import struct
import os
import concurrent.futures

def get_files_list(directory):
    return [file for file in os.listdir(directory)]


def make_plot(data):
    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(data)
    plt.show()


def bytes_dump(file):
    with open(file, 'rb') as fobj:
        raw_bytes = fobj.read()
        return raw_bytes


def bits_dump(file):
    with open(file, 'rb') as fobj:
        raw_bytes = fobj.read()
        return ''.join(map(lambda x: '{:08b}'.format(x), raw_bytes))


def get_signals(file):
    spf = wave.open(file, "r")
    # Extract Raw Audio from Wav File
    signal = spf.readframes(-1)
    
    signal_tuple = struct.unpack('<' + 'h' * (len(signal) // 2), signal)
    # Convert the tuple to a list (optional, if you prefer to work with lists)
    signal_list = list(signal_tuple)
    return signal_list


def get_deltas(nums):
    return [nums[i] - nums[i - 1] for i in range(1, len(nums))]


def make_as_dict(data):
    data_dict = {}
    for i in data:
        data_dict[i] = data_dict.get(i, 0) + 1
    
    return data_dict

def get_all_files_freqs():
    all_dicts = []
    dir = 'data'
    files = get_files_list(dir)
    
    for file in files:
        print(f"file: {file}")
        signals = get_signals(f'{dir}/{file}')
        res = get_deltas(signals)
        freq = make_as_dict(res)
        all_dicts.append(freq)

    joined_dict = {}
    for i in all_dicts:
        joined_dict = joined_dict | i
    print(joined_dict)


def main():
    data = get_signals('in.wav')
    data = get_deltas(data)
    print(f"max:{max(data)}, min:{min(data)}")

if __name__ == '__main__':
    main()