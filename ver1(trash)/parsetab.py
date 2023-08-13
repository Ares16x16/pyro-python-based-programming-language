
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BEGIN END IDENTIFIER INT MULTIPLY PLUS PRINTstatement : IDENTIFIER ASSIGN expressionexpression : expression PLUS expression\n                  | expression MULTIPLY expressionexpression : INT\n                  | IDENTIFIERstatement : PRINT expressionprogram : BEGIN statement_list ENDstatement_list : statement_list statement\n                      | statement'
    
_lr_action_items = {'IDENTIFIER':([0,3,4,9,10,],[2,7,7,7,7,]),'PRINT':([0,],[3,]),'$end':([1,5,6,7,8,11,12,],[0,-6,-4,-5,-1,-2,-3,]),'ASSIGN':([2,],[4,]),'INT':([3,4,9,10,],[6,6,6,6,]),'PLUS':([5,6,7,8,11,12,],[9,-4,-5,9,9,9,]),'MULTIPLY':([5,6,7,8,11,12,],[10,-4,-5,10,10,10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([3,4,9,10,],[5,8,11,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IDENTIFIER ASSIGN expression','statement',3,'p_statement_assign','pyroParser.py',6),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','pyroParser.py',10),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binop','pyroParser.py',11),
  ('expression -> INT','expression',1,'p_expression_value','pyroParser.py',15),
  ('expression -> IDENTIFIER','expression',1,'p_expression_value','pyroParser.py',16),
  ('statement -> PRINT expression','statement',2,'p_statement_print','pyroParser.py',20),
  ('program -> BEGIN statement_list END','program',3,'p_program','pyroParser.py',25),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','pyroParser.py',29),
  ('statement_list -> statement','statement_list',1,'p_statement_list','pyroParser.py',30),
]
