"""
    deg_rad2.py
    
    1 deg = 180/pi * 1 radian

"""

#import sys
#sys.path.insert(0, "..")
from pynomo.nomographer import Nomographer
import numpy as np

ax_deg = {
    'tag': 'ang',
    'u_min': 0.0,
    'u_max': 359.0,
    'function_x': lambda u: 3 * np.cos(u / 180.0 * np.pi),
    'function_y': lambda u: 3 * np.sin(u / 180.0 * np.pi),
    'title': r'$degrees$',
    'tick_levels': 3,
    'tick_text_levels': 3,
    #'text_format': r'$%4.4g$',
    'title_x_shift': 1,
    'title_y_shift': 1,
    'scale_type': 'linear',
    }
    
block_deg = {
    'block_type': 'type_8',
    'f_params': ax_deg,
    'width': 5.0,
    'height': 15.0,
    }

ax_rad = {
    'tag': 'ang',
    'u_min': 0.0,
    'u_max': 359.0*np.pi/180,
    'function_x': lambda u: 3 * np.cos(u ),
    'function_y': lambda u: 3 * np.sin(u ),
    'align_func': lambda u: u*180/np.pi,    
    'title': r'$radians$',
    'tick_levels': 3,
    'tick_text_levels': 3,
    #'text_format': r'$%4.4g$',
    'tick_side': 'left',
    'title_x_shift': 1,
    'title_y_shift': -2,
    'scale_type': 'linear',
    'extra_params':[{
        'scale_type': 'manual arrow',
        'manual_axis_data': {
            0.7853: r'$\pi/4$',
            1.5707: r'$\pi/2$',
            2.356:  r'$3/4\pi$',
            3.1415: r'$\pi$',
            4.7123: r'$3/2\pi$',
            },
        'arrow_length': 2.0,
        }]
    }   

block_rad = {
    'block_type': 'type_8',
    'f_params': ax_rad,
    'width': 5.0,
    'height': 15.0,
    }    
    
main_params = {
    'filename': 'deg_rad2.pdf',
    'paper_height': 10.0,
    'paper_width': 10.0,
    'block_params': [block_deg,block_rad],
    'title_str': r'$angle[deg] = angle[rad] \cdot 180/\pi $',  
    'title_y': 5, 
    'title_x': 5,    
    'transformations': [('scale paper',)]
    }
               
Nomographer(main_params)
