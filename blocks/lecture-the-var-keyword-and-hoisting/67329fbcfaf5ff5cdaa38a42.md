---
id: 67329fbcfaf5ff5cdaa38a42
title: 什么是 var 关键字，为什么不再建议使用它？
challengeType: 19
dashedName: what-is-the-var-keyword-and-why-is-it-no-longer-suggested-to-use-it
---

# --interactive--

JavaScript 中的 `var` 关键字是声明变量的原始方式之一。自从语言诞生以来它就是语言的一部分，并且多年来它一直是创建变量的主要方法。然而，随着 JavaScript 的发展和开发者对语言经验的积累，使用 `var` 的某些缺点变得明显，这导致了 2015 年引入了 `let` 和 `const`。

当你用 `var` 声明一个变量时，它会变成函数作用域或全局作用域。这意味着如果你在函数内使用 `var` 声明一个变量，它只能在该函数内访问。但是，如果你在任何函数之外声明它，它就会变成一个全局变量，可以在整个脚本中访问。这种行为有时会导致意外结果，使你的代码更难理解。

`var` 的一个问题是你可以在不抛出错误的情况下多次重新声明同一个变量。这可能导致意外覆盖，使调试更加困难。

:::interactive_editor

```js
var num = 5;
console.log(num); // 5

// 这是允许的，不会抛出错误
var num = 10;
console.log(num); // 10
```

:::

`var` 最重要的问题是它缺乏块作用域。在块内（如 `if` 语句或 `for` 循环）用 `var` 声明的变量在该块之外仍然可以访问。

:::interactive_editor

```js
if (true) {
  var num = 5;
}
console.log(num); // 5
```

:::

这种行为可能导致意外的变量泄漏，使你的代码更容易出现错误。

由于这些问题，现代 JavaScript 开发已经很大程度上从 `var` 转向了 `let` 和 `const`。这些关键字提供了块作用域，这与许多其他编程语言中的作用域工作方式更接近。

它们也不允许在相同作用域内重新声明，有助于防止意外覆盖。

虽然 `var` 仍然是 JavaScript 的一部分，并且在所有浏览器中都能工作，但通常建议在现代 JavaScript 开发中使用 `let` 和 `const`。它们提供了清晰的作用域规则，有助于防止常见陷阱，并使你的代码行为更加可预测。

# --questions--

## --text--

在任何函数之外声明的 `var` 变量的作用域是什么？

## --answers--

块作用域。

### --feedback--

想想在函数之外声明的 `var` 变量可以在哪里被访问。

---

函数作用域。

### --feedback--

想想在函数之外声明的 `var` 变量可以在哪里被访问。

---

全局作用域。

---

模块作用域。

### --feedback--

想想在函数之外声明的 `var` 变量可以在哪里被访问。

## --video-solution--

3

## --text--

下面代码的输出是什么？

```js
var x = 10;

if (true) {
  var x = 20;
  console.log(x);
}

console.log(x);
```

## --answers--

```js
10
10
```

### --feedback--

记住 `var` 是函数作用域或全局作用域，并且它允许在相同作用域内重新声明。

---

```js
20
20
```

---

```js
10
20
```

### --feedback--

记住 `var` 是函数作用域或全局作用域，并且它允许在相同作用域内重新声明。

---

```js
20
10
```

### --feedback--

记住 `var` 是函数作用域或全局作用域，并且它允许在相同作用域内重新声明。

## --video-solution--

2

## --text--

以下哪项不是在现代 JavaScript 中避免使用 `var` 的原因？

## --answers--

`var` 允许在相同作用域内重新声明变量。

### --feedback--

考虑哪个关于 `var` 行为或支持的陈述是错误的。

---

`var` 在现代浏览器中不受支持。

---

`var` 变量是函数作用域，不是块作用域。

### --feedback--

考虑哪个关于 `var` 行为或支持的陈述是错误的。

---

`var` 变量会被提升。

### --feedback--

考虑哪个关于 `var` 行为或支持的陈述是错误的。

## --video-solution--

2