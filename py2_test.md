

```python
from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        
    def getRadius(self):
        # return self.radius
        return round(self.radius, 2) # 仅返回两位有效数字
    
    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError("Wrong type.")
        self.radius = float(value)
        
    def getArea(self):
        return self.radius ** 2 * pi

    R = property(fget=getRadius, fset=setRadius)
```


```python
#  直接访问属性的可能问题　
c = Circle(3.2)
c.radius = 'abc'
d = c.radius * 2
print(d)
```

    abcabc



```python
c.setRadius('abc')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-6cdc3013a779> in <module>()
    ----> 1 c.setRadius('abc')
    

    <ipython-input-1-e9c40e6b4329> in setRadius(self, value)
          9 
         10     def setRadius(self, value):
    ---> 11         if not isinstance(value, (int, long, float)):
         12             raise ValueError("Wrong type.")
         13         self.radius = float(value)


    NameError: name 'long' is not defined



```python
c = Circle(3.2)
print(c.R)
```

    3.2



```python
c.R = 'abc' # 实际上是调用set方法，所以进行了判断
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-fbb599f5e286> in <module>()
    ----> 1 c.R = 'abc'
    

    <ipython-input-5-4d445df8be90> in setRadius(self, value)
         10 
         11     def setRadius(self, value):
    ---> 12         if not isinstance(value, (int, long, float)):
         13             raise ValueError("Wrong type.")
         14         self.radius = float(value)


    NameError: name 'long' is not defined



```python

```
