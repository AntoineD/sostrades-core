'''
Copyright 2022 Airbus SAS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
# -*-mode: python; py-indent-offset: 4; tab-width: 8; coding: iso-8859-1 -*-
import numpy as np


class FDScheme(object):
    """
    Abstract class for finite differences numerical scheme.
    """

    def __init__(self, fd_step, bounds=None):
        """
        Constructor.
        Args :
            fd_step : finite differences step
        """
        self.__fd_step = fd_step
        self.__samples = []
        self.__bounds = bounds
        self.__n = 0
        self.order = 0
        self.dtype = np.float

    def get_order(self):
        """
        Accessor for the order of the scheme
        Returns :
            the scheme order
        """
        return self.order

    def set_order(self, order):
        self.order = order
        if self.order == 1j:
            self.dtype = np.complex128
        else:
            self.dtype = np.float

    def get_bounds(self):
        return self.__bounds

    def set_x(self, x):
        """
        Setter for the variables values at which the finite differences are comptued
        Args :
            x  : variables values
        """
        self.__x = x
        self.__n = np.shape(x)[0]

    def set_bounds(self, bounds):
        self.__bounds = bounds

    def get_x(self):
        """
        Accessor for the  variables
        Returns :
            x : the variables set
        """
        return self.__x

    def generate_samples(self):
        """
        Implementation of the perturbations of the variables.
        Computes a set of perturbed variables at which the function will be called.
        For instance : [(x0-fd_step, x1), (x0, x1-fd_step),(x0+fd_step, x1), (x0, x1+fd_step)]
        for a second order centered scheme.
        """
        pass

    def get_fd_step(self):
        """
        Accessor for the finite differences step.
        Returns :
            The step
        """
        return self.__fd_step

    def get_samples(self):
        """
        Accessor for the samples generated by self.generate_samples().
        Returns:
            A list of perturbed variables set.
        """
        return self.__samples

    def set_samples(self, samples):
        """
        Setter for the samples.
        Args:
            samples : a  list of perturbed variables set.
        """
        self.__samples = samples

    def compute_grad(self, y_array):
        """
        Gradient computation from the function calculated at the perturbed
         variables set.
        Args :
            y_array : the array of functions values calculated at the perturbed
         variables set.
        """
        return None

    def get_grad_dim(self):
        """
        Accessor for the gradient dimension.
        Returns :
            the gradient dimension.
        """
        return self.__n
