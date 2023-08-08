"""
Dimensiones del telescopio Newtoniano:
S = F - Rt - E
S: Separación entre espejo principal y secundario
F: Distancia Focal del primario (= 0.5 * Radio de curvatura)
Rt: Radio exterior del tubo
E: Mitad de recorrido del porta-ocular (desde su base)

Nomograma tipo 3:
(S - F) + (Rt + E) = 0
"""

"""
    ex_type3_nomo_1.py

    Simple nomogram of type 3: F1 + F2 + ... + FN = 0

    This example has N = 6: F1 + F2 + F3 + F4 + F5 + F6 = 0

    Copyright (C) 2007-2009  Leif Roschier

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys

sys.path.insert(0, "..")
from pynomo.nomographer import Nomographer

N_S = {
    'u_min': 0.85,
    'u_max': 1.25,
    'function': lambda u: u,
    'title': r'$S [m]$',
    'tick_levels': 3,
    'tick_text_levels': 3,
    'tick_side': 'left',
}
N_F = {
    'u_min': 1.1,
    'u_max': 1.4,
    'function': lambda u: -1*u,
    'title': r'$F [m]$',
    'tick_levels': 2,
    'tick_text_levels': 1,
}
N_Rt = {
    'u_min': 5,
    'u_max': 18,
    'function': lambda u: u/100, #valor en cm
    'title': r'$R_T [cm]$',
    'tick_levels': 2,
    'tick_text_levels': 1,
}
N_E = {
    'u_min': 0,#5,
    'u_max': 20,#15,
    'function': lambda u: u/100, #valor en cm
    'title': r'$E [cm]$',
    'tick_levels': 2,
    'tick_text_levels': 1,
    'tick_side': 'left',
}

# block_1_params = {
#     'block_type': 'type_3',
#     'width': 10.0,
#     'height': 10.0,
#     'f_params':        [ N_Rt,  N_E,    N_S,    N_F],
#     'isopleth_values': [[  10,    8,    'x',  1.225]],
# }

block_1_params = {
    'block_type': 'type_3',
    'width': 10.0,
    'height': 10.0,
    'reference_titles': [''],
    'f_params':        [ N_Rt,  N_F,    N_S,    N_E],
    'isopleth_values': [[  10,    1.225,    'x',  8]],
}

# main_params = {
#     'filename': 'Telescopio.pdf',
#     'paper_height': 20.0,
#     'paper_width': 20.0,
#     'block_params': [block_1_params],
#     'transformations': [('rotate', 0.01), ('scale paper',)],
#     'title_str': r'$S = F - R_T - E$',
#     'title_y': 21.0,
# }

main_params = {
    'filename': 'Telescopio.pdf',
    'paper_height': 20.0,
    'paper_width': 15.0,
    'block_params': [block_1_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'$S = F - R_T - E$',
    'title_y': 19.0,
    'title_x': 2.0,
}
Nomographer(main_params)
