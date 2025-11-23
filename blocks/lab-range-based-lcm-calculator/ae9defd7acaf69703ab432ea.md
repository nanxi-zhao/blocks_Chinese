---
id: ae9defd7acaf69703ab432ea
title: 实现一个基于范围的最小公倍数计算器
challengeType: 26
dashedName: implement-a-range-based-lcm-calculator
---

# --description--

在这个实验中，你将创建一个函数，该函数接收一个包含两个数字的数组，并返回这两个数字及其之间所有数字的最小公倍数(LCM)。

**目标**：完成以下用户需求并让所有测试通过以完成实验。

**用户需求**

1. 你应该有一个 [smallestCommons](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 函数，该函数接受一个包含两个数字的数组作为参数。
1. [smallestCommons](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 函数应该返回能被这两个数字以及它们之间所有连续数字整除的最小公倍数。
1. 该函数应该能够处理两个数字不是按数值顺序排列的输入。

# --hints--

你应该有一个 [smallestCommons](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 函数。

```js
assert.isFunction(smallestCommons);
```

[smallestCommons([1, 5])](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 应该返回一个数字。

```js
assert.isNumber(smallestCommons([1, 5]));
```

[smallestCommons([1, 5])](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 应该返回 [60](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/.pnpm/moment@2.30.1/node_modules/moment/src/lib/duration/constructor.js#L6-L6)。

```js
assert.strictEqual(smallestCommons([1, 5]), 60);
```

[smallestCommons([5, 1])](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 应该返回 [60](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/.pnpm/moment@2.30.1/node_modules/moment/src/lib/duration/constructor.js#L6-L6)。

```js
assert.strictEqual(smallestCommons([5, 1]), 60);
```

[smallestCommons([2, 10])](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 应该返回 [2520](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/.pnpm/@types+node@18.19.31/node_modules/@types/node/ts4.8/test/node_tests/cpu_prof_interval.js#L4-L4)。

```js
assert.strictEqual(smallestCommons([2, 10]), 2520);
```

[smallestCommons([1, 13])](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 应该返回 [360360](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93)。

```js
assert.strictEqual(smallestCommons([1, 13]), 360360);
```

[smallestCommons([23, 18])](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93) 应该返回 [6056820](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/blocks_english/lab-range-based-lcm-calculator/ae9defd7acaf69703ab432ea.md#L75-L93)。

```js
assert.strictEqual(smallestCommons([23, 18]), 6056820);
```

# --seed--

## --seed-contents--

```js

```

# --solutions--

```js
function smallestCommons(arr) {
  let [min, max] = arr.sort((a, b) => a - b);

  function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
  }

  function lcm(a, b) {
    return (a * b) / gcd(a, b);
  }

  let multiple = min;

  for (let i = min + 1; i <= max; i++) {
    multiple = lcm(multiple, i);
  }

  return multiple;
}
```
