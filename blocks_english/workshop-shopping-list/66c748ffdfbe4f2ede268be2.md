---
id: 66c748ffdfbe4f2ede268be2
title: 步骤 20
challengeType: 1
dashedName: step-20
---

# --description--

在工作坊的最后一步中，将最终的购物清单记录到控制台。

为此，在 `console.log` 中调用 `getShoppingListMsg` 函数，并将 `shoppingList` 数组作为参数传递。

完成这最后一步后，你的购物清单就完成了！

# --hints--

你应该在 `console.log` 中调用 `getShoppingListMsg(shoppingList)`。

```js
assert.lengthOf(code.match(/console\.log\(\s*getShoppingListMsg\(\s*shoppingList\s*\)\s*\)/g), 7);
```

# --seed--

## --seed-contents--

```js
console.log("杂货购物清单");

const shoppingList = [];

console.log("吃点水果会很不错。");

shoppingList.push("Apples");

function getShoppingListMsg(arr) {
  return `当前购物清单: ${arr}`;
}

console.log(getShoppingListMsg(shoppingList));

shoppingList.push("Grapes");
console.log(getShoppingListMsg(shoppingList));

console.log("看起来我们需要买一些食用油。");

shoppingList.unshift("Vegetable Oil");
console.log(getShoppingListMsg(shoppingList));

shoppingList.push("Popcorn", "Beef Jerky", "Potato Chips");
console.log(getShoppingListMsg(shoppingList));

console.log("这看起来像太多的垃圾食品。");

shoppingList.pop();
console.log(getShoppingListMsg(shoppingList));

console.log("吃点甜点会很不错。");

shoppingList.unshift("Chocolate Cake");
console.log(getShoppingListMsg(shoppingList));

console.log("再想想，也许我们应该更注重健康。");

shoppingList.shift();
shoppingList[0] = "Canola Oil";

--fcc-editable-region--

--fcc-editable-region--
```

# --solutions--

```js
console.log("杂货购物清单");

const shoppingList = [];

console.log("吃点水果会很不错。");

shoppingList.push("Apples");

function getShoppingListMsg(arr) {
  return `当前购物清单: ${arr}`;
}

console.log(getShoppingListMsg(shoppingList));

shoppingList.push("Grapes");
console.log(getShoppingListMsg(shoppingList));

console.log("看起来我们需要买一些食用油。");

shoppingList.unshift("Vegetable Oil");
console.log(getShoppingListMsg(shoppingList));

shoppingList.push("Popcorn", "Beef Jerky", "Potato Chips");
console.log(getShoppingListMsg(shoppingList));

console.log("这看起来像太多的垃圾食品。");

shoppingList.pop();
console.log(getShoppingListMsg(shoppingList));

console.log("吃点甜点会很不错。");

shoppingList.unshift("Chocolate Cake");
console.log(getShoppingListMsg(shoppingList));

console.log("再想想，也许我们应该更注重健康。");

shoppingList.shift();
shoppingList[0] = "Canola Oil";

console.log(getShoppingListMsg(shoppingList));
```
