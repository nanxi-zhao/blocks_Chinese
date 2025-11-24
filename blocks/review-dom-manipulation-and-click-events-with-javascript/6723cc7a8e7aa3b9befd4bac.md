---
id: 6723cc7a8e7aa3b9befd4bac
title: 使用 JavaScript 操作 DOM 和点击事件复习
challengeType: 31
dashedName: review-dom-manipulation-and-click-events-with-javascript
---

# --description--

## 使用 DOM 和 Web API

- **API**：API（应用程序编程接口）是一组规则和协议，允许软件应用程序相互通信并高效地交换数据。
- **Web API**：Web API 是专门为 Web 应用程序设计的。这些类型的 API 通常分为两大类：浏览器 API 和第三方 API。
- **浏览器 API**：这些 API 暴露来自浏览器的数据。作为 Web 开发人员，你可以使用 JavaScript 访问和操作这些数据。
- **第三方 API**：这些 API 不是默认内置浏览器的。你必须以某种方式获取它们的代码。通常，它们会有详细的文档解释如何使用它们的服务。例如 Google Maps API，你可以使用它在你的网站上显示交互式地图。
- **DOM**：DOM 代表文档对象模型。它是一个编程接口，让你与 HTML 文档交互。使用 DOM，你可以添加、修改或删除网页上的元素。DOM 树的根是 `html` 元素。它是 HTML 文档所有内容的顶级容器。所有其他节点都是这个根节点的后代。然后，在根节点下方，我们在层次结构中找到其他节点。父节点是包含其他元素的元素。子节点是包含在另一个元素中的元素。
- **`navigator` 接口**：这提供了有关浏览器环境的信息，如用户代理字符串、平台和浏览器版本。用户代理字符串是标识所使用浏览器和操作系统的文本字符串。
- **`window` 接口**：这代表包含 DOM 文档的浏览器窗口。它提供了与浏览器窗口交互的方法和属性，如调整窗口大小、打开新窗口和导航到不同 URL。

## 使用 `querySelector()`、`querySelectorAll()` 和 `getElementById()` 方法

- **`getElementById()` 方法**：此方法用于获取表示具有指定 `id` 的 HTML 元素的对象。请记住，id 在每个 HTML 文档中必须是唯一的，因此此方法只会返回一个 Element 对象。

```html
<div id="container"></div>
```

```js
const container = document.getElementById("container");
```

- **`querySelector()` 方法**：此方法用于获取 HTML 文档中与作为参数传递的 CSS 选择器匹配的第一个元素。

```html
<section class="section"></section>
```

```js
const section = document.querySelector(".section");
```

- **`querySelectorAll()` 方法**：你可以使用此方法获取与特定 CSS 选择器匹配的所有 DOM 元素列表。

```html
<ul class="ingredients">
  <li>糖</li>
  <li>牛奶</li>
  <li>鸡蛋</li>
</ul>
```

```js
const ingredients = document.querySelectorAll('ul.ingredients li');
```

## 使用 `innerText()`、`innerHTML()`、`createElement()` 和 `textContent()` 方法

- **`innerHTML` 属性**：这是 `Element` 的一个属性，用于设置或更新 HTML 标记的部分。

```html
<div id="container">
  <!-- 在这里添加新元素 -->
</div>
```

```js
const container = document.getElementById("container");
container.innerHTML = '<ul><li>奶酪</li><li>番茄</li></ul>';
```

- **`createElement` 方法**：这用于创建 HTML 元素。

```js
const img = document.createElement("img");
```

- **`innerText`**：这表示 HTML 元素及其后代的可见文本内容。

```html
<div id="container">
  <p>你好，世界！</p>
  <p>我正在学习 JavaScript</p>
</div>
```

```js
const container = document.getElementById("container");
console.log(container.innerText);
```

- **`textContent`**：这返回元素的纯文本内容，包括其后代中的所有文本。

```html
<div id="container">
  <p>你好，世界！</p>
  <p>我正在学习 JavaScript</p>
</div>
```

```js
const container = document.getElementById("container");
console.log(container.textContent);
```

## 使用 `appendChild()` 和 `removeChild()` 方法

- **`appendChild()` 方法**：此方法用于将节点添加到指定父节点的子节点列表的末尾。

```html
<ul id="desserts">
  <li>蛋糕</li>
  <li>派</li>
</ul>
```

```js
const dessertsList = document.getElementById("desserts");
const listItem = document.createElement("li");

listItem.textContent = "饼干";
dessertsList.appendChild(listItem);
```

- **`removeChild()` 方法**：此方法用于从 DOM 中删除节点。

```html
<section id="example-section">
  <h2>示例子标题</h2>
  <p>第一段</p>
  <p>第二段</p>
</section>
```

```js
const sectionEl = document.getElementById("example-section");
const lastParagraph = document.querySelector("#example-section p:last-of-type");

sectionEl.removeChild(lastParagraph);
```

## 使用 `setAttribute()` 方法

- **定义**：此方法用于为给定元素设置属性。如果属性已存在，则更新值。否则，添加具有值的新属性。

```html
<p id="para">我是一个段落</p>
```

```js
const para = document.getElementById("para");
para.setAttribute("class", "my-class");
```

## 事件对象

- **定义**：`Event` 对象是在用户以某种方式与你的网页交互时触发的有效载荷。这些交互可以是点击按钮或聚焦输入，甚至是摇动他们的移动设备。所有 `Event` 对象都有 `type` 属性。此属性揭示了触发有效载荷的事件类型，如 keydown 或 click。这些值将对应于你可能传递给 `addEventListener()` 的相同值，你可以在其中捕获和利用 `Event` 对象。

## `addEventListener()` 和 `removeEventListener()` 方法

- **`addEventListener` 方法**：此方法用于监听事件。它接受两个参数：你要监听的事件和事件发生时将被调用的函数。事件的一些常见示例是点击事件、输入事件和更改事件。

```js
const btn = document.getElementById("btn");

btn.addEventListener("click", () => alert("你点击了按钮"));
```

- **`removeEventListener()` 方法**：此方法用于删除先前使用 `addEventListener()` 方法添加到元素的事件监听器。当你想要停止监听元素上的特定事件时，这很有用。

```js
const bodyEl = document.querySelector("body");
const para = document.getElementById("para");
const btn = document.getElementById("btn");

let isBgColorGrey = true;

function toggleBgColor() {
  bodyEl.style.backgroundColor = isBgColorGrey ? "blue" : "grey";
  isBgColorGrey = !isBgColorGrey;
}

btn.addEventListener("click", toggleBgColor);

para.addEventListener("mouseover", () => {
  btn.removeEventListener("click", toggleBgColor);
});
```

- **内联事件处理程序**：内联事件处理程序是 HTML 元素上的特殊属性，用于在事件发生时执行 JavaScript 代码。在现代 JavaScript 中，内联事件处理程序不被认为是最佳实践。更推荐使用 `addEventListener` 方法。

```html
<button onclick="alert('你好世界！')">显示警告</button>
```

## 更改事件

- **定义**：更改事件是一种特殊事件，当用户修改某些输入元素的值时触发。示例包括选中复选框或单选按钮时。或者当用户从日期选择器或下拉菜单中进行选择时。

```html
<label>
  选择一种编程语言：
  <select class="language" name="language">
    <option value="">---选择一个---</option>
    <option value="JavaScript">JavaScript</option>
    <option value="Python">Python</option>
    <option value="C++">C++</option>
  </select>
</label>

<p class="result"></p>
```

```js 
const selectEl = document.querySelector(".language");
const result = document.querySelector(".result");

selectEl.addEventListener("change", (e) => {
  result.textContent = `你喜欢用 ${e.target.value} 编程。`;
});
```

## 事件冒泡

- **定义**：事件冒泡或传播是指事件在触发时"冒泡"到父对象的方式。
- **`stopPropagation()` 方法**：此方法防止事件的进一步传播。

## 事件委托

- **定义**：事件委托是在父级上监听已冒泡的事件的过程，而不是直接在触发它们的元素上处理它们。

## DOMContentLoaded

- **定义**：当 HTML 文档中的所有内容都已加载和解析时，会触发 `DOMContentLoaded` 事件。如果你有外部样式表或图像，`DOMContentLoaded` 事件不会等待它们加载。它只会等待 HTML 加载。

## 使用 `style` 和 `classList`

- **`Element.style` 属性**：这是一个只读属性，表示元素的内联样式。你可以使用此属性获取或设置元素的样式。

```js
const paraEl = document.getElementById("para");
paraEl.style.color = "red";
```

- **`Element.classList` 属性**：这是一个只读属性，可用于在元素上添加、删除或切换类。

```js
// 示例添加类
const paraEl = document.getElementById("para");
paraEl.classList.add("highlight");

// 示例删除类
paraEl.classList.remove("blue-background");

// 示例切换类
const menu = document.getElementById("menu");
const toggleBtn = document.getElementById("toggle-btn");

toggleBtn.addEventListener("click", () => menu.classList.toggle("show"));
```

## 使用 `setTimeout()` 和 `setInterval()` 方法

- **`setTimeout()` 方法**：此方法允许你延迟指定时间的操作。

```js
setTimeout(() => {
 console.log('这在 3 秒后运行'); 
}, 3000);
```

- **`setInterval()` 方法**：此方法以设定的时间间隔重复运行一段代码。由于 `setInterval()` 在指定的时间间隔内持续执行提供的函数，你可能想要停止它。为此，你必须使用 `clearInterval()` 方法。

```js
setInterval(() => {
 console.log('这每 2 秒运行一次');
}, 2000);

// 使用 clearInterval 的示例
const intervalID = setInterval(() => {
 console.log('这将在 5 秒后停止');
}, 1000);

setTimeout(() => {
 clearInterval(intervalID);
}, 5000);
```

## `requestAnimationFrame()` 方法

- **定义**：此方法允许你在下一次屏幕重绘之前安排动画的下一步，从而产生流畅且视觉上吸引人的体验。下一次屏幕重绘是指浏览器刷新网页视觉显示的时刻。这每秒发生多次，通常在大多数显示器上约为 60 次（或每秒 60 帧）。

```js
function animate() {
 // 更新动画...
 // 例如，移动元素，更改样式等。
 update();
 // 请求下一帧
 requestAnimationFrame(animate);
}
```

## Web 动画 API

- **定义**：Web 动画 API 让你能够直接在 JavaScript 中创建和控制动画。

```js
const square = document.querySelector('#square');

const animation = square.animate(
 [{ transform: 'translateX(0px)' }, { transform: 'translateX(100px)' }],
 {
   duration: 2000, // 使动画持续 2 秒
   iterations: Infinity, // 无限循环
   direction: 'alternate', // 来回移动
   easing: 'ease-in-out', // 平滑缓动
 }
);
```

## Canvas API

- **定义**：Canvas API 是一个强大的工具，让你能够在 JavaScript 文件中直接操作图形。要使用 Canvas API，你首先需要在 HTML 中提供一个 `canvas` 元素。这个元素充当绘图表面，你可以使用 Canvas API 中接口的实例方法和属性来操作它。此 API 具有 `HTMLCanvasElement`、`CanvasRenderingContext2D`、`CanvasGradient`、`CanvasPattern` 和 `TextMetrics` 等接口，其中包含可用于在 JavaScript 文件中创建图形的方法和属性。

```html
<canvas id="my-canvas" width="400" height="400"></canvas>
```

```js
const canvas = document.getElementById('my-canvas');

// 访问画布的绘图上下文。
// "2d" 允许你在二维中绘图
const ctx = canvas.getContext('2d');

// 设置背景颜色
ctx.fillStyle = 'crimson';

// 绘制矩形
ctx.fillRect(1, 1, 150, 100);
```

## 使用 JavaScript 打开和关闭对话框和模态框

- **模态框和对话框定义**：对话框让你向用户显示重要信息或操作。使用 HTML 内置的 dialog 元素，你可以轻松地在 Web 应用中创建这些对话框（包括模态和非模态对话框）。模态对话框是一种对话框类型，它强制用户在访问应用程序或网页的其余部分之前与之交互。相比之下，非模态对话框允许用户在对话框打开时继续与页面或应用程序的其他部分交互。它不会阻止访问其余内容。
- **`showModal()` 方法**：此方法用于打开模态框。

```html
<dialog id="my-modal">
   <p>这是一个模态对话框。</p>
</dialog>
<button id="open-modal">打开模态对话框</button>
```

```js
const dialog = document.getElementById('my-modal');
const openButton = document.getElementById('open-modal');

openButton.addEventListener('click', () => {
  dialog.showModal();
});
```

- **`close()` 方法**：此方法用于关闭模态框。

```html
<dialog id="my-modal">
   <p>这是一个模态对话框。</p>
   <button id="close-modal">关闭模态框</button>
</dialog>
<button id="open-modal">打开模态对话框</button>
```

```js
const dialog = document.getElementById('my-modal');
const openButton = document.getElementById('open-modal');
const closeButton = document.getElementById('close-modal');

openButton.addEventListener('click', () => {
  dialog.show();
});

closeButton.addEventListener('click', () => {
  dialog.close();
});
```

# --assignment--

复习使用 JavaScript 操作 DOM 和点击事件的主题和概念。