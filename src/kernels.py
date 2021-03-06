#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Raw kernels
"""
import numpy as np
import keras.backend as K

# Simple convolution kernels


def outline():
    return np.array([[-1, -1, -1],
                     [-1, 8, -1],
                     [-1, -1, -1]])


def outline_big():
    return np.array([[-2, -2, -2, -2, -2],
                     [-2, -1, 1, -1, -2],
                     [-2, 1, 8, 1, -2],
                     [-2, -1, 1, -1, -2],
                     [-2, -2, -2, -2, -2]])


def sobel_5x():
    return np.array([[2, 1, 0, -1, -2],
                     [2, 1, 0, -1, -2],
                     [4, 2, 0, -2, -4],
                     [2, 1, 0, -1, -2],
                     [2, 1, 0, -1, -2]])


def sobel_y():
    return np.array([[1, 2, 1],
                     [0, 0, 0],
                     [-1, -2, -1]])


def triangle_5():
    return np.array([[0, 0, 1, 0, 0],
                     [0, 0.5, 1, 0.5, 0],
                     [0, 1, 1, 1, 0],
                     [0.5, 1, 1, 1, 0.5],
                     [1, 1, 1, 1, 1]])


def triangle_7():
    return np.array([[0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0.5, 1, 0.5, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0],
                     [0, 0.5, 1, 1, 1, 0.5, 0],
                     [0, 1, 1, 1, 1, 1, 0],
                     [0.5, 1, 1, 1, 1, 1, 0.5],
                     [1, 1, 1, 1, 1, 1, 1]])


def triangle_11():
    return np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0.5, 1, 0.5, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0.5, 1, 1, 1, 0.5, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0.5, 1, 1, 1, 1, 1, 0.5, 0, 0],
                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0.5, 1, 1, 1, 1, 1, 1, 1, 0.5, 0],
                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                     [0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


def simple_test():
    return np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0.5, 1, 0.5, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0.5, 1, 1, 1, 0.5, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0.5, 1, 1, 1, 1, 1, 0.5, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0.5, 1, 0.5, 0, 0, 0, 0.5, 1, 0.5, 0],
                     [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                     [0.5, 1, 1, 1, 0.5, 0, 0.5, 1, 1, 1, 0.5],
                     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]])


def my_rescaler(X):
    max_val = K.max(K.max(X, axis=2, keepdims=True), axis=3)[0, 0, 0, 0]
    min_val = K.min(K.min(X, axis=2, keepdims=True), axis=3)[0, 0, 0, 0]
    return 255*(X - min_val)/(max_val - min_val)
