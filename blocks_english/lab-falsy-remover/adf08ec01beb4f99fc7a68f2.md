---
id: adf08ec01beb4f99fc7a68f2
title: 实现假值移除器
challengeType: 26
dashedName: implement-a-falsy-remover
---

# --description--

在这个实验中，你将创建一个从数组中移除所有假值的函数。

JavaScript中的假值有 `false`、`null`、`0`、`""`、`undefined` 和 `NaN`。

**目标**：实现以下用户需求并通过所有测试以完成实验。

**用户需求：**

1. 你应该有一个 `bouncer` 函数，它接受一个数组作为参数。
1. `bouncer` 函数应该返回一个新数组，该数组包含与作为参数传入的数组相同的元素，但移除了假值元素。
1. `bouncer` 函数不应该改变作为参数传入的数组。

提示：尝试将每个值转换为布尔值。

# --hints--

你应该有一个 `bouncer` 函数。

```js
assert.isFunction(bouncer);
```

`bouncer([7, "ate", "", false, 9])` 应该返回 `[7, "ate", 9]`。

```js
assert.deepEqual(bouncer([7, 'ate', '', false, 9]), [7, 'ate', 9]);
```

`bouncer(["a", "b", "c"])` 应该返回 `["a", "b", "c"]`。

```js
assert.deepEqual(bouncer(['a', 'b', 'c']), ['a', 'b', 'c']);
```

`bouncer([false, null, 0, NaN, undefined, ""])` 应该返回 `[]`。

```js
assert.deepEqual(bouncer([false, null, 0, NaN, undefined, '']), []);
```

`bouncer([null, NaN, 1, 2, undefined])` 应该返回 `[1, 2]`。

```js
assert.deepEqual(bouncer([null, NaN, 1, 2, undefined]), [1, 2]);
```

`bouncer` 函数不应该改变作为参数传入的数组。

```js
const arr = ['a', false, 0, 'Naomi'];
bouncer(arr);
assert.deepEqual(arr, ['a', false, 0, 'Naomi']);
```

`bouncer([])` 应该返回 `[]`。

```js  
assert.deepEqual(bouncer([]), []);  
```

# --seed--

## --seed-contents--

```js

```

# --solutions--

```js
function bouncer(arr) {
  return arr.filter(e => e);
}
```