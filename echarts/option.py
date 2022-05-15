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
    def __init__(self, key, override_key=None, *args):
        self.key = key
        if override_key != None:
            self.key = override_key
        self._jsn = dict()
        #self._jsn.update(kwargs)
        for a in args:
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
        super().__init__('title',*args)


class Legend(Base):
    '''
    Legend component shows symbol, color and name of different series. 
    You can click legends to toggle displaying series in the chart.

    - type: plain, scroll
    - show: Show
    - left: Left
    - right: Right
    - top: Top
    - bottom: Bottom
    - width: Width
    - height: Height
    - orient: horizontal, vertical
    - align: Align


    TODO
    '''
    def __init__(self, type='plain', *args):
        args = Prop('type',type) + args
        super().__init__(*args)

class Grid(Base):
    '''
    TODO
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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


class Tooltip(Base):
    """A tooltip when hovering."""

    def __init__(self, trigger='axis', **kwargs):
        assert trigger in ('axis', 'item')
        self.trigger = trigger

        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {
            'trigger': self.trigger,
        }
        if self._kwargs:
            json.update(self._kwargs)
        return json


class Series(Base):
    """ Data series holding. """
    def __init__(self, type, name=None, data=None, **kwargs):
        types = (
            'bar', 'boxplot', 'candlestick', 'chord', 'effectScatter',
            'eventRiver', 'force', 'funnel', 'gauge', 'graph', 'heatmap',
            'k', 'line', 'lines', 'map', 'parallel', 'pie', 'radar',
            'sankey', 'scatter', 'tree', 'treemap', 'venn', 'wordCloud'
        )
        assert type in types
        self.type = type
        self.name = name
        self.data = data or []
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {
            'type': self.type,
            'data': self.data
        }
        if self.name:
            json['name'] = self.name
        if self._kwargs:
            json.update(self._kwargs)
        return json


class Toolbox(Base):
    """ A toolbox for visitor. """

    def __init__(self, orient='horizontal', position=None, **kwargs):
        assert orient in ('horizontal', 'vertical')
        self.orient = orient
        if not position:
            position = ('right', 'top')
        self.position = position
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {
            'orient': self.orient,
            'x': self.position[0],
            'y': self.position[1]
        }
        if self._kwargs:
            json.update(self._kwargs)
        return json

    
class VisualMap(Base):
    """maps data to visual channels"""

    def __init__(self, type, min, max,  **kwargs):
        assert type in ("continuous", "piecewise")
        self.type = type
        self.min = min
        self.max = max
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data"""
        json = {
            "type": self.type,
            'min': self.min,
            'max': self.max
        }
        if self._kwargs:
            json.update(self._kwargs)
        return json

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

    TODO
    '''
    def __init__(self, override_key=None, *args):
        super().__init__('textStyle', override_key=override_key, *args)

class SubTextStyle(TextStyle):
    '''
    - color: Color
    - fontStyle: FontStyle
    - fontWeight: FontWeight
    - fontFamily: FontFamily
    - fontSize: FontSize
    - lineHeight: LineHeight

    TODO
    '''
    def __init__(self, *args):
        super().__init__(override_key='subTextStyle', *args)

class Label(Base):
    '''
    - show:
    - align: left, center, right
    - verticalAlign: top, middle, bottom

    TODO
    '''
    def __init__(self, *args):
        super().__init__(*args)

class LineStyle(Base):
    '''
    - type: solid, dashed, dotted
    - color: Color
    - width: Width
    - opacity: Opacity

    TODO
    '''
    def __init__(self, type='solid', *args):
        args = Prop('type',type) + args
        super().__init__(*args)

#endregion