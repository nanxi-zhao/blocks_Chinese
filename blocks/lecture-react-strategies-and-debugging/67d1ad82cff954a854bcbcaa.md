---
id: 67d1ad82cff954a854bcbcaa
title: What Is Prop Drilling?
challengeType: 19
dashedName: what-is-prop-drilling
---

# --description--

Prop drilling 是 React 应用中最基础的一种状态传递方式，乍看简单，但很容易变得混乱且难以扩展——别担心，我会一步步带你理解并提供更好的做法。

下面我们来看什么是 prop drilling、为什么它会成为问题，以及当应用变大时可以用来替代它的更好方案。

所谓 prop drilling，就是将 props 从父组件一层层传到深层子组件，即使中间的某些子组件并不真正需要这些 props，也必须把它们向下传递。

举个例子，假设你有 `Parent`、`Child` 和 `Grandchild` 三个组件。如果你想在 `Grandchild` 中使用某些数据，而这些数据保存在 `Parent` 中，那么你就需要把数据先从 `Parent` 传给 `Child`，再从 `Child` 传给 `Grandchild`。

如果数据来源更靠上层，可能还要把它一路传到 `Parent`，然后再向下传。

下面示例中，我们要显示的文本是 `Hello, Prop Drilling!`，它被赋值给根组件 `App` 中的 `greeting` 变量：

```jsx
import "./App.css";
import Parent from "./Parent";

function App() {
  const greeting = "Hello, Prop Drilling!";

  return <Parent greeting={greeting} />;
}

export default App;
```

你会看到 `Parent` 组件也通过 `greeting` prop 接收该变量，并把它作为 `Child` 的 `greeting` prop 继续传递：

```jsx
import Child from "./Child";

const Parent = ({ greeting }) => {
  return <Child greeting={greeting} />;
};

export default Parent;
```

接着 `Child` 再把它传给 `Grandchild`：

```jsx
import Grandchild from "./Grandchild";

const Child = ({ greeting }) => {
  return <Grandchild greeting={greeting} />;
};

export default Child;
```

最后 `Grandchild` 接收到 `greeting`，并把它作为 `h1` 的内容显示出来：

```jsx
const Grandchild = ({ greeting }) => {
  return <h1>{greeting}</h1>;
};

export default Grandchild;
```

在浏览器中，你会看到页面上只有一个 `h1`，其文本为 `Hello, Prop Drilling!`。

起初，prop drilling 看起来并不是什么大问题，但随着应用规模变大，代码会越来越难以理解、调试与维护。

如果确实需要频繁传递 props，尽量把它们集中到单一的父组件里管理。把所有必要数据集中在一个地方被称为“单一真实来源（single source of truth）”。

例如，现在你想给 `greeting` 配套一个新的 `response`，并在 `Grandchild` 中同时使用它们。既然 `greeting` 在 `App`，把 `response` 也放在 `App` 并一并传下去是合理的：

```jsx
function App() {
  const greeting = "Hello, Prop Drilling!";
  const response = "I'm not here to play!";

  return <Parent greeting={greeting} response={response} />;
}

const Parent = ({ greeting, response }) => {
  return <Child greeting={greeting} response={response} />;
};

const Child = ({ greeting, response }) => {
  return <Grandchild greeting={greeting} response={response} />;
};

const Grandchild = ({ greeting, response }) => {
  return (
    <>
      <h1>{greeting}</h1>
      <h2>{response}</h2>
    </>
  );
};

export default App;
```

这样在浏览器中会显示一个 `h1`（`Hello, Prop Drilling!`）和一个 `h2`（`I'm not here to play!`）。

为了避免在大型复杂应用中出现 prop drilling，建议考虑使用 Context API 或状态管理库，例如 Redux / Redux Toolkit、Zustand、Recoil 等，它们可以让状态共享更清晰、更易维护。

后面的课程会深入讲解这些内容，跟着学你会越来越顺手，继续加油！

# --questions--

## --text--

How would a prop flow from a parent to a grandchild component?

## --answers--

By defining the prop inside the grandchild component.

### --feedback--

The prop must go through the child before reaching the grandchild.

---

By passing it from parent to child, then from child to grandchild.

---

By using the `useEffect` hook to fetch the prop dynamically.

### --feedback--

The prop must go through the child before reaching grandchild.

---

By using the `useState` hook in the grandchild.

### --feedback--

The prop must go through the child before reaching grandchild.

## --video-solution--

2

## --text--

What is prop drilling in React?

## --answers--

Passing props directly to only the components that need them.

### --feedback--

It happens when props are passed through multiple levels unnecessarily.

---

Using context to share state between components.

### --feedback--

It happens when props are passed through multiple levels unnecessarily.

---

Passing props from a parent to deeply nested child components.

---

Drilling down into component state using hooks.

### --feedback--

It happens when props are passed through multiple levels unnecessarily.

## --video-solution--

3

## --text--

Why is prop drilling considered a problem in larger applications?

## --answers--

It makes it easier to manage state.

### --feedback--

Too many props passing through multiple components can make the code messy.

---

It improves performance by reducing re-renders.

### --feedback--

Too many props passing through multiple components can make the code messy.

---

It makes the code harder to read, debug, and maintain.

---

It eliminates the need for state management libraries.

### --feedback--

Too many props passing through multiple components can make the code messy.

## --video-solution--

3
