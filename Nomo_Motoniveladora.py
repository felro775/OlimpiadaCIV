import math
from pynomo.nomographer import *
D_params={
'u_min':2.0,
'u_max':4.0,
'function':lambda u:-math.log10(u),
'scale_type':'linear',
'title':r'\Large $D$',
'tick_levels':2,
'tick_text_levels':1,
'tick_side':'left',
}

a_params={
'u_min':0.1,
'u_max':1.0,
'function':lambda u:-math.log10(u),
'scale_type':'linear',
'title':r'\Large $a$',
'tick_levels':3,
'tick_text_levels':2,
'tick_side':'left',
}

t_params={
'u_min':0.1,
'u_max':1.0,
'function':lambda u:math.log10(u),
'scale_type':'linear',
'title':r'\Large $t$',
'tick_levels':3,
'tick_text_levels':2,
'tick_side':'left',
}

R_params={
'u_min':1.0,
'u_max':3.0,
'function':lambda u:math.log10(u),
'scale_type':'linear',
'title':r'\Large $R$',
'tick_levels':3,
'tick_text_levels':1,
}

block_1_params={
'block_type':'type_3',
'width':10.0,
'height':10.0,
'reference_titles':['Ref. 1','Ref. 2'],
'f_params':[D_params,a_params,t_params,R_params],
}

main_params={
'filename':'Rend_Motoniveladora.pdf',
'paper_height':40.0,
'paper_width':40.0,
'block_params':[block_1_params],
'transformations':[('rotate',0.01),('scale paper',)],
'title_x':10.0,
'title_y':-1.0,
'title_box_width': 20.0,
'title_str':r'Rendimiento = (D $\times$ a ) \
/ (t)',
}
Nomographer(main_params)
