---
id: 66f1adcf97e3e4c1bd89ebf5
title: 网页性能测验
challengeType: 8
dashedName: quiz-web-performance
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

网页开发中实际性能和感知性能的关键区别是什么？

#### --distractors--

实际性能关注浏览器发出的 HTTP 请求数量，而感知性能基于 CSS 渲染速度。

---

实际性能只关注加载时间，而感知性能与动画和加载指示器等视觉元素相关。

---

实际性能只包括服务器端处理时间，而感知性能完全是客户端的。

#### --answer--

实际性能是内容加载的速度，而感知性能是用户认为页面加载的速度。

### --question--

#### --text--

以下哪个指标最能表明网页内容出现的速度？

#### --distractors--

可交互时间 (TTI)

---

页面加载时间 (PLT)

---

最大内容绘制 (LCP)

#### --answer--

首次内容绘制 (FCP)

### --question--

#### --text--

以下哪项不是减少页面加载时间的方法？

#### --distractors--

优化媒体资源。

---

利用浏览器缓存。

---

压缩和缩小文件。

#### --answer--

仅使用 JPEG 文件。

### --question--

#### --text--

什么是"可用时间"？

#### --distractors--

这是从用户请求页面到他们可以与页面上的表单交互的时间间隔。

---

这是所有图像和动画变得可用和可操作所需的时间。

---

这是所有 CSS 和 JavaScript 动画在屏幕上加载所需的时间。

#### --answer--

这是从用户请求页面到他们可以有意义地与之交互的时间间隔。

### --question--

#### --text--

首次内容绘制 (FCP) 测量什么？

#### --distractors--

页面上所有 JavaScript 文件的总体加载时间。

---

用户可以与页面上的任何元素交互之前的延迟。

---

所有样式表完全加载和应用所需的时间。

#### --answer--

第一段文本或图像渲染所需的时间。

### --question--

#### --text--

以下哪项不是常用的性能测量工具？

#### --distractors--

Chrome DevTools

---

Lighthouse

---

WebPageTest

#### --answer--

WebMeasure

### --question--

#### --text--

性能网页 API 用于什么？

#### --distractors--

仅用于测量 CSS 动画的性能。

---

用于自动提高网页的性能。

---

为用户提供详细的性能指标表。

#### --answer--

让开发人员直接从代码中跟踪网页加载和响应的效率。

### --question--

#### --text--

哪种策略可以有效提升感知性能？

#### --distractors--

使用大图像来提高整体视觉质量。

---

最后加载 CSS 样式以优先渲染内容。

---

预加载所有脚本以确保它们在需要时准备就绪。

#### --answer--

在获取内容时显示加载骨架。

### --question--

#### --text--

以下哪项指的是请求在浏览器和服务器之间传输所需的时间？

#### --distractors--

渲染

---

INP

---

CDN

#### --answer--

延迟

### --question--

#### --text--

优化 CSS 如何影响页面性能？

#### --distractors--

防止浏览器执行不必要的 JavaScript。

---

减少图像的总体文件大小。

---

消除延迟加载图像的需求。

#### --answer--

加快 HTML 的解析。

### --question--

#### --text--

以下哪项显示了主线程被繁重的 JavaScript 任务阻塞的时间？

#### --distractors--

源代码顺序

---

跳出率

---

WebPageTest

#### --answer--

总阻塞时间

### --question--

#### --text--

在测量交互到下一次绘制 (INP) 时，评估的是什么？

#### --distractors--

用户交互后页面完全加载所有样式和图像所需的时间。

---

用户交互与浏览器能够注册下一次用户输入之间的延迟。

---

JavaScript 执行与浏览器刷新页面内容之间的时间间隔。

#### --answer--

用户交互与浏览器通过渲染下一帧进行响应之间的时间。

### --question--

#### --text--

以下哪个 API 为你提供高精度时间戳（以毫秒为单位），以测量网站不同部分的加载时间？

#### --distractors--

`performance.delay()`

---

`performance.previous()`

---

`performance.next()`

#### --answer--

`performance.now()`

### --question--

#### --text--

以下哪个 API 为你提供从 DNS 查找到 `DOMContentLoaded` 的每个页面加载阶段的详细分解？

#### --distractors--

Permit Timing API

---

Performance Text API

---

Perform Timing API

#### --answer--

Performance Timing API

### --question--

#### --text--

以下哪项监听布局偏移、长任务和用户交互等性能事件？

#### --distractors--

```js
const observer = new PermitObserve((list) => {  
  list.getEntries().forEach((entry) => {  
    console.log(`Long task detected: ${entry.duration}ms`);  
  });  
});  

observer.observe({ type: "longtask", buffered: true });
```

---

```js
const observer = new PerformObserver((list) => {  
  list.getEntries().forEach((entry) => {  
    console.log(`Long task detected: ${entry.duration}ms`);  
  });  
});  

observer.observe({ type: "longtask", buffered: true });
```

---

```js
const observer = new PermitObserver((list) => {  
  list.getEntries().forEach((entry) => {  
    console.log(`Long task detected: ${entry.duration}ms`);  
  });  
});  

observer.observe({ type: "longtask", buffered: true });
```

#### --answer--

```js
const observer = new PerformanceObserver((list) => {  
  list.getEntries().forEach((entry) => {  
    console.log(`Long task detected: ${entry.duration}ms`);  
  });  
});  

observer.observe({ type: "longtask", buffered: true });
```

### --question--

#### --text--

延迟加载图像如何提升页面性能？

#### --distractors--

确保所有图像立即加载以获得更好的用户体验。

---

减少图像文件大小以加快加载速度。

---

预加载图像以防止任何加载延迟。

#### --answer--

延迟加载非必要的图像直到它们出现在视图中。

### --question--

#### --text--

什么是代码分割？

#### --distractors--

将你的 React 代码分割成只执行关键任务的模块

---

将你的 HTML 代码分割成只执行非关键任务的模块。

---

将你的 CSS 代码分割成执行关键和非关键任务的模块。

#### --answer--

将你的 JavaScript 代码分割成执行关键和非关键任务的模块。

### --question--

#### --text--

以下哪项是延迟加载图像的正确方式？

#### --distractors--

```html
<img src="placeholder.jpg" lazy="loading">
```

---

```html
<img src="placeholder.jpg" load="lazy">
```

---

```html
<img src="placeholder.jpg" lazy="load">
```

#### --answer--

```html
<img src="placeholder.jpg" loading="lazy">
```

### --question--

#### --text--

以下哪项不是改善 INP 的方法？

#### --distractors--

通过分解长 JavaScript 任务来减少主线程工作。

---

优化事件处理程序。

---

延迟或延迟加载重型资源。

#### --answer--

仅使用 PNG 和 JPEG 图像。

### --question--

#### --text--

为什么能效是网页性能的关键方面？

#### --distractors--

它增强了网页的整体视觉吸引力。

---

它最小化了网页上使用的 JavaScript 数量。

---

它减少了所需的 CSS 文件数量并使你的 CSS 运行得更快。

#### --answer--

它减少了硬件负载，节约能源并提高可持续性。