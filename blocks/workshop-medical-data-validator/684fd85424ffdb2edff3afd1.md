---
id: 684fd85424ffdb2edff3afd1
title: 步骤 26
challengeType: 20
dashedName: step-26
---

# --description--

现在你可能会在终端看到 `{'patient_id': None}`，这是因为小写的 `p` 无法匹配 `P1001`，而 `and` 运算符会返回表达式中第一个为假（falsy）的值。

我们希望患者 ID 以字母 `p` 开头，但大小写都应被接受。为此可以使用正则表达式的 flags 参数来改变匹配行为。例如，`re.search` 接受第三个参数用于指定 flags：

```py
import re

greeting = "Hello there!"
print(re.search('hello', greeting)) # None

print(re.search('hello', greeting, re.IGNORECASE))
# <re.Match object; span=(0, 5), match='Hello'>
```

请在 `re.search` 调用中添加 `re.IGNORECASE` 作为第三个参数，这样正则匹配将不区分大小写。

添加后，你将看到 `None` 被匹配对象替换为 `<re.Match object; span=(0, 1), match='P'>`，其中 `match` 表示匹配到的内容，`span` 标示其在字符串中的位置。

# --hints--

在 `re.search` 调用中添加 `re.IGNORECASE` 作为第三个参数即可。

```js
({ test: () => assert(runPython(`
_var = _Node(_code).find_function("find_invalid_records").find_variable("constraints")
_first = "constraints = {'patient_id': isinstance(patient_id, str) and re.search('p', patient_id, flags=re.IGNORECASE)}"
_second = "constraints = {'patient_id': isinstance(patient_id, str) and re.search('p', patient_id, re.IGNORECASE)}"
_var.is_equivalent(_first) or _var.is_equivalent(_second)
`)) })
```

# --seed--

## --seed-contents--

```py
import re


medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):

--fcc-editable-region--
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.search('p', patient_id)
    }
--fcc-editable-region--

    return constraints

def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True

    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)
print(find_invalid_records(**medical_records[0]))
```
