#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys


def get_logger(name=None, filename=None, level=logging.ERROR):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if filename:
        fh = logging.FileHandler(filename)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
