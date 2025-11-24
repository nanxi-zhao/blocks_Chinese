---
id: 6732b28eeadda1158cdbff7b
title: 如何检查数组是否包含某个特定值？
challengeType: 19
dashedName: how-can-you-check-if-an-array-contains-a-certain-value
---

# --interactive--

在JavaScript中，[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法是检查数组是否包含特定值的简单而高效的方法。这个方法返回一个布尔值：如果数组包含指定元素则返回[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)，否则返回[false](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)。

当您需要快速验证数组中是否存在某个元素而不需要知道其确切位置时，[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法特别有用。让我们从一个如何使用[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法的示例开始：

:::interactive_editor

```js
let fruits = ["apple", "banana", "orange", "mango"];
console.log(fruits.includes("banana")); // true
console.log(fruits.includes("grape"));  // false
```

:::

在这个示例中，我们有一个水果数组。我们使用[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法检查[banana](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)是否在数组中。它返回[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)，因为[banana](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)确实存在。然后我们检查[grape](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)，它返回[false](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)，因为它不在数组中。

处理字符串时，[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法是区分大小写的。这意味着首字母大写的[Banana](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L33-L33)和全小写的[banana](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L32-L32)被认为是不同的值。以下示例说明了这一点：

:::interactive_editor

```js
let fruits = ["apple", "banana", "orange"];
console.log(fruits.includes("banana")); // true
console.log(fruits.includes("Banana")); // false
```

:::

在这种情况下，全小写的[banana](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L32-L32)在数组中找到了，但首字母大写的[Banana](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L33-L33)没有找到，所以第二个[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)调用返回[false](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)。

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法还可以接受一个可选的第二个参数，指定在数组中开始搜索的位置。如果您想检查数组特定部分中元素的存在，这很有用。以下是使用此功能的方法：

:::interactive_editor

```js
let numbers = [10, 20, 30, 40, 50, 30, 60];
console.log(numbers.includes(30, 3)); // true
console.log(numbers.includes(30, 4)); // true
```

:::

对于第一个[console.log](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L46-L46)，我们从索引[3](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L46-L46)开始查找数字[30](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L45-L45)。在这种情况下，索引[3](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L46-L46)之后确实有一个数字[30](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L45-L45)，所以[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法返回[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)。

第二个[console.log](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L47-L47)也是如此。我们从索引[4](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L47-L47)开始查找数字[30](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L45-L45)。由于数字[30](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L45-L45)确实出现在该索引之后，所以它将返回[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)。

值得注意的是，[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)使用严格相等比较（[===](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L56-L56)），这意味着它可以区分不同类型。例如：

:::interactive_editor

```js
let mixedArray = [1, "2", 3, "4", 5];
console.log(mixedArray.includes(2));  // false
console.log(mixedArray.includes("2")); // true
```

:::

在这种情况下，数字[2](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L62-L62)和字符串["2"](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L63-L63)被认为是不同的数据类型。所以，第一个[console.log](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L62-L62)将返回[false](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)，而第二个[console.log](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L63-L63)将返回[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)。

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法是检查数组中元素存在的强大工具。它使用简单、高效，可以节省您编写更复杂的循环或条件来搜索数组的时间。无论您处理的是字符串、数字还是混合数据类型，[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)都提供了一种直接的方法来验证值是否存在于您的数组中。

# --questions--

## --text--

下面代码的输出是什么？

```js
let arr = [1, 2, 3, 4, 5];
console.log(arr.includes(3, 3));
```

## --answers--

[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)

### --feedback--

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)的第二个参数指定搜索的起始位置。

---

[false](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)

---

[undefined](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L97-L97)

### --feedback--

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)的第二个参数指定搜索的起始位置。

---

会报错。

### --feedback--

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)的第二个参数指定搜索的起始位置。

## --video-solution--

2

## --text--

下面代码的输出是什么？

```js
let arr = ["a", "b", "c", "d", "e"];
console.log(arr.includes("C"));
```

## --answers--

[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)

### --feedback--

记住处理字符串时[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)是区分大小写的。

---

[false](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)

---

[undefined](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L138-L138)

### --feedback--

记住处理字符串时[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)是区分大小写的。

---

会报错。

### --feedback--

记住处理字符串时[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)是区分大小写的。

## --video-solution--

2

## --text--

下面代码的输出是什么？

```js
let arr = [1, "2", 3, "4", 5];
console.log(arr.includes("3"));
```

## --answers--

[true](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)

### --feedback--

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法使用严格相等（[===](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L56-L56)）进行比较。

---

[false](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L19-L19)

---

[undefined](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L179-L179)

### --feedback--

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法使用严格相等（[===](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L56-L56)）进行比较。

---

会报错。

### --feedback--

[includes()](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L18-L18)方法使用严格相等（[===](file:///F:/Code/blocks_Chinese/blocks_english/lecture-working-with-common-array-methods/6732b28eeadda1158cdbff7b.md#L56-L56)）进行比较。

## --video-solution--

2