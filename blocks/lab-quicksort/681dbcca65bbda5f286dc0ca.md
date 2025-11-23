---
id: 681dbcca65bbda5f286dc0ca
title: 实现快速排序算法
challengeType: 27
dashedName: implement-the-quicksort-algorithm
---

# --description--

**目标：** 实现以下用户需求并通过所有测试以完成实验。

**用户需求：**

1. 您应该定义一个名为 `quick_sort` 的函数来实现快速排序算法。

2. `quick_sort` 函数应该接受一个整数列表作为输入，并返回一个按从小到大排序的整数新列表。

3. 要实现该算法，您应该：
   - 从输入列表的元素中选择一个基准值（使用列表的第一个或最后一个元素）。
   - 将输入列表分区为三个子列表：一个小于基准值的元素列表，一个等于基准值的元素列表，一个大于基准值的元素列表。
   - 递归调用 `quick_sort` 来排序子列表，并连接排序后的子列表以生成最终的排序列表。

# --hints--

您应该有一个名为 `quick_sort` 的函数。

```js
({ test: () => runPython(`assert _Node(_code).has_function("quick_sort")`) })
```

您的 `quick_sort` 函数应该接受一个参数。

```js
({ test: () => runPython(`
from inspect import signature
sig = signature(quick_sort)
assert len(sig.parameters) == 1
`) })
```

`quick_sort([])` 应该返回一个空列表。

```js
({ test: () => runPython(`assert quick_sort([]) == []`) })
```

您的 `quick_sort` 函数不应该修改作为参数传递给它的列表。

```js
({ test: () => runPython(`
_test_list = [20, 3, 14, 1, 5]
quick_sort(_test_list)
assert _test_list == [20, 3, 14, 1, 5]
`) })
```

`quick_sort([20, 3, 14, 1, 5])` 应该返回 `[1, 3, 5, 14, 20]`。

```js
({ test: () => runPython(`assert quick_sort([20, 3, 14, 1, 5]) == [1, 3, 5, 14, 20]`) })
```

`quick_sort([83, 4, 24, 2])` 应该返回 `[2, 4, 24, 83]`。

```js
({ test: () => runPython(`assert quick_sort([83, 4, 24, 2]) == [2, 4, 24, 83]`) })
```

`quick_sort([4, 42, 16, 23, 15, 8])` 应该返回 `[4, 8, 15, 16, 23, 42]`。

```js
({ test: () => runPython(`assert quick_sort([4, 42, 16, 23, 15, 8]) == [4, 8, 15, 16, 23, 42]`) })
```

`quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])` 应该返回 `[11, 11, 18, 18, 23, 23, 56, 56, 87, 87]`。

```js
({ test: () => runPython(`assert quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]) == [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]`) })
```

您不应该在代码中使用内置的 `sorted()` 函数。

```js
({ test: () => runPython(`
assert not _Node(_code).block_has_call("sorted")
`) })
```

您不应该在代码中使用 `sort()` 方法。

```js
({ test: () => runPython(`
assert not _Node(_code).block_has_call("sort")
`) })
```

# --seed--

## --seed-contents--

```py

```

# --solutions--

```py
def quick_sort(numbers):
    if not numbers:
        return []
    pivot = numbers[0]
    lesser = []
    equal = []
    greater = []
    for number in numbers:
        if number < pivot:
            lesser.append(number)
        elif number > pivot:
            greater.append(number)
        else:
            equal.append(number)
    return quick_sort(lesser) + equal + quick_sort(greater)
```