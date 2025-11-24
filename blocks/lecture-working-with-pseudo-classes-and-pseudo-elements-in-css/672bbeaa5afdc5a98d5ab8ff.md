---
id: 672bbeaa5afdc5a98d5ab8ff
title: 位置伪类的示例有哪些？
challengeType: 19
dashedName: what-are-examples-of-location-pseudo-classes
---

# --interactive--

位置伪类用于为链接和当前文档中作为目标的元素设置样式。它们提供了一种基于链接是否被访问或元素当前是否处于焦点状态来应用样式的方法。

位置伪类的示例包括：

- [:link]
- [:visited]
- [:any-link]
- [:local-link]
- [:target]
- [:target-within]

让我们更深入地了解这些伪类中的每一个。

[:link]伪类允许您定位网页上所有未访问的链接。您可以使用它在用户点击链接之前以不同方式设置链接样式。例如，您可能希望将所有未访问的链接设置为蓝色或您网站的主要颜色：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<a target="_blank" href="https://www.example.com">访问Example.com</a>
```

```css
a:link {
  color: magenta;
}
```

:::

在这种情况下，用户尚未点击的任何链接都会显示为洋红色。一旦用户点击链接，[:link]样式将不再适用，[:visited]伪类将接管。[:visited]伪类在用户点击链接后起作用，因此您可以使用它来定位用户已经点击的链接。

这是一个将已访问链接状态更改为紫色的示例：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<a target="_blank" href="https://www.example.com">访问Example.com</a>
```

```css
a:visited {
  color: purple;
}
```

:::

[:visited]伪类帮助用户区分已访问和未访问的链接。

[:any-link]伪类是[:link]和[:visited]伪类的组合。因此，它匹配任何具有[href]属性的锚元素，无论它是否被访问过。

这是一个将[:any-link]伪类的链接颜色更改为深红色的示例：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<a target="_blank" href="https://www.example.com">访问Example.com</a>
```

```css
a:any-link {
  color: crimson;
}
```

:::

[:local-link]伪类针对指向同一文档的链接。当您想要区分内部链接和外部链接时，它很有用。目前，没有浏览器支持[:local-link]伪类。

[:target]伪类选择与当前URL片段标识符匹配的元素，例如[#section1]。对于具有页面内导航的页面非常有用。

这是一个表示页面内导航的HTML示例。CSS使用[:target]伪类为用户导航到的相应部分设置样式：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<nav id="table-of-contents">
  <ul>
    <li><a href="#section1">介绍</a></li>
    <li><a href="#section2">特性</a></li>
  </ul>
</nav>

<section id="section1">
  <h2>介绍</h2>
  <p>这是介绍部分。</p>
</section>

<section id="section2">
  <h2>特性</h2>
  <p>本节描述了特性。</p>
</section>
```

```css
section:target {
  background-color: green;
  border: 2px solid green;
  padding: 10px;
}
```

:::

当用户点击其中一个导航链接时，相应部分的背景颜色将变为绿色。

# --questions--

## --text--

哪个伪类允许您为与当前URL片段标识符匹配的元素设置样式，例如[#section1]？

## --answers--

[:hover]

### --feedback--

考虑如何在通过页面内链接导航时突出显示特定部分。

---

[:focus]

### --feedback--

考虑如何在通过页面内链接导航时突出显示特定部分。

---

[:target]

---

[:checked]

### --feedback--

考虑如何在通过页面内链接导航时突出显示特定部分。

## --video-solution--

3

## --text--

位置伪类在什么时候特别有用？

## --answers--

当基于兄弟关系设置元素样式时。

### --feedback--

考虑如何根据用户交互设置链接和目标元素的样式。

---

当基于链接是否被访问或元素当前是否处于焦点状态应用样式时。

---

当基于父元素属性设置元素样式时。

### --feedback--

考虑如何根据用户交互设置链接和目标元素的样式。

---

当动态调整网页布局时。

### --feedback--

考虑如何根据用户交互设置链接和目标元素的样式。

## --video-solution--

2

## --text--

哪个伪类旨在针对指向同一文档的链接，但目前不受任何浏览器支持？

## --answers--

[:any-link]

### --feedback--

考虑用于区分内部链接和外部链接的伪类，尽管它尚未受支持。

---

[:local-link]

---

[:visited]

### --feedback--

考虑用于区分内部链接和外部链接的伪类，尽管它尚未受支持。

---

[:target]

### --feedback--

考虑用于区分内部链接和外部链接的伪类，尽管它尚未受支持。

## --video-solution--

2