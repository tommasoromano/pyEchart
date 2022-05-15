


################################
#   PROP
################################
#region PROP

class Prop(object):
    def __init__(self, key, value, override_key=None):
        self.key = key
        if override_key != None:
            self.key = override_key
        self.value = value

class Type(Prop):
    '''
    Different from option to option
    - Legend: plain, scroll
    - LineStyle: solid, dashed, dotted
    '''
    def __init__(self, value):
        super().__init__('type', value)

class Show(Prop):
    '''
    Set this to false to prevent the option from showing
    
    - bool
    '''
    def __init__(self, value):
        super().__init__('show', value)

class Text(Prop):
    '''
    - string
    '''
    def __init__(self, value, override_key=None):
        super().__init__('text', value, override_key=override_key)

class SubText(Text):
    '''
    - string
    '''
    def __init__(self, value):
        super().__init__(value, override_key='subText')

class Align(Prop):
    '''
    - string: auto, left, right, center
    '''
    def __init__(self, value, override_key=None):
        super().__init__('align', value, override_key=override_key)

class TextAlign(Align):
    '''
    - string: auto, left, right, center
    '''
    def __init__(self, value):
        super().__init__(value, override_key='textAlign')

class VerticalAlign(Prop):
    '''
    - string: auto, top, bottom, middle
    '''
    def __init__(self, value, override_key=None):
        super().__init__('verticalAlign', value, override_key=override_key)

class TextVerticalAlign(VerticalAlign):
    '''
    - string: auto, top, bottom, middle
    '''
    def __init__(self, value):
        super().__init__(value, override_key='textVerticalAlign')

class Padding(Prop):
    '''
    - number: for top/bottom/left/right
    - array2: [top/bottm, left/right]
    - array4: [top, bottom, left, right]

    (es. 5, es. [5, 8], es. [5, 3, 8, 9])
    '''
    def __init__(self, value):
        super().__init__('padding',value)

class Left(Prop):
    '''
    - string: auto, left, center, right 
    - number: pixel value
    - string percentge: (es. 20%)
    '''
    def __init__(self, value):
        super().__init__('left',value)

class Right(Prop):
    '''
    - string: auto, left, center, right 
    - number: pixel value
    - string percentge: (es. 20%)
    '''
    def __init__(self, value):
        super().__init__('right',value)

class Top(Prop):
    '''
    - string: auto, left, center, right 
    - number: pixel value
    - string percentge: (es. 20%)
    '''
    def __init__(self, value):
        super().__init__('top',value)

class Bottom(Prop):
    '''
    - string: auto, left, center, right 
    - number: pixel value
    - string percentge: (es. 20%)
    '''
    def __init__(self, value):
        super().__init__('bottom',value)

class Width(Prop):
    '''
    - string: auto
    - number: pixel value
    '''
    def __init__(self, value):
        super().__init__('width',value)

class Height(Prop):
    '''
    - string: auto
    - number: pixel value
    '''
    def __init__(self, value):
        super().__init__('height',value)

class Orient(Prop):
    '''
    - string: horizontal, vertical
    '''
    def __init__(self, value):
        super().__init__('orient',value)

class Color(Prop):
    '''
    - string: (es. #333)
    '''
    def __init__(self, value):
        super().__init__('color', value)

class Opacity(Prop):
    '''
    - number: [0, 1]
    '''
    def __init__(self, value):
        super().__init__('opacity', value)

class FontStyle(Prop):
    '''
    - string: normal, italic, oblique
    '''
    def __init__(self, value):
        super().__init__('fontStyle', value)

class FontWeight(Prop):
    '''
    - string: normal, bold, bolder, lighter
    - number: 100, 200, 300, 400...
    '''
    def __init__(self, value):
        super().__init__('fontWeight', value)

class FontFamily(Prop):
    '''
    - string: sans-serif, serif, monospace, ...
    '''
    def __init__(self, value):
        super().__init__('fontFamily', value)

class FontSize(Prop):
    '''
    - number: (es. 18)
    '''
    def __init__(self, value):
        super().__init__('fontSize', value)

class LineHeight(Prop):
    '''
    - number: (es. 56)
    '''
    def __init__(self, value):
        super().__init__('lineHeight', value)

#endregion