---
id: afd15382cdfb22c9efe8b7de
title: 实现DNA配对生成器
challengeType: 26
dashedName: implement-a-dna-pair-generator
---

# --description--

在DNA的双螺旋结构中，碱基总是成对出现：如果一条链上有<em>A</em>碱基，另一条链正对面就是<em>T</em>碱基，另一对是<em>C</em>和<em>G</em>。

在这个实验中，你将编写一个函数来为提供的DNA链匹配缺失的碱基对。对于提供的字符串中的每个字符，找到配对的碱基字符。

例如，对于输入`ATCG`，返回`[["A", "T"], ["T", "A"], ["C", "G"], ["G", "C"]]`

<em>A</em>碱基与<em>T</em>碱基配对，<em>T</em>碱基与<em>A</em>碱基配对，<em>C</em>与<em>G</em>碱基配对，最后<em>G</em>碱基与<em>C</em>碱基配对。

**目标**：实现以下用户需求并通过所有测试以完成实验。

**用户需求：**

1. 你应该有一个`pairElement`函数，它接受任意长度的字符串作为参数。
1. `pairElement`函数应该返回一个二维数组，其中每个内部数组包含两个字符串，第一个字符串是来自输入的一个碱基，第二个字符串是配对的碱基。
1. 当给定`A`时，函数应该将其与`T`配对。
1. 当给定`T`时，函数应该将其与`A`配对。
1. 当给定`C`时，函数应该将其与`G`配对。
1. 当给定`G`时，函数应该将其与`C`配对。

# --hints--

你应该创建一个名为`pairElement`的函数。

```js
assert.isFunction(pairElement);
```

`pairElement`应该接受一个参数。

```js
assert.lengthOf(pairElement, 1);
```

`pairElement("ATCGA")`应该返回`[["A","T"],["T","A"],["C","G"],["G","C"],["A","T"]]`。

```js
assert.deepEqual(pairElement('ATCGA'), [
  ['A', 'T'],
  ['T', 'A'],
  ['C', 'G'],
  ['G', 'C'],
  ['A', 'T']
]);
```

`pairElement("TTGAG")`应该返回`[["T","A"],["T","A"],["G","C"],["A","T"],["G","C"]]`。

```js
assert.deepEqual(pairElement('TTGAG'), [
  ['T', 'A'],
  ['T', 'A'],
  ['G', 'C'],
  ['A', 'T'],
  ['G', 'C']
]);
```

`pairElement("CTCTA")`应该返回`[["C","G"],["T","A"],["C","G"],["T","A"],["A","T"]]`。

```js
assert.deepEqual(pairElement('CTCTA'), [
  ['C', 'G'],
  ['T', 'A'],
  ['C', 'G'],
  ['T', 'A'],
  ['A', 'T']
]);
```

# --seed--

## --seed-contents--

```js

```

# --solutions--

```js
var lookup = Object.create(null);
lookup.A = 'T';
lookup.T = 'A';
lookup.C = 'G';
lookup.G = 'C';

function pairElement(str) {
 return str.split('').map(function(p) {return [p, lookup[p]];});
}
```