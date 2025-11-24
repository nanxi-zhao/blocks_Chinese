---
id: 67d2f4ddb4a4306fdf5bbaee
title: 什么是记忆化，useMemo钩子是如何工作的？
challengeType: 19
dashedName: what-is-memoization-and-how-does-the-usememo-hook-work
---

# --description--

随着你的React应用程序变得越来越大，不必要的重新渲染和昂贵的计算会减慢性能，导致UI更新缓慢和资源使用增加。

这在具有复杂状态管理、大型列表、需要大量计算的函数以及许多具有单个父组件的应用程序中尤其成问题。

这产生了优化React应用程序以获得更好性能的需求，通过最小化冗余计算并确保更流畅的交互。

React通过一种称为记忆化的过程解决了这个问题，这是一种缓存值和函数以防止不必要重新计算的技术，因此你的应用程序可以更快、响应更灵敏。

根据定义，记忆化是一种优化技术，其中基于特定参数缓存（记住）昂贵函数调用的结果。当再次提供相同参数时，返回缓存的结果而不是重新计算函数。

记忆化过程是这样进行的：

- 存储函数调用的结果及其输入参数。

- 在执行函数之前，检查当前参数的结果是否已存在于缓存中。

- 如果存在，则返回缓存的结果而不是再次运行计算。

- 如果不存在，则计算结果，将其存储在缓存中，然后返回它。

为了改善开发者使用记忆化的体验，React提供了三种工具——`React.memo`（或`memo`）、`useMemo`和`useCallback`。

正如你可能猜到的，`useMemo`和`useCallback`都是钩子，但`React.memo`是一个组件包装器，一个高阶组件（HOC）。

在下一课中，我们将看看`useCallback`钩子和`React.memo`是如何工作的。

`useMemo`让你记忆化计算值，而`useCallback`对函数引用做同样的事情。

如果你想知道什么是计算值和函数引用，计算值指的是执行函数的结果，而函数引用是函数的指针——内存中的函数对象。

让我们先看看如何使用`useMemo`钩子。这是`useMemo`钩子的基本语法：

```js
const memoizedValue = useMemo(
  function () {
    return computeExpensiveValue(a, b);
  },
  [a, b]
);
```

你可以看到所需要做的就是将`useMemo`钩子包装在函数周围。

这个`ExpensiveSquare`组件将接收一个`num` prop，它将用来计算平方：

```jsx
function ExpensiveSquare({ num }) {
  function calculateSquare(n) {
    console.log("计算平方...");
    return n * n;
  }

  const squared = calculateSquare(num);
  return (
    <p>
      {num}的平方: {squared}
    </p>
  );
}
export default ExpensiveSquare;
```

这是使用`ExpensiveSquare`的`App`组件：

```jsx
import { useState, useEffect } from "react";
import ExpensiveSquare from "./components/ExpensiveSquare";

function App() {
 const [timer, setTimer] = useState(0);
 const [num, setNum] = useState(0);

 useEffect(() => {
   const interval = setInterval(() => setTimer((c) => c + 1), 1000);
   return () => clearInterval(interval);
 }, []);

 return (
   <div>
     <h1>计时器: {timer}秒已过</h1>
     <ExpensiveSquare num={num} />
     <button onClick={() => setNum((n) => n + 1)}>增加数字</button>
   </div>
 );
}

export default App;
```

`useEffect`中的`timer`每秒运行一次，会使`calculateSquare`函数每次运行时都执行，即使你没有增加`num`状态变量。

为了解决这个问题，我们可以使用`useMemo`钩子，将函数调用包装在其中，并将`num`变量指定为依赖项：

```jsx
// 导入useMemo钩子
import { useMemo } from "react";

function ExpensiveSquare({ num }) {
  function calculateSquare(n) {
    console.log("计算平方...");
    return n * n;
  }

  // const squared = calculateSquare(num);
  // 改为将函数调用包装在useMemo中
  const squared = useMemo(() => calculateSquare(num), [num]);

  return (
    <p>
      {num}的平方: {squared}
    </p>
  );
}

export default ExpensiveSquare;
```

这将确保通过缓存结果来记忆化函数，因此计算只在`num`变量改变时发生，而不是在使用它的组件中的任何内容改变时发生。

`calculateSquare`函数调用不再在`timer`改变时运行，而是在初始渲染和`num`改变时运行。

# --questions--

## --text--

React中的记忆化是什么？

## --answers--

一种缓存值和函数以防止不必要重新计算的技术。

---

一种让你管理组件状态更新以防止不必要重新计算的技术。

### --feedback--

它通过存储先前计算的结果来帮助优化性能。

---

一种协调虚拟DOM与实际DOM的过程。

### --feedback--

它通过存储先前计算的结果来帮助优化性能。

---

一种处理函数组件中副作用的方法。

### --feedback--

它通过存储先前计算的结果来帮助优化性能。

## --video-solution--

1

## --text--

计算值和函数引用之间有什么区别？

## --answers--

计算值是函数对象，而函数引用是执行结果。

### --feedback--

一个是函数的输出，另一个只是指向它的指针。

---

计算值是执行函数的结果，而函数引用是内存中的函数对象。

---

计算值和函数引用是同一回事。

### --feedback--

一个是函数的输出，另一个只是指向它的指针。

---

函数引用存储计算值。

### --feedback--

一个是函数的输出，另一个只是指向它的指针。

## --video-solution--

2

## --text--

以下哪项不是React为记忆化提供的工具？

## --answers--

`React.memo`

### --feedback--

记忆化工具专注于缓存值和函数，而这个选项处理副作用。

---

`useMemo`

### --feedback--

记忆化工具专注于缓存值和函数，而这个选项处理副作用。

---

`useCallback`

### --feedback--

记忆化工具专注于缓存值和函数，而这个选项处理副作用。

---

`useEffect`

### --feedback--

记忆化工具专注于缓存值和函数，而这个选项处理副作用。

## --video-solution--

4