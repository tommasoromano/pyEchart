# -*- coding: utf-8 -*-

"""
    echarts.option
    ~~~~~~~~~~~~~~
    Options for chart
    https://echarts.apache.org/en/option.html
"""
import json
from echarts.props import *

################################
#   BASE
################################
#region BASE

class Base(object):
    def __init__(self, key, override_key, *args):
        self.key = key
        if override_key != None:
            self.key = override_key
        self._jsn = dict()
        #self._jsn.update(kwargs)
        print(args)
        for a in args:
            print(a)
            if isinstance(a, Prop):
                self._jsn[a.key] = a.value
            elif isinstance(a, Base):
                self._jsn[a.key] = a.to_dict()

    def to_dict(self):
        """DICT format data."""
        self.__fix_dict__()
        return self._jsn

    def __fix_dict__(self):
        for k in self._jsn.keys():
            if isinstance(self._jsn[k], Prop):
                self._jsn[k] = self._jsn[k].value
            if isinstance(self._jsn[k], Base):
                self._jsn[k] = self._jsn[k].to_dict()

class Title(Base):
    '''
    Title component, including main title and subtitle.
    There could be one or more than one title components. It is more useful when multiple diagrams in one instance all need titles.

    https://echarts.apache.org/en/option.html#title

    - show: Show
    - text: Text
    - textStyle: TextStyle 
    - subtext: SubText
    - subtextStyle: TextStyle
    - textAlign: TextAlign
    - textVerticalAlign: TextVerticalAlign
    - padding: Padding
    - left: Left 
    - right: Right
    - top: Top
    - bottom: Bottom 

    TODO
    '''
    def __init__(self, *args):
        super().__init__('title', None, *args)

class Legend(Base):
    '''
    Legend component shows symbol, color and name of different series. 
    You can click legends to toggle displaying series in the chart.
    
    https://echarts.apache.org/en/option.html#legend

    - type: LegendType
    - show: Show
    - left: Left
    - right: Right
    - top: Top
    - bottom: Bottom
    - width: Width
    - height: Height
    - orient: Orient
    - align: Align

    TODO
    '''
    def __init__(self, *args):
        super().__init__('legend', None, *args)

class Grid(Base):
    '''
    Drawing grid in rectangular coordinate. 
    In a single grid, at most two X and Y axes each is allowed. 
    Line chart, bar chart, and scatter chart (bubble chart) can be drawn in grid.
    In ECharts 2.x, there could only be one single grid component 
    at most in a single echarts instance. 
    But in ECharts 3, there is no limitation.

    **Make sure the ars**

    - show: Show
    - left: Left ('10%')
    - top: Top (60)
    - right: Right ('10%')
    - bottom: Bottom (60)
    - width: Width ('auto')
    - height: Height ('auto')

    TODO
    '''
    def __init__(self, *args):
        super().__init__('grid', None, *args)

class Axis(Base):
    '''
    - show: 
    - position: top, bottom
    - type: value, category, time, log
    - name:
    - nameLocation: start, middle, center, end
    - nameTextStyle: TextStyle
    - min: TODO number, string, function
    - max: TODO number, string, function
    - axisLine: TODO


    TODO
    '''
    def __init__(self, key, override_key=None, *args):
        super().__init__(key, *args)

#endregion
################################
#   BASE_SECONDARY
################################
#region BASE_SECONDARY

class TextStyle(Base):
    '''
    - color: Color
    - fontStyle: FontStyle
    - fontWeight: FontWeight
    - fontFamily: FontFamily
    - fontSize: FontSize
    - lineHeight: LineHeight

    DONE
    TODO
    '''
    def __init__(self, override_key, *args):
        super().__init__('textStyle', override_key, *args)

class SubTextStyle(TextStyle):
    '''
    - color: Color
    - fontStyle: FontStyle
    - fontWeight: FontWeight
    - fontFamily: FontFamily
    - fontSize: FontSize
    - lineHeight: LineHeight

    DONE
    TODO
    '''
    def __init__(self, *args):
        super().__init__('subTextStyle', *args)

class Label(Base):
    '''
    - show:
    - align: left, center, right
    - verticalAlign: top, middle, bottom

    TODO
    '''
    def __init__(self, *args):
        super().__init__('label',None,*args)

class LineStyle(Base):
    '''
    - type: LineStyleType
    - color: Color
    - width: Width
    - opacity: Opacity

    TODO
    '''
    def __init__(self, *args):
        print(args)
        super().__init__('lineStyle', None, *args)

#endregion