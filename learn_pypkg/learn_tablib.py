#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tablib是kennethreitz大神用纯Python写的二维表数据的管理的包。相比pandas而言, 
可以很轻易地包含到你的项目中(因为是纯Python), 体积也较小。当然, 功能比pandas
是远远不如了。

- PyPI: https://pypi.python.org/pypi/tablib
- GitHub: https://github.com/kennethreitz/tablib
- Document: http://docs.python-tablib.org/en/latest/
"""

import tablib
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def init_from_list():
    data = tablib.Dataset(*[(1, 2), (3, 4)], headers=list("ab"))
    assert data.dict == [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    
init_from_list()


@run_if_is_main(__name__)
def init_from_scratch():
    data = tablib.Dataset()
    data.headers = list("ab")
    data.append([1, 2])
    data.append([3, 4])
    assert data.dict == [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    
init_from_scratch()


@run_if_is_main(__name__)
def select_row():
    data = tablib.Dataset(*[(1, 2), (3, 4)], headers=list("ab"))
    assert data[0] == (1, 2)
    
select_row()


@run_if_is_main(__name__)
def select_column():
    data = tablib.Dataset(*[(1, 2), (3, 4)], headers=list("ab"))
    assert data["a"] == [1, 3]
    
select_column()