"""
A suite of utility functions that assist in carrying out the analysis
=====================================================================

!! Please import as a module and use it as such -- not as a script !!

"""
# Created: Thu May 26, 2016  03:50PM
# Last modified: Fri Apr 19, 2019  10:54pm
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>


from progressbar import ProgressBar, Bar, Percentage, ETA
import numpy as np


def _printmsg(msg, verbose):
    """
    Prints given message according to specified varbosity level.
    """
    if verbose:
        print(msg)
    return None


def progressbar_start(max_value, pbar_on, pbar_title="Progress: "):
    """
    Starts a progress bar as per given maximum value.
    """
    prog_bar = None
    widgets = [pbar_title,
               Percentage(),
               ' ',
               Bar(marker=u'\u25fc', left='[', right=']', fill=u'\u00b7'),
               ' ',
               ETA(format="ETA:"),
               ' ',
               ]
    if pbar_on:
        prog_bar = ProgressBar(maxval=max_value,
                               widgets=widgets,
                               term_width=80)
        prog_bar.start()
    return prog_bar


def progressbar_update(prog_bar, i):
    """
    Updates current progress bar with integer i.
    """
    if prog_bar:
        prog_bar.update(i)
    return None


def progressbar_finish(prog_bar):
    """
    Terminates a given progress bar.
    """
    if prog_bar:
        prog_bar.finish()
    return None


