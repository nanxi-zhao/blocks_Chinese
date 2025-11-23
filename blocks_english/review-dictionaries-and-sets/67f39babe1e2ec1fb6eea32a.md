---
id: 67f39babe1e2ec1fb6eea32a
title: 字典和集合复习
challengeType: 31
dashedName: review-dictionaries-and-sets
---

# --description--

## 字典

- **字典**：字典是存储键值对集合的内置数据结构。键需要是不可变的数据类型。这是 Python 字典的一般语法：

```python
dictionary = {
    key1: value1,
    key2: value2
}
```

- **`dict()` 构造函数**：`dict()` 构造函数是构建字典的替代方法。你将一个元组列表作为参数传递给 `dict()` 构造函数。这些元组包含键作为第一个元素和值作为第二个元素。

```python
pizza = dict([('name', '玛格丽特披萨'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['马苏里拉奶酪', '罗勒'])])
```

- **方括号表示法**：要访问键值对的值，你可以使用称为方括号表示法的语法。

```python
dictionary[key]
```

## 常见字典方法

- **`get()` 方法**：`get()` 方法检索与键关联的值。它类似于方括号表示法，但它让你设置默认值，防止键不存在时出错。

```python
dictionary.get(key, default)
```

- **`keys()` 和 `values()` 方法**：`keys()` 和 `values()` 方法返回包含字典中所有键和值的视图对象。视图对象是一种查看字典内容而无需创建数据单独副本的方法。

```python
pizza = {
    'name': '玛格丽特披萨',
    'price': 8.9,
    'calories_per_slice': 250
}

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['玛格丽特披萨', 8.9, 250])
```

- **`items()` 方法**：`items()` 方法返回包含字典中所有键值对的视图对象，包括键和值。

```python
pizza.items()
# dict_items([('name', '玛格丽特披萨'), ('price', 8.9), ('calories_per_slice', 250)])
```

- **`clear()` 方法**：`clear()` 方法从字典中删除所有键值对。

```python
pizza.clear()
```

- **`pop()` 方法**：`pop()` 方法删除以第一个参数指定的键的键值对并返回其值。如果键不存在，它返回指定为第二个参数的默认值。如果键不存在且未指定默认值，则引发 `KeyError`。

```python
pizza.pop('price', 10)
pizza.pop('total_price') # KeyError
```

- **`popitem()` 方法**：在 Python 3.7 及更高版本中，`popitem()` 方法删除最后插入的项目。

```python
pizza.popitem()
```

- **`update()` 方法**：`update()` 方法用另一个字典的键值对更新键值对。如果它们有共同的键，则它们的值被覆盖。新键将作为新的键值对添加到字典中。

```python
pizza.update({ 'price': 15, 'total_time': 25 })
```

## 遍历字典

- **遍历值**：如果你需要遍历字典中的值，你可以编写一个带有 `values()` 的 `for` 循环来获取字典的所有值。

```python
products = {
    '笔记本电脑': 990,
    '智能手机': 600,
    '平板电脑': 250,
    '耳机': 70,
}

for price in products.values():
    print(price)
```

输出：

```md
990
600
250
70
```

- **遍历键**：如果你需要遍历 `products` 字典中的键，你可以编写 `products.keys()` 或直接编写 `products`。

```python
for product in products.keys():
    print(product)

for product in products:
    print(product)
```

输出：

```md
笔记本电脑
智能手机
平板电脑
耳机
```

- **遍历键值对**：如果你需要同时遍历键及其对应的值，你可以遍历 `products.items()`。你得到包含键及其对应值的单独元组。

```python
for product in products.items():
    print(product)
```

输出：

```md
('笔记本电脑', 990)
('智能手机', 600)
('平板电脑', 250)
('耳机', 70)
```

要将键和值存储在单独的循环变量中，你需要用逗号分隔它们。第一个变量存储键，第二个存储值。

```python
for product, price in products.items():
    print(product, price)
```

输出：

```md
笔记本电脑 990
智能手机 600
平板电脑 250
耳机 70
```

- **`enumerate()` 函数**：如果你需要在遍历字典时跟踪计数器，你可以调用 `enumerate()` 函数。该函数返回一个 `enumerate` 对象，它为每个项目分配一个整数，就像计数器一样。你可以从任何数字开始计数器，但默认情况下，它从 0 开始。

将索引和项目分配给单独的循环变量是使用 `enumerate()` 的常见方式。例如，使用 `products.items()`，你可以获得整个键值对以及索引：

```python
for index, product in enumerate(products.items()):
    print(index, product)
```

输出：

```md
0 ('笔记本电脑', 990)
1 ('智能手机', 600)
2 ('平板电脑', 250)
3 ('耳机', 70)
```

要自定义计数的初始值，你可以向 `enumerate()` 传递第二个参数。例如，这里我们从 1 开始计数。

```python
for index, product in enumerate(products.items(), 1):
    print(index, product)
```

输出：

```md
1 ('笔记本电脑', 990)
2 ('智能手机', 600)
3 ('平板电脑', 250)
4 ('耳机', 70)
```

## 集合

- **集合**：集合是 Python 中的内置数据结构，不允许重复值。集合是可变且无序的，这意味着它们的元素不按任何特定顺序存储，因此你无法使用索引或键访问它们。此外，集合只能包含不可变数据类型的值，如数字、字符串和元组。

- **定义集合**：要定义集合，你需要将其元素写在花括号内并用逗号分隔。

```python
my_set = {1, 2, 3, 4, 5}
```

- **定义空集合**：如果你需要定义空集合，你必须使用 `set()` 函数。只写空花括号将自动创建字典。

```python
set() # 集合
{}    # 字典
```

## 常见集合方法

- **`add()` 方法**：你可以使用 `add()` 方法向集合添加元素，将新元素作为参数传递。

```python
my_set.add(6)
```

- **`remove()` 和 `discard()` 方法**：要从集合中删除元素，你可以使用 `remove()` 方法或 `discard()` 方法，将要删除的元素作为参数传递。如果未找到元素，`remove()` 方法将引发 `KeyError`，而 `discard()` 方法不会。

```python
my_set.remove(4)
my_set.discard(4)
```

- **`clear()` 方法**：`clear()` 方法从集合中删除所有元素。

```python
my_set.clear()
```

## 数学集合运算

- **`issubset()` 和 `issuperset()` 方法**：`issubset()` 和 `issuperset()` 方法检查一个集合是否是另一个集合的子集或超集。

```python
my_set = {1, 2, 3, 4, 5} 
your_set = {2, 3, 4, 5}

print(your_set.issubset(my_set)) # True
print(my_set.issuperset(your_set)) # True
```

- **`isdisjoint()` 方法**：`isdisjoint()` 方法检查两个集合是否不相交，即它们没有共同的元素。

```python
print(my_set.isdisjoint(your_set)) # False
```

- **并集运算符 (`|`)**：并集运算符 `|` 返回包含两个集合中所有元素的新集合。

```python
my_set | your_set # {1, 2, 3, 4, 5, 6}
```

- **交集运算符 (`&`)**：交集运算符 `&` 返回仅包含集合共同元素的新集合。

```python
my_set & your_set # {2, 3, 4}
```

- **差集运算符 (`-`)**：差集运算符 `-` 返回包含第一个集合中不在其他集合中的元素的新集合。

```python
my_set - your_set # {1, 5}
```

- **对称差集运算符 (`^`)**：对称差集运算符 `^` 返回包含在第一个或第二个集合中但不在两个集合中的元素的新集合。

```python
my_set ^ your_set # {1, 5, 6}
```

- **`in` 运算符**：你可以使用 `in` 运算符检查元素是否在集合中。

```python
print(5 in my_set)
```

## Python 标准库

- **Python 标准库**：库为你提供预编写和可重用的代码，如函数、类和数据结构，你可以在项目中重用它们。Python 拥有广泛的内置模块标准库，为许多问题和任务实现标准化解决方案。一些流行的内置模块示例是 `math`、`random`、`re`（"正则表达式"的缩写）和 `datetime`。

## 导入语句

- **导入语句**：要访问内置模块中定义的元素，你使用导入语句。导入语句通常写在文件的顶部。导入语句对函数、类、常量、变量和模块中定义的任何其他元素都有效。

- **基本导入语句**：你可以使用 `import` 关键字后跟模块名称：

```python
import module_name
```

然后，如果你需要调用该模块中的方法，你将使用点表示法，模块名称后跟方法名称。

```python
module_name.method_name()
```

例如，你将在代码中编写以下内容来导入 `math` 模块并获取 36 的平方根：

```python
import math

math.sqrt(36)
```

- **使用不同名称导入模块**：如果你需要使用不同名称（也称为"别名"）导入模块，你可以在导入语句末尾使用 `as` 后跟别名。这通常用于长模块名称或避免命名冲突。

```python
import module_name as module_alias
```

例如，要在代码中将 `math` 模块称为 `m`，你可以这样分配别名：

```python
import math as m
```

然后，你可以使用别名访问模块的元素：

```python
m.sqrt(36)
```

- **导入特定元素**：如果你不需要模块中的所有内容，你可以使用 `from` 导入特定元素。在这种情况下，导入语句以 `from` 开始，后跟模块名称，然后是 `import` 关键字，最后是你想要导入的元素名称。

```python
from module_name import name1, name2
```

然后，你可以在 Python 脚本中使用这些名称而无需模块前缀。例如：

```python
from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978
```

这很有帮助，但它可能导致命名冲突，如果你已经有同名的函数或变量。在选择要使用的导入语句类型时请记住这一点。

如果你需要为这些名称分配别名，你也可以这样做，使用 `as` 关键字后跟别名。

```python
from module_name import name1 as alias1, name2 as alias2
```

- **带星号 (`*`) 的导入语句**：星号告诉 Python 你想要导入该模块中的所有内容，但你想要导入它，这样你就不需要使用模块名称作为前缀。

```python
from module_name import *
```

例如，如果你这样导入 `math` 模块，你将能够调用该模块中定义的任何函数而无需指定模块名称作为前缀。

```python
from math import *
print(sqrt(36))  # 6.0
```

然而，这通常不被推荐，因为它可能导致命名空间冲突并使你难以知道名称来自哪里。

## `if __name__ == '__main__'`

- **`__name__` 变量**：`__name__` 是 Python 中的特殊内置变量。当 Python 文件直接执行时，Python 将此变量的值设置为字符串 `"__main__"`。但如果 Python 文件作为模块导入到另一个 Python 脚本中，则 `__name__` 变量的值设置为该模块的名称。

这就是为什么你经常在 Python 脚本中找到这个条件。它包含你只想在 Python 脚本作为主程序运行时才运行的代码。

```python
if __name__ == '__main__': 
    # 代码
```

# --assignment--

复习字典和集合主题和概念。