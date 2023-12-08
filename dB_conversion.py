"""
    dB_conversion.py
    
    A_dB = 20 * log10(A)

"""
import sys

#sys.path.insert(0, "..")
# sys.path[:0] = [".."]
from pynomo.nomographer import Nomographer
from math import log10, log, pi

ax_dB = {
    'tag': 'freq',
    'u_min': 0.0,
    'u_max': 20.0,
    'function': lambda u: u,
    'title': r'$A_{dB}$',
    #'title_draw_center': True,
    #'title_opposite_tick': False,
    #'title_x_shift': -0.8,
    #'title_y_shift': 0.7,
    'tick_levels': 3,
    'tick_text_levels': 1,
    'tick_side': 'left',
    'title_x_shift': -1.0,
    #'scale_type': 'lin'
}

ax_A = {
    'tag': 'freq',
    'u_min': 1.0,
    'u_max': 10.0,
    'function': lambda u: 20*log10(u),
    'align_func': lambda u: 20*log10(u),    
    'title': r'$A$',
    #'title_draw_center': True,
    #'title_x_shift': 0.8,
    'tick_levels': 3,
    'tick_text_levels': 2,
    #'tick_side': 'right',
    'title_x_shift': 1.0,
    #'scale_type': 'log'
}

block_dB = {
    'block_type': 'type_8',
    'f_params': ax_dB,
    'width': 10.0,
    'height': 5.0
}

block_A = {
    'block_type': 'type_8',
    'f_params': ax_A,
    #'width': 10.0,
    #'height': 10.0
}

main_params = {
    'filename': 'dB_conversion.pdf',
    'paper_height': 10.0,
    'paper_width': 10.0,
    'block_params': [block_dB, block_A],
    #'transformations': []
    'transformations': [('scale paper',)],
    'title_str': r'$ A_{dB} = 20 \cdot log_{10}(A)$',
    'title_y':10.6, 
    'title_x':10,
}

Nomographer(main_params)