""" 
    LC_osc.py

    Various expressions, with main arguments being:
    f0-Q-L-Vpp

    Relevant expressions:
    1) C = 2/(2pi*f0)^2/L
    2) Rp = 2pif0*L*Q
    3) Rs = Rp/Q^2
    4) Ibias = Vpp/(16*f0*L*Q)

    Then:
    1) type-1 with logs
    (2pi*f0)^2*L*C/2 = 1

"""

#import sys

#sys.path.insert(0, "..")
from pynomo.nomographer import Nomographer
import numpy as np

# f(L,C)
params_L = {
    'u_min': 1.0,
    'u_max': 8.0,
    'function': lambda ind: ind * 1e-6,
    'title': r'$L$ ($\mu$H)',
    'tick_levels': 4,
    'tick_text_levels': 3,
    #'scale_type': 'log smart',
    'tick_side': 'right',
    'text_format': r"$%6.6g$ ",
    # 'tag':'L',
    'dtag': 'L',
}

params_f = {
    'u_min': 3.0,
    'u_max': 4.0,
    'function': lambda f: 2.0 / (2 * np.pi * f * 1e6)**2,
    'title': r'$f$ (MHz)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    #'scale_type': 'log smart',
    'tick_side': 'left',
    'text_format': r"$%6.6g$ ",
}

params_C = {
    'u_min': 0.4,
    'u_max': 6.0,
    'function': lambda c: 1.0/(c * 1e-9),
    'title': r'$C$ (nF)',
    'tick_levels': 4,
    'tick_text_levels': 4,
    'tick_side': 'left',
    'scale_type': 'log smart',
    'text_format': r"$%6.6g$ ",
    'tag': 'C',
}

block_LfC = {
    'block_type': 'type_2',
    'width': 10.0,
    'height': 15.0,
    'f1_params': params_L,
    'f2_params': params_C,
    'f3_params': params_f,
    'isopleth_values': [[5.5, 'x', 3.5]],
    'mirror_x': True,
}

main_params = {
    'filename': 'LC_osc.pdf',
    'paper_height': 15.0,
    'paper_width': 25.0,
    'block_params': [block_LfC],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'$2\pi\cdot f_0=1/\sqrt{(LC/2)}$',
    'title_x': 5.0,
}

Nomographer(main_params)