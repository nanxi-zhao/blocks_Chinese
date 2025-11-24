---
id: 66cc1ccfefdd727e18c2ab20
title: 步骤 14
challengeType: 1
dashedName: step-14
---

# --description--

你的[calculateQuotient]似乎工作正常，但还有一个情况你还没有测试过。

添加一个[console.log]，用参数[3]和[0]调用[calculateQuotient]函数。

确保仔细查看这次调用的输出。

# --hints--

你应该有一个[console.log]，用参数[3]和[0]调用[calculateQuotient]函数。

```js
assert.match(code, /console\.log\s*\(\s*calculateQuotient\s*\(\s*3\s*,\s*0\s*\)\s*\)\s*;?/);
```

# --seed--

## --seed-contents--

```js
function calculateSum(num1, num2) {
  return num1 + num2;
}

console.log(calculateSum(2, 5));
console.log(calculateSum(10, 10));
console.log(calculateSum(5, 5));

function calculateDifference(num1, num2) {
  return num1 - num2;
}

console.log(calculateDifference(22, 5));
console.log(calculateDifference(12, 1));
console.log(calculateDifference(17, 9));

function calculateProduct(num1, num2) {
  return num1 * num2;
}

console.log(calculateProduct(13, 5));

function calculateQuotient(num1, num2) {
  return num1 / num2;
}

console.log(calculateQuotient(7, 11));

--fcc-editable-region--

--fcc-editable-region--
```