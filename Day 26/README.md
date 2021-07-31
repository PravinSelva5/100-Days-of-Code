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

```python
name = "Travis"
letters_list = [letter for letter in name]
```

# Dictionary Comprehension

```python

new_dict = {new_key: new_value for item in list}

import random

names = ["Alex", "Beth", "Caroline", "Dave", 'Eleanor', 'Freddie']

student_scores = {student:random.randint(1,100) for student in names}

passed_scores = {student:score  for (student,score) in student_scores.items() if score >= 60}

```
