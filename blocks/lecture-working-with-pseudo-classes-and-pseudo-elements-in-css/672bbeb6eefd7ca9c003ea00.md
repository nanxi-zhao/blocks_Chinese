---
id: 672bbeb6eefd7ca9c003ea00
title: 树结构伪类的示例有哪些？
challengeType: 19
dashedName: what-are-examples-of-tree-structural-pseudo-classes
---

# --interactive--

树结构伪类允许您根据元素在文档树中的位置来定位和设置元素样式。文档树指的是HTML文档中元素的层次结构。

以下是树结构伪类列表：

- [:root]
- [:empty]
- [:nth-child(n)]
- [:nth-last-child(n)]
- [:first-child]
- [:last-child]
- [:only-child]
- [:nth-of-type]
- [:first-of-type]
- [:last-of-type]
- [:only-of-type]

让我们更仔细地看看每个树结构伪类，并附上示例。

​​[:root]伪类通常是根[html]元素。它帮助您定位文档中的最高级别，以便您可以对整个文档应用通用样式。

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<h1>欢迎访问我的网站</h1>
<p>这是一个示例段落，用于演示:root伪类。</p>
```

```css
:root {
  background: black;
  color: aliceblue;
}
```

:::

[:root]伪类也常用于设置CSS变量：

```css
:root {
  --main-font: 'Arial, sans-serif';
  --primary-color: blue; 
  --secondary-color: green; 
}
```

通过CSS变量，您可以存储值并在样式表中重用它们。您将在以后了解更多相关内容。

空元素，即除了空白字符外没有子元素的元素，也包含在文档树中。这就是为什么有[:empty]伪类来定位空元素。例如，此HTML代码有两个空列表项。通过[:empty]伪类，您可以以不同方式为空列表项设置样式：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<ul>
  <li>项目1</li>
  <li></li> <!-- 这个列表是空的 -->
  <li>项目2</li>
  <li></li> <!-- 另一个空列表 -->
  <li>项目3</li>
</ul>
```

```css
:empty {
  background: black;
}
```

:::

对空列表项最实用的做法可能是根本不显示它们：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<ul>
  <li>项目1</li>
  <li></li> <!-- 这个列表是空的 -->
  <li>项目2</li>
  <li></li> <!-- 另一个空列表 -->
  <li>项目3</li>
</ul>
```

```css
:empty {
  display: none;
}
```

:::

[:nth-child(n)]允许您根据元素在父元素中的位置来选择元素，而[:nth-last-child(n)]使您能够通过从末尾开始计数来选择元素。[n]可以是特定数字或[odd]或[even]等关键字。这在基于位置对表格单元格进行样式设置时非常有用：奇数和偶数。

这是一个水果价格列表表格的HTML示例。CSS使用[:nth-child]伪类根据奇数和偶数位置来定位表格单元格：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<table>
  <tr>
    <th>项目</th>
    <th>价格</th>
  </tr>
  <tr>
    <td>苹果</td>
    <td>$1.00</td>
  </tr>
  <tr>
    <td>香蕉</td>
    <td>$0.50</td>
  </tr>
  <tr>
    <td>橙子</td>
    <td>$0.80</td>
  </tr>
</table>
```

```css
th,
td {
  border: 1px solid lightgray;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: orangered;
}

tr:nth-child(odd) {
  background-color: lightgreen;
}
```

:::

[:first-child]、[:last-child]和[:only-child]伪类都作用于父容器或整个文档中的项目。

- [:first-child]选择父元素或文档中的第一个元素。
- [:last-child]选择父元素或文档中的最后一个元素。
- [:only-child]选择父元素或文档中唯一的元素。

使用[:first-child]和[:last-child]伪类将在此示例中选择项目1和项目3：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<ul>
  <li>项目1</li>
  <li>项目2</li>
  <li>项目3</li>
</ul>
```

```css
li:first-child {
  background-color: orangered;
}

li:last-child {
  background-color: lightgreen;
}
```

:::

如果您在页面上有更多无序列表，则必须更具体地进行选择：

为了向您展示[:only-child]伪类的工作原理，这里有一个包含两个独立[div]元素的HTML示例。使用[:only-child]伪类确保只选择具有单个子元素的[div]元素：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<div class="container">
  <div>这是此容器中的唯一项目。</div>
</div>

<div class="container">
  <div>这是此容器中的两个项目之一。</div>
  <div>这里是第二个项目。</div>
</div>
```

```css
.container div:only-child {
  border: 2px solid crimson;
  padding: 10px;
  background-color: lightblue;
}
```

:::

[:first-of-type]和[:last-of-type]伪类选择其父元素中特定元素类型的第一次和最后一次出现。它们对于对同级元素中该元素类型的第一次或最后一次实例应用独特样式很有用。

在下面的示例中，[:first-of-type]和[:last-of-type]应用于[section]元素中的第一个元素和最后一个元素：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />

<section>
  <h2>介绍</h2>
  <p>这是第一部分中的第一个段落</p>
  <p>这是第一部分中的第二个段落</p>
</section>
<section>
  <h2>详情</h2>
  <p>这是第二部分中的第一个段落。</p>
  <p>这是第二部分中的第二个段落。</p>
</section>
```

```css
section p:first-of-type {
  background-color: lightgreen;
}

section p:last-of-type {
  background-color:lightblue;
}
```

:::

[:nth-of-type(n)]允许您根据元素在其父元素中的位置选择特定元素。例如，在下面的HTML中，[:nth-of-type(2)]定位容器中的第二个元素：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />

<div class="container">
  <p>第一个段落</p>
  <p>第二个段落</p>
  <p>第三个段落</p>
</div>
```

```css
p:nth-of-type(2) {
  color: red;
  font-weight: bold;
}
```

:::

[:only-of-type]选择其父元素中唯一的该类型元素。这对于强调单个项目或确保它们在不作为组的一部分时以不同方式设置样式很有用。

在下面的示例中，有两个[div]元素，其中一个具有单个元素。CSS仅应用于第一个容器：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />

<div class="container">
  <p>唯一的段落</p>
</div>

<div class="container">
  <p>第一个段落</p>
  <p>第二个段落</p>
</div>
```

```css
p:only-of-type {
  border: 4px solid green;
}
```

:::

# --questions--

## --text--

[:first-of-type]和[:last-of-type]伪类之间有什么区别？

## --answers--

[:first-of-type]定位其父元素中特定类型的第一个元素，而[:last-of-type]定位不同类型元素的最后一个元素。

### --feedback--

考虑这些伪类如何帮助您为特定标签（如[p]或[h1]）的第一个和最后一个实例设置样式。

---

[:first-of-type]和[:last-of-type]都定位第一个出现的元素，但在文档的不同部分。

### --feedback--

考虑这些伪类如何帮助您为特定标签（如[p]或[h1]）的第一个和最后一个实例设置样式。

---

[:first-of-type]选择其父元素中特定元素类型的第一次出现，而[:last-of-type]选择其父元素中相同元素类型的最后一次出现。

---

[:last-of-type]对文档中的第一个和最后一个元素应用样式，而[:last-of-type]对特定类型的所有元素应用样式。

### --feedback--

考虑这些伪类如何帮助您为特定标签（如[p]或[h1]）的第一个和最后一个实例设置样式。

## --video-solution--

3

## --text--

[:first-child]和[:last-child]伪类之间有什么区别？

## --answers--

[:first-child]定位其父元素中的第一个元素，而[:last-child]定位不同父元素中的最后一个元素。

### --feedback--

考虑这两个伪类如何帮助您为同一父容器中的第一个和最后一个元素设置样式。

---

[:first-child]定位其父元素中的第一个元素，而[:last-child]定位同一父元素中的最后一个元素。

---

[:first-child]定位其父元素中特定类型的第一个元素，而[:last-child]定位其父元素中不同类型元素的最后一个元素。

### --feedback--

考虑这两个伪类如何帮助您为同一父容器中的第一个和最后一个元素设置样式。

---

[:first-child]定位父元素中的第一个和最后一个元素，而[:last-child]定位所有其他元素。

### --feedback--

考虑这两个伪类如何帮助您为同一父容器中的第一个和最后一个元素设置样式。

## --video-solution--

2

## --text--

哪个伪类允许您定位没有子元素的元素，包括仅包含空白字符的元素？

## --answers--

[:empty]

---

[:first-child]

### --feedback--

考虑如何为没有内容的元素设置样式。

---

[:last-child]

### --feedback--

考虑如何为没有内容的元素设置样式。

---

[:only-of-type]

### --feedback--

考虑如何为没有内容的元素设置样式。

## --video-solution--

1