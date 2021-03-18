
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE END EQUAL LKAKKO MINUS NAME NUMBER PLUS RKAKKO STA TIMESexpr : NAME NAME EQUAL NAMEexpr : NAME NAME PLUS SENTexpr : NAME NAME EQUAL NAME PLUS NAMEexpr : NAME NAMEexpr : NAME NAME EQUAL NAME MINUS NAMEexpr : NAME NAME MINUS SENTSENT : exprexpr : NAME NAME LKAKKO NAME RKAKKO STAexpr : NUMBER'
    
_lr_action_items = {'NAME':([0,2,5,6,7,8,14,15,],[2,4,9,2,2,13,17,18,]),'NUMBER':([0,6,7,],[3,3,3,]),'$end':([1,3,4,9,10,11,12,17,18,19,],[0,-9,-4,-1,-2,-7,-6,-3,-5,-8,]),'EQUAL':([4,],[5,]),'PLUS':([4,9,],[6,14,]),'MINUS':([4,9,],[7,15,]),'LKAKKO':([4,],[8,]),'RKAKKO':([13,],[16,]),'STA':([16,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,6,7,],[1,11,11,]),'SENT':([6,7,],[10,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> NAME NAME EQUAL NAME','expr',4,'p_mov','main.py',62),
  ('expr -> NAME NAME PLUS SENT','expr',4,'p_add','main.py',71),
  ('expr -> NAME NAME EQUAL NAME PLUS NAME','expr',6,'p_addandmov','main.py',77),
  ('expr -> NAME NAME','expr',2,'p_msg','main.py',86),
  ('expr -> NAME NAME EQUAL NAME MINUS NAME','expr',6,'p_subandmov','main.py',92),
  ('expr -> NAME NAME MINUS SENT','expr',4,'p_sub','main.py',101),
  ('SENT -> expr','SENT',1,'p_SENT','main.py',107),
  ('expr -> NAME NAME LKAKKO NAME RKAKKO STA','expr',6,'p_define','main.py',112),
  ('expr -> NUMBER','expr',1,'p_expr2NUM','main.py',117),
]
