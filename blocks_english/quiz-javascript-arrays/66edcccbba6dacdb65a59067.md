---
id: 66edcccbba6dacdb65a59067
title: JavaScript数组测验
challengeType: 8
dashedName: quiz-javascript-arrays
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

以下代码的输出结果是什么？

```js
const numbers = [1, 2, 3];
console.log(numbers[10]);
```

#### --distractors--

`[1, 2, 3]`

---

`null`

---

`10`

#### --answer--

`undefined`

### --question--

#### --text--

以下哪种方式是正确地从`developers`数组中访问字符串`"Jessica"`？

#### --distractors--

```js
const developers = ["Jessica", "Naomi", "Tom"];
developers[1]
```

---

```js
const developers = ["Jessica", "Naomi", "Tom"];
developers[2]
```

---

```js
const developers = ["Jessica", "Naomi", "Tom"];
developers[-1]
```

#### --answer--

```js
const developers = ["Jessica", "Naomi", "Tom"];
developers[0]
```

### --question--

#### --text--

`index`变量将被赋什么值？

```js
const numbers = [10, 20, 30, 40];
const index = numbers.indexOf(20);
console.log(index);
```

#### --distractors--

2

---

3

---

-1

#### --answer--

1

### --question--

#### --text--

rest语法的作用是什么？

#### --distractors--

用于将字符串分割成子字符串数组。

---

用于在数组的任意位置添加或删除元素。

---

用于在数组末尾添加元素并返回新长度。

#### --answer--

用于将数组的剩余元素捕获到新数组中。

### --question--

#### --text--

什么是数组解构？

#### --distractors--

用于将数组的所有元素连接成单个字符串。

---

用于检查数组是否包含特定值。

---

用于从数组中删除最后一个元素并返回该删除的元素。

#### --answer--

用于从数组中提取值并以更简洁易读的方式将它们分配给变量。

### --question--

#### --text--

`arr2`变量将被赋什么值？

```js
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2);
```

#### --distractors--

`[4, 5, 1, 2, 3]`

---

`[1, 2, [3, 4, 5]]`

---

`[1, 2, 3]`

#### --answer--

`[1, 2, 3, 4, 5]`

### --question--

#### --text--

这段代码会向控制台记录什么？

```js
const colors = ["red", "blue", "green", "yellow"];
colors.splice(1, 2, "purple");
console.log(colors);
```

#### --distractors--

`["red", "blue", "green", "yellow"]`

---

`["red", "blue", "yellow"]`

---

`["red", "yellow"]`

#### --answer--

`["red", "purple", "yellow"]`

### --question--

#### --text--

`slicedArr`变量将被赋什么值？

```js
const arr = ["apple", "banana", "cherry", "date"];
const slicedArr = arr.slice(1, 3);
console.log(slicedArr);
```

#### --distractors--

`["apple", "banana"]`

---

`["cherry", "date"]`

---

`["apple", "cherry"]`

#### --answer--

`["banana", "cherry"]`

### --question--

#### --text--

哪个方法返回数组中给定元素的第一个索引？

#### --distractors--

`firstIndex()`

---

`lastIndex()`

---

`searchIndex()`

#### --answer--

`indexOf()`

### --question--

#### --text--

哪个方法用于从数组中删除第一个元素并返回该删除的元素？

#### --distractors--

`pop()`

---

`slice()`

---

`splice()`

#### --answer--

`shift()`

### --question--

#### --text--

`concat()`方法的作用是什么？

#### --distractors--

将数组元素连接成字符串。

---

在数组开头添加元素。

---

从数组中删除元素。

#### --answer--

将两个数组合并成新数组。

### --question--

#### --text--

这段代码的输出结果是什么？

```js
const fruits = ["apple", "banana", "cherry", "apple", "orange"];

fruits.splice(0, 1);

console.log(fruits);
```

#### --distractors--

`["apple", "banana", "cherry", "apple", "orange"]`

---

`["apple", "banana", "cherry"]`

---

`["cherry", 'apple']`

#### --answer--

`["banana", "cherry", "apple", "orange"]`

### --question--

#### --text--

`includes()`方法的作用是什么？

#### --distractors--

用于将字符串分割成子字符串数组。

---

用于将数组的所有元素连接成单个字符串。

---

用于在数组的任意位置添加或删除元素。

#### --answer--

用于检查数组是否包含特定值。

### --question--

#### --text--

以下哪个方法用于就地反转数组？

#### --distractors--

`reversed()`

---

`reverseArr()`

---

`reversing()`

#### --answer--

`reverse()`

### --question--

#### --text--

什么是二维数组？

#### --distractors--

只包含对象字面量的数组。

---

固定长度的数组。

---

浮点数数组。

#### --answer--

数组的数组。

### --question--

#### --text--

关于数组中的`indexOf()`方法，以下哪一项是正确的？

#### --distractors--

它总是返回元素的最后一次出现。

---

如果找不到元素则抛出错误。

---

要求数组排序。

#### --answer--

如果找不到元素则返回`-1`。

### --question--

#### --text--

以下哪一项不是数组方法？

#### --distractors--

`includes()`

---

`pop()`

---

`push()`

#### --answer--

`trim()`

### --question--

#### --text--

以下代码的输出结果是什么？

```js
const arr = ["o", "l", "l", "e", "h"];
console.log(arr.join(""));
```

#### --distractors--

`["o", "l", "l", "e", "h"]`

---

`"hello"`

---

`undefined`

#### --answer--

`"olleh"`

### --question--

#### --text--

对空数组使用`shift()`方法的结果是什么？

#### --distractors--

`TypeError`

---

`[]`

---

`null`

#### --answer--

`undefined`

### --question--

#### --text--

哪个方法会返回一个不改变原始数组的新数组？

#### --distractors--

`shift()`

---

`pop()`

---

`push()`

#### --answer--

`slice()`