# Copyright (c) 2018, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import os
import numpy as np

import config_eval as config
import tfutil
import misc
#----------------------------------------------------------------------------
# Main entry point.
# Calls the function indicated in config.py.

if __name__ == "__main__":
	misc.init_output_logging()
	np.random.seed(config.random_seed)
	print('Initializing TensorFlow...')
	os.environ.update(config.env)
	tfutil.init_tf(config.tf_config)
	print('Running %s()...' % config.train['func'])
	tfutil.call_func_by_name(**config.train)
	print('Exiting...')

#----------------------------------------------------------------------------
