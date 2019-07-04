#!/usr/bin/python -tt
# Project: Dropbox (Indigo Wire Networks)
# Filename: md2pdf
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2019-07-03"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse




class FilterModule(object):
    def filters(self):
        return {
            'md2pdf': self.a_filter,
            'another_filter': self.b_filter
        }

    def a_filter(self, a_variable):
        a_new_variable = a_variable + ' CRAZY NEW FILTER'
        return a_new_variable


def main():
    pass


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python md2pdf' ")
    arguments = parser.parse_args()
    main()
