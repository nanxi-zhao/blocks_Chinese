---
id: 67e2a513dbffdc8dcf1700af
title: 什么是useOptimistic钩子，它是如何工作的？
challengeType: 19
dashedName: what-is-the-useoptimistic-hook-and-how-does-it-work
---

# --description--

React的最新版本引入了服务器组件和服务器操作，将一些渲染和逻辑责任转移到服务器上。

随着这些更新，React添加了一个名为`useOptimistic`的新钩子，以在等待异步操作在后台完成时保持UI的响应性。

虽然这通常用于从服务器获取数据，但不仅限于此。该钩子通常用于处理异步操作，确保在操作运行时UI保持流畅和交互性。

让我们来看看`useOptimistic`钩子是什么，以及它如何有助于创建快速响应的UI。

`useOptimistic`钩子帮助管理UI中的"乐观更新"，这是一种策略，即你基于操作的预期结果立即更新UI，比如等待服务器响应。

这是`useOptimistic`钩子的基本语法：

```js
const [optimisticState, addOptimistic] = useOptimistic(actualState, updateFunction);
```

- `optimisticState`是临时状态，会立即更新以获得更好的用户体验。

- `addOptimistic`是在实际状态改变之前应用乐观更新的函数。

- `actualState`是来自操作结果的真实状态值，比如从服务器获取数据。

- `updateFunction`是确定调用时乐观状态应如何更新的函数。

乍一看，`useOptimistic`钩子似乎只是React中处理加载状态的另一种方式。但它不仅如此。

加载状态控制你在后台发生某些事情时在UI中看到微调器、消息或其他指示器。

然而，`useOptimistic`钩子基于预期结果即时更新UI，甚至在你调用API之前。这个钩子让你有机会显示加载指示器或消息，优雅地处理潜在错误，并显示即时反馈，使UI感觉快速响应。

当我们通过一些示例展示`useOptimistic`钩子如何工作时，这将变得更加清晰。

这是一个模拟将任务保存到服务器的操作。它在1秒延迟后返回任务，就像在现实世界的API请求中可能发生的那样：

```js
export async function saveTask(task) {
  await new Promise((res) => setTimeout(res, 1000));

  return task;
}
```

这是通过导入和初始化`useOptimistic`钩子来设置代码的部分，以及一个将输入发送到操作的`handleSubmit`函数：

```jsx
"use client";

import { useOptimistic } from "react";

export default function TaskList({ tasks, addTask }) {
  const [optimisticTasks, addOptimisticTask] = useOptimistic(
    tasks,
    (state, newTask) => [...state, { text: newTask, pending: true }]
  );

  async function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);

    addOptimisticTask(formData.get("task"));

    addTask(formData);
    e.target.reset();
  }

  return <>{/* UI */}</>;
}
```

在代码中，`useOptimistic`钩子维护一个临时任务列表，当你添加新任务时会立即更新。

`(state, newTask) => [...state, { text: newTask, pending: true }]`这一行确保在服务器确认表单中的内容之前，新任务会立即显示为待处理状态。

当表单提交时，`handleSubmit`函数提取任务并使用`addOptimisticTask`参数"乐观地"添加它。然后`addTask`作为prop传递，将任务发送到服务器。最后，通过调用`e.target.reset()`重置表单。

这是`TaskList`组件：

```jsx
"use client";
import { useOptimistic, startTransition } from "react";

export default function TaskList({ tasks, addTask }) {
  const [optimisticTasks, addOptimisticTask] = useOptimistic(
    tasks,
    (state, newTask) => [...state, { text: newTask, pending: true }]
  );

  async function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);

    startTransition(() => {
      addOptimisticTask(formData.get("task"));
    });

    addTask(formData);
    e.target.reset();
  }

  return (
    <div className="max-w-md mx-auto p-4">
      <h3 className="text-xl font-medium mb-3">任务</h3>

      <ul className="space-y-2 mb-4">
        {optimisticTasks.map((task, index) => (
          <li key={index} className="p-2 border-b">
            {task.text}
            {task.pending && (
              <small className="ml-2 text-gray-500 text-sm">
                正在添加任务...
              </small>
            )}
          </li>
        ))}
      </ul>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          name="task"
          placeholder="输入一个任务..."
          className="flex-1 p-2 border"
        />
        <button type="submit" className="bg-gray-200 px-3 py-2 cursor-pointer">
          提交
        </button>
      </form>
    </div>
  );
}
```

在这里，我们遍历`optimisticTask`参数来显示任务。当`task.pending`为`true`时，文本`正在添加任务...`会显示在任务旁边，确认任务在服务器确认之前已被乐观地添加。

这是管理表单状态的`Task`组件。它从操作中调用`saveTask`函数来添加任务，并在服务器接收到新任务后将其追加：

```jsx
"use client";

import { useState } from "react";
import TaskList from "./TaskList";
import { saveTask } from "./actions";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);

  async function addTask(formData) {
    const newTaskText = formData.get("task");

    const savedTask = await saveTask(newTaskText);
    setTasks((prev) => [...prev, { text: savedTask, pending: false }]);
  }

  return <TaskList tasks={tasks} addTask={addTask} />;
}
```

这通过显示即时反馈而不是等待响应来确保快速的UI更新。一旦任务被保存，`pending`属性被移除，最终的任务列表相应地更新。

在UI中，有两件不应该发生的事情正在发生。首先，你看不到`正在添加任务...`文本，因为它出现和消失得太快。其次，添加任务后会出现一个错误。

我们需要做两件事来解决这些问题。

首先，我们需要从React导入`startTransition`并用它来包装`addOptimisticTask(formData.get('task'))`这一行：

```js
startTransition(() => {
  addOptimisticTask(formData.get("task"));
});
```

其次，我们需要让`正在添加任务...`文本在消失前可见一段时间。

为此，我们可以用pending状态修改`addTask`函数，并在将任务标记为完成之前模拟几秒钟的延迟。`setTimeout()`非常适合这个：

```js
async function addTask(formData) {
  const newTaskText = formData.get("task");

  // 添加一个带有pending状态的乐观任务
  const tempTask = { id: Date.now(), text: newTaskText, pending: true };
  setTasks((prev) => [...prev, tempTask]);

  // 模拟3秒延迟后再将任务标记为完成
  setTimeout(async () => {
    const savedTask = await saveTask(newTaskText);

    setTasks((prev) =>
      prev.map((task) =>
        task.id === tempTask.id
          ? { ...task, text: savedTask, pending: false }
          : task
      )
    );
  }, 3000);
}
```

一旦你这样做了，一切都会正常工作。

# --questions--

## --text--

`useOptimistic`钩子的目的是什么？

## --answers--

它允许组件在渲染UI之前从服务器获取数据。

### --feedback--

这个钩子确保在异步操作完成之前UI反映预期的变化。

---

它通过在等待异步操作（如服务器响应）时立即更新UI来帮助管理乐观更新。

---

它为React应用程序中的失败API请求启用自动错误处理和回滚。

### --feedback--

这个钩子确保在异步操作完成之前UI反映预期的变化。

---

它通过将状态更新批处理在一起来优化性能。

### --feedback--

这个钩子确保在异步操作完成之前UI反映预期的变化。

## --video-solution--

2

## --text--

`useOptimistic`钩子与加载状态有什么不同？

## --answers--

加载状态在等待响应时显示UI反馈，而`useOptimistic`基于预期结果立即更新UI。

---

加载状态即时修改服务器数据，而`useOptimistic`只更新客户端UI。

### --feedback--

一个在服务器甚至知道请求之前就更新UI。

---

`useOptimistic`钩子用于处理错误，而加载状态只用于显示微调器。

### --feedback--

一个在服务器甚至知道请求之前就更新UI。

---

两者相同，但`useOptimistic`为失败的请求提供自动重试。

### --feedback--

一个在服务器甚至知道请求之前就更新UI。

## --video-solution--

1

## --text--

在下面的`useOptimistic`钩子语法中，`addOptimistic`做什么？

```js
const [optimisticState, addOptimistic] = useOptimistic(actualState, updateFunction);
```

## --answers--

它在实际状态改变之前应用乐观更新，提供更流畅的用户体验。

---

它从服务器获取真实状态并相应地更新UI。

### --feedback--

这个函数在实际状态改变之前更新UI。

---

它在接收到服务器响应后用临时状态替换实际状态。

### --feedback--

这个函数在实际状态改变之前更新UI。

---

它在应用乐观更新到UI之前验证服务器数据。

### --feedback--

这个函数在实际状态改变之前更新UI。

## --video-solution--

1