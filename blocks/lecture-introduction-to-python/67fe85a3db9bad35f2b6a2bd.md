---
id: 67fe85a3db9bad35f2b6a2bd
title: How Do Conditional Statements and Logical Operators Work?
challengeType: 19
dashedName: how-do-conditional-statements-and-logical-operators-work
---

# --description--

条件语句（conditionals）允许你根据某些条件为真或为假来控制程序的执行流程。

在深入之前，我们先来看组成条件语句的基本要素：比较运算符（comparison operators）。比较运算符用于比较两个或多个值，并返回布尔值（True 或 False）。

在之前的课程中，你已经了解到布尔值是 Python 的一种数据类型，只能为 `True` 或 `False`。

下面是 Python 中常用的比较运算符：

| 运算符 | 名称              | 含义                                                             |
| ------ | ----------------- | ---------------------------------------------------------------- |
| `==`   | 等于              | 检查两个值是否相等                                               |
| `!=`   | 不等于            | 检查两个值是否不相等                                             |
| `>`    | 大于              | 检查左侧值是否大于右侧值                                         |
| `<`    | 小于              | 检查左侧值是否小于右侧值                                         |
| `>=`   | 大于等于          | 检查左侧值是否大于或等于右侧值                                   |
| `<=`   | 小于等于          | 检查左侧值是否小于或等于右侧值                                   |

下面是一些会被求值为 `True` 或 `False` 的示例：

```python
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
```

这些运算符可以用于条件语句中，根据条件的真值来决定是否执行某段代码。

在 Python 中，最基本的条件语句是 `if` 语句，基本语法如下：

```python
if condition:
    # condition 为 True 时执行的代码块
```

* `if` 语句以关键字 `if` 开始。

* `condition` 是一个求值为 `True` 或 `False` 的表达式，后面跟冒号（`:`）。

* 缩进用于标识 `if` 语句体中的代码块。

例子：

```python
age = 18

if age >= 18:
    print('You are an adult') # You are an adult
```

当 `age` 小于 18 时，终端不会打印任何内容：

```python
age = 12

if age >= 18:
    print('You are an adult') # 终端无输出
```

如果你希望在条件为假时也执行某些代码，可以使用 `else` 子句。`else` 在 `if` 条件为 False 时执行。`if…else` 的语法如下：

```python
if condition:
   # condition 为 True 时执行
else:
   # condition 为 False 时执行
```

例如：

```python
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet
```

当需要处理多个条件时，可以使用 `elif`（else if）：

```python
if condition:
   # condition 为 True 时执行
elif condition2:
   # condition2 为 True 时执行
else:
   # 所有条件均为 False 时执行
```

示例：

```python
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
```

注意可以有任意多个 `elif`：

```python
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant
```

现在你已经理解了比较运算符和条件语句的工作方式，就可以开始编写能根据逻辑和输入做出决策的程序了。比较与分支语句是构建灵活且响应式代码的基础。

# --questions--

## --text--

What do comparison operators do?

## --answers--

Perform mathematical calculations with boolean values

### --feedback--

These operators check things like equality or which value is greater, and the result is either `True` or `False`.

---

Convert strings to boolean values.

### --feedback--

These operators check things like equality or which value is greater, and the result is either `True` or `False`.

---

Compare two values and return a boolean value.

---

Create loops and iterations.

### --feedback--

These operators check things like equality or which value is greater, and the result is either `True` or `False`.

## --video-solution--

3

## --text--

What will be the result for the following code?

```python
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') 
```

## --answers--

`You are an adult` will be printed to the console.

### --feedback--

Review the last part of the lesson for the correct answer.

---

`You are a teenager` will be printed to the console.

### --feedback--

Review the last part of the lesson for the correct answer.

---

`You are a child` will be printed to the console.

---

An error will be printed to the console.

### --feedback--

Review the last part of the lesson for the correct answer.

## --video-solution--

3

## --text--

What will the expression `3 >= 4` evaluate to?

## --answers--

`True`

### --feedback--

3 is not greater than or equal to 4.

---

`SyntaxError`

### --feedback--

3 is not greater than or equal to 4.

---

`None`

### --feedback--

3 is not greater than or equal to 4.

---

`False`

## --video-solution--

4
