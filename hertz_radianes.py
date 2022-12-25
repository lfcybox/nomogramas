"""
    hertz_radianes.py
    
    \omega = 2 \pi f

"""
import sys

#sys.path.insert(0, "..")
# sys.path[:0] = [".."]
from pynomo.nomographer import Nomographer
from math import log10, log, pi

ax_f = {
    'tag': 'freq',
    'u_min': 1.0,
    'u_max': 10.0,
    'function': lambda u: log10(u),
    'title': r'$f$',
    #'title_draw_center': True,
    'title_x_shift': -0.8,
    'title_y_shift': 0.7,
    'tick_levels': 3,
    'tick_text_levels': 3,
    'tick_side': 'left',
    'scale_type': 'log'
}

ax_w = {
    'tag': 'freq',
    'u_min': 6,#1.0*2*pi,
    'u_max': 70,#10.0*2*pi,
    'function': lambda u: log10(u),
    'align_func': lambda u: u/(2*pi),
    'title': r'$\omega$',
    #'title_draw_center': True,
    'title_x_shift': 0.8,
    'tick_levels': 3,
    'tick_text_levels': 3,
    'tick_side': 'right',
    'scale_type': 'log'
}

block_f = {
    'block_type': 'type_8',
    'f_params': ax_f,
    #'width': 10.0,
    #'height': 10.0
}

block_w = {
    'block_type': 'type_8',
    'f_params': ax_w,
    #'width': 10.0,
    #'height': 10.0
}

main_params = {
    'filename': 'hertz_radianes.pdf',
    'paper_height': 10.0,
    'paper_width': 10.0,
    'block_params': [block_f, block_w],
    #'transformations': []
    'transformations': [('scale paper',)],
    'title_str': r'$ \omega = 2 \pi f$',
    'title_y':10.6, 
    'title_x':10,
}

Nomographer(main_params)