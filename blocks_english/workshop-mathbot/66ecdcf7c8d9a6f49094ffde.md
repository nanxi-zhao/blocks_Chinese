---
id: 66ecdcf7c8d9a6f49094ffde
title: 步骤 11
challengeType: 1
dashedName: step-11
---

# --description--

在之前的课程中，你已经学会了 `Math.round()` 方法会将数值四舍五入到最接近的整数。

这里有一些例子：

```js
Math.round(6.7); // 7
Math.round(3.2); // 3
```

这与 `Math.floor()` 和 `Math.ceil()` 方法不同，它们分别向下和向上舍入到最接近的整数。

创建一个名为 `numRounded` 的新变量，并将数字 `2.7` 四舍五入后的结果赋值给它。然后，将 `numRounded` 的值输出到控制台。

在下方再创建另一个名为 `numRounded2` 的新变量，并将数字 `11.2` 四舍五入后的结果赋值给它。然后，将 `numRounded2` 的值输出到控制台。

# --hints--

你应该有一个名为 `numRounded` 的变量。

```js
assert.isNotNull(numRounded);
```

你应该将数字 `2.7` 四舍五入后的结果赋值给变量 `numRounded`。

```js
assert.equal(numRounded, 3);
```

你不应该将 `3` 这个值直接写入 `numRounded` 变量中。请确保你使用的是 `Math.round()` 方法。

```js
assert.notMatch(code, /numRounded\s*=\s*3/);
```

你应该将 `numRounded` 的值输出到控制台。

```js
assert.match(code, /console\.log\(\s*numRounded\s*\)/);
```

你应该有一个名为 `numRounded2` 的变量。

```js
assert.isNotNull(numRounded2);
```

你应该将数字 `11.2` 四舍五入后的结果赋值给变量 `numRounded2`。

```js
assert.equal(numRounded2, 11);
```

你不应该将 `11` 这个值直接写入 `numRounded2` 变量中。请确保你使用的是 `Math.round()` 方法。

```js
assert.notMatch(code, /numRounded2\s*=\s*11/);
```

你应该将 `numRounded2` 的值输出到控制台。

```js
assert.match(code, /console\.log\(\s*numRounded2\s*\)/);
```

# --seed--

## --seed-contents--

```js
const botName = "MathBot";
const greeting = `你好呀！我的名字是 ${botName}，我将会教会你有关 Math 对象的知识！`;

console.log(greeting);

console.log("Math.random() 方法会返回一个在 0 到小于 1 范围内的伪随机数。");

const randomNum = Math.random();
console.log(randomNum);

console.log("现在，让我们在两个数值之间生成一个随机数。");

const min = 1;
const max = 100;

const randomNum2 = Math.random() * (max - min) + min;
console.log(randomNum2);

console.log("Math.floor() 方法会将数值向下舍入到最接近的整数。");

const numRoundedDown = Math.floor(6.7);
console.log(numRoundedDown);

console.log("Math.ceil() 方法会将数值向上舍入到最接近的整数。");

const numRoundedUp = Math.ceil(3.2);
console.log(numRoundedUp);

console.log("Math.round() 方法会将数值四舍五入到最接近的整数。");

--fcc-editable-region--

--fcc-editable-region--
```