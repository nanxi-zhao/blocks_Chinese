---
id: 672bbe9171a5cca90f2edeea
title: 元素用户操作伪类的示例有哪些？
challengeType: 19
dashedName: what-are-examples-of-element-user-action-pseudo-classes
---

# --interactive--

用户反馈是网页设计的关键要素。例如，当用户与网站上的元素交互时（如悬停在按钮上或点击链接），接收视觉提示非常重要。这种反馈帮助用户了解交互元素的状态，比如指示链接是否已被访问。

CSS中的用户操作伪类是特殊的关键字，允许您在不需要JavaScript或其他编程语言的情况下提供这种反馈。

这些伪类包括[:hover]、[:active]、[:focus]和[:visited]等。它们使您能够根据用户交互更改元素的外观，从而改善整体用户体验。

让我们深入了解我们拥有的用户操作伪类，看看它们是如何工作的。

[:active]伪类在用户激活元素时应用样式。例如，当用户点击按钮或链接时，它会提供即时的视觉反馈，向用户显示他们的操作已被识别。

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<a href="#">示例链接</a>
```

```css
a:active {
  color: crimson;
}
```

:::

[:hover]伪类在用户将鼠标或其他指向设备悬停在元素上时触发。开发人员经常使用它为按钮、链接或任何应该响应用户注意力的元素创建视觉反馈。这是一个用户在点击前会悬停的按钮示例：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<button class="btn">悬停在我上面</button>
```

```css
.btn:hover {
  background-color: darkgreen;
  color: white;
  cursor: pointer;
}
```

:::

[:focus]伪类在元素获得焦点时应用样式，通常是通过键盘导航或用户点击表单输入。这不仅仅是为了反馈，对可访问性也至关重要。它确保重度依赖键盘的用户可以轻松识别他们正在交互的元素。

这是一个输入字段在被点击或通过键盘导航到时获得焦点的示例：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<form>
  <input type="text" />
</form>
```

```css
input:focus {
  outline: 2px solid darkgreen;
  border-radius: 4px;
}
```

:::

[:visited]伪类针对用户已访问的链接。这有助于用户区分已访问的页面和尚未访问的页面。这是一个将锚文本颜色更改为青色的示例，当链接被访问时：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<a href="https://www.example.com" target="_blank">访问Example.com</a>
```

```css
a:visited {
  color: cyan;
}
```

:::

CSS中的[:checked]伪类允许您为选中（勾选）的表单元素（如复选框和单选按钮）设置样式。这个伪类对于自定义这些元素的外观以增强用户体验很有用，尽管浏览器为它们提供了默认样式。

这是一个带有复选框的示例，用于同意网站条款。

**注意**：此示例中的一些CSS使用了尚未涉及的属性。这只是为了让您了解如何创建自定义复选框。您将在未来的课程和研讨会中学习所有这些内容的工作原理。

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<form>
  <label>
  同意 <input class="checkbox" type="checkbox" />
  </label>
</form>
```

```css
.checkbox {
  appearance: none;
  width: 18px;
  height: 18px;
  border: 2px solid #ccc;
  border-radius: 4px;
  display: inline-block;
  position: relative;
  cursor: pointer;
  transition: all 0.25s ease;
  vertical-align: middle; 
}

.checkbox:hover {
  border-color: #888;
}

.checkbox:checked {
  background-color: #4caf50;
  border-color: #4caf50;
}

.checkbox:checked::after {
  content: "";
  position: absolute;
  left: 4px;
  top: 0px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.checkbox:focus {
  outline: 2px solid #90caf9;
  outline-offset: 2px;
}
```

:::

在这个示例中，我们使用[appearance]属性设置为[none]来移除浏览器应用于复选框输入的默认样式。当用户勾选框时，它将具有绿色背景。

其他操作伪类的示例包括：

- [:focus-within]：当元素或其任何后代获得焦点时应用样式。
- [:enabled]：针对当前启用的表单按钮或其他元素。
- [:disabled]：针对禁用的表单按钮或其他元素。
- [:target]：应用样式到作为URL片段目标的元素（URL中[#]符号后面的部分）。

# --questions--

## --text--

用户操作伪类允许您做什么？

## --answers--

它们启用动画和过渡。

### --feedback--

考虑如何仅使用CSS与用户交互。

---

它们允许您动态修改DOM结构。

### --feedback--

考虑如何仅使用CSS与用户交互。

---

它们让您在不依赖JavaScript的情况下向用户提供反馈。

---

它们让您为列表中的最后一个元素设置样式。

### --feedback--

考虑如何仅使用CSS与用户交互。

## --video-solution--

3

## --text--

CSS中的[:checked]伪类有什么作用？

## --answers--

当元素被禁用时选择该元素。

### --feedback--

考虑表单如何处理用户选择。

---

当元素被悬停时选择该元素。

### --feedback--

考虑表单如何处理用户选择。

---

为选中的复选框或单选按钮等元素设置样式。

---

当元素获得焦点时为元素设置样式。

### --feedback--

考虑表单如何处理用户选择。

## --video-solution--

3

## --text--

[:focus]伪类有什么作用？

## --answers--

当鼠标悬停在元素上时选择该元素。

### --feedback--

考虑用户如何使用键盘导航表单。

---

当元素通过键盘导航或点击获得焦点时应用样式。

---

当表单提交后选择该元素。

### --feedback--

考虑用户如何使用键盘导航表单。

---

当元素被禁用时为其应用样式。

### --feedback--

考虑用户如何使用键盘导航表单。

## --video-solution--

2