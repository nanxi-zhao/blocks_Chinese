---
id: af2170cad53daa0770fabdea
title: Implement the Mutations Algorithm
challengeType: 26
dashedName: implement-the-mutations-algorithm
---

# --description--

**目标：**实现以下用户需求并通过所有测试以完成实验。

**用户需求：**

1. 创建一个名为[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)的函数，该函数接收一个数组作为参数。
2. 如果数组第一个元素中的字符串包含数组第二个元素中字符串的所有字母，则[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)，否则返回[false](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。例如：
   - [mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["hello", "Hello"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)，因为第二个字符串中的所有字母都出现在第一个字符串中，忽略大小写。
   - [mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["hello", "hey"])应返回[false](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)，因为字符串[hello](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-reverse-a-string/66b8957bad1d0a11a980f0dc.md#L35-L53)不包含[y](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-element-skipper/66c072ad3475cd92421b9ac6.md#L39-L57)。
   - [mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["Alien", "line"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)，因为[line](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-line-chart/66db569d34c7089b9b41bfd7.md#L45-L63)中的所有字母都出现在[Alien](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L18-L18)中。

# --hints--

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["hello", "hey"])应返回[false](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isFalse(mutation(['hello', 'hey']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["hello", "Hello"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isTrue(mutation(['hello', 'Hello']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["zyxwvutsrqponmlkjihgfedcba", "qrstu"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isTrue(mutation(['zyxwvutsrqponmlkjihgfedcba', 'qrstu']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["Mary", "Army"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isTrue(mutation(['Mary', 'Army']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["Mary", "Aarmy"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isTrue(mutation(['Mary', 'Aarmy']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["Alien", "line"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isTrue(mutation(['Alien', 'line']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["floor", "for"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isTrue(mutation(['floor', 'for']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["hello", "neo"])应返回[false](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isFalse(mutation(['hello', 'neo']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["voodoo", "no"])应返回[false](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isFalse(mutation(['voodoo', 'no']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["ate", "date"])应返回[false](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isFalse(mutation(['ate', 'date']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["Tiger", "Zebra"])应返回[false](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isFalse(mutation(['Tiger', 'Zebra']));
```

[mutation](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-mutations/af2170cad53daa0770fabdea.md#L103-L115)(["Noel", "Ole"])应返回[true](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-boolean-check/66b8957bad1d0a11a980f0d6.md#L35-L53)。

```js
assert.isTrue(mutation(['Noel', 'Ole']));
```

# --seed--

## --seed-contents--
```js
```

# --solutions--

```js
function mutation(arr) {
  let hash = Object.create(null);

  arr[0]
    .toLowerCase()
    .split('')
    .forEach(c => (hash[c] = true));

  return !arr[1]
    .toLowerCase()
    .split('')
    .filter(c => !hash[c]).length;
}

mutation(['hello', 'hey']);
```
