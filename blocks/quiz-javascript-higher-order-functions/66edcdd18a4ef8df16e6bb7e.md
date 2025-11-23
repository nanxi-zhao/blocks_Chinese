---
id: 66edcdd18a4ef8df16e6bb7e
title: JavaScript高阶函数测验
challengeType: 8
dashedName: quiz-javascript-higher-order-functions
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

关于JavaScript高阶函数，以下哪个陈述是不正确的？

#### --distractors--

高阶函数可以通过启用函数式编程技术大大提高代码的可读性和可维护性。

---

像map、filter和reduce这样的高阶函数是数组操作的强大工具，但它们不是函数式编程独有的。

---

高阶函数可能会增加理解代码的复杂性，但它们也可以带来更富有表现力和简洁的解决方案。

#### --answer--

JavaScript中的所有函数，包括那些不接受或不返回其他函数的函数，都可以被归类为高阶函数。

### --question--

#### --text--

在高阶函数的上下文中，工厂函数是什么？

#### --distractors--

创建新变量的函数。

---

只处理字符串的函数。

---

自动生成代码注释的函数。

#### --answer--

根据特定参数返回新函数的函数

### --question--

#### --text--

代码执行后，`forEachRes`和`mapRes`的值是什么？

```js
const numbers = [1, 1, 1, 1, 1];
let sum = 0;
const forEachRes = numbers.forEach(num => {
  return (sum += num);
});
const mapRes = numbers.map(num => {
  return (sum += num);
});
```

#### --distractors--

`forEachRes`是`undefined`，`mapRes`是`[1,2,3,4,5]`

---

`forEachRes`是`0`，`mapRes`是`[1,2,3,4,5]`

---

`forEachRes`是`5`，`mapRes`是`[1,2,3,4,5]`

#### --answer--

`forEachRes`是`undefined`，`mapRes`是`[6,7,8,9,10]`

### --question--

#### --text--

这段代码的结果是什么？

```js
[, undefined, 'a', 'b', { 20: 5 }].sort();
```

#### --distractors--

数组排序的不支持元素，因此出错。

---

未提供回调函数，因此出错。

---

```js
[empty, 'a', 'b', undefined, { '20': 5 }]
```

#### --answer--

```js
[{ '20': 5 }, 'a', 'b', undefined, empty]
```

### --question--

#### --text--

以下哪项描述了JavaScript中的回调函数？

#### --distractors--

在声明时立即调用的函数。

---

在特定上下文中调用的函数。

---

返回另一个函数的函数。

#### --answer--

作为参数传递给另一个函数的函数，由该函数的逻辑执行。

### --question--

#### --text--

在数组上使用`reduce()`的结果是什么？

#### --distractors--

指示是否有任何元素满足条件的布尔值。

---

包含所有元素按指定回调函数减少的数组。

---

布尔值数组。

#### --answer--

它根据累加器的初始值和回调函数而变化。

### --question--

#### --text--

如果在数值排序中没有提供比较函数，`sort()`方法会如何表现？

#### --distractors--

它用`null`填充空槽。

---

它返回一个特殊字符数组。

---

它按相反顺序对数组进行排序。

#### --answer--

它基于UTF-16代码单元将数组作为字符串排序。

### --question--

#### --text--

JavaScript中`some()`方法的用途是什么？

#### --distractors--

创建一个包含对每个元素应用函数结果的新数组。

---

遍历数组而不产生结果。

---

基于回调函数将数组减少到单个值。

#### --answer--

确定数组中是否有任何元素通过指定测试。

### --question--

#### --text--

以下哪项是方法链式的有效示例？

#### --distractors--

```js
Math.random();
```

---

```js
array.push(1).pop();
```

---

```js
console.log('Hello');
```

#### --answer--

```js
str.toLowerCase().trim().replace(' ', '_');
```

### --question--

#### --text--

以下代码的输出是什么？

```js
let numbers = [2, 4, 8, 10];

numbers.forEach(function(number) {
    console.log(number % 2);
});
```

#### --distractors--

`2 4 8 10`

---

`null null null null`

---

`1 2 4 5`

#### --answer--

`0 0 0 0`

### --question--

#### --text--

以下哪项是方法链式的好处？

#### --distractors--

通过减少函数执行时间来优化性能。

---

消除对临时变量的需求，但在某些情况下可能会增加内存使用。

---

允许错误处理和调试更加直接。

#### --answer--

通过允许在单个表达式中进行多个操作来促进简化语法和更易读的代码。

### --question--

#### --text--

如何使用`sort`方法按特定属性对对象数组进行排序？

#### --distractors--

`sort`方法无法对对象进行排序。

---

在排序后使用`reverse`方法。

---

将对象转换为字符串并对其进行排序。

#### --answer--

使用比较函数来比较属性值。

### --question--

#### --text--

在方法链式中，什么是增强清晰度和调试的常见做法？

#### --distractors--

在链中使用更少的方法。

---

避免链式返回原始值的方法。

---

只使用内置方法。

#### --answer--

将长链分解为多个步骤。

### --question--

#### --text--

在代码中过度使用方法链式的潜在缺点是什么？

#### --distractors--

它使代码运行得更慢。

---

它阻止使用注释。

---

它使文件大小更大。

#### --answer--

它可能使代码更难调试。

### --question--

#### --text--

使用哪个方法来确定数组中的所有元素都是字符串？

#### --distractors--

`some()`

---

`everyInstance()`

---

`filter()`

#### --answer--

`every()`

### --question--

#### --text--

以下代码运行后`originalArray`的值是什么？

```js
const originalArray = [{ id: 1 }, { id: 2 }, { id: 3 }];
const filteredArray = originalArray.filter(item => item.id > 1);
filteredArray[0].id = 4;
```

#### --distractors--

`[{ id: 1 }, { id: 2 }, { id: 3 }]`

---

`[{ id: 1 }]`

---

`[{ id: 4 }, { id: 2 }, { id: 3 }]`

#### --answer--

`[{ id: 1 }, { id: 4 }, { id: 3 }]`

### --question--

#### --text--

以下代码运行后`shortWords`的值是什么？

```js
const words = ['apple', 'banana', 'pear', 'kiwi'];
const shortWords = words.filter(word => word.length <= 5);
```

#### --distractors--

`[]`

---

`['pear', 'kiwi']`

---

`['apple', 'banana']`

#### --answer--

`['apple', 'pear', 'kiwi']`

### --question--

#### --text--

向`reduce()`方法提供初始值作为参数的目的是什么？

#### --distractors--

设置数组的长度。

---

限制迭代次数。

---

指定函数的返回类型。

#### --answer--

定义累加器的起始值。

### --question--

#### --text--

`map`方法可以用于不是数组的对象吗？

#### --distractors--

是的，它可以用于任何对象。

---

是的，但只能用于具有数值属性的对象。

---

这取决于JavaScript版本。

#### --answer--

不，它是专门为数组设计的。

### --question--

#### --text--

JavaScript中`map`方法的主要用途是什么？

#### --distractors--

对数组进行排序并返回一个新数组，同时保持原始顺序。

---

从数组中过滤元素并根据条件删除或添加元素。

---

在数组中查找特定元素并返回其索引和元素。

#### --answer--

创建一个新数组，其中包含对起始数组中每个元素调用提供的函数的结果。