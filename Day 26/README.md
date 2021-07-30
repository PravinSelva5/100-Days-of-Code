# List Comprehension

```python
new_list = [new_item for item in list]```

```python
numbers = [1, 2, 3]
new_list = []
for n in list:
    add_1 = n + 1

new_list.append(add_1)
```

The above code can be replaced with list comprehension as follows:

```python
numbers = [1,2,3]
new_list = [ n+1 for n in numbers]
```