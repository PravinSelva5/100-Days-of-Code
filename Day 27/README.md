# Day 27 Notes

## Advanced Python Arguments

- Default Values
```python 
 def function(a=1, b=2, c=3)

 # to change b value
 def function(b=5)
```
- Unlimited Positional Arguments
```python
    def add(*args):
            for n in args:
                print(n) 
  ```
  - Unlimited Keyword Arguments
    - values are stored as dictionaries
```python
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)


class Car:
    def __int__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GTR")
```