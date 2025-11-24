---
id: 672bccc8ea33bad87abb3c56
title: content-box和border-box之间有什么区别？
challengeType: 19
dashedName: what-is-the-difference-between-content-box-and-border-box
---

# --interactive--

`box-sizing`属性可以设置为`content-box`或`border-box`来控制元素宽度和高度的计算方式。这里你可以看到`box-sizing`属性和两个可能的值：

```css
box-sizing: content-box;
```

```css
box-sizing: border-box;
```

这个属性可以设置在通用选择器（`*`）上，以应用到文档中的所有元素：

```css
* {
  box-sizing: border-box;
}
```

`box-sizing`属性的默认值是`content-box`，但如果你需要的话可以选择`border-box`。我们将首先探讨`content-box`，然后进入`border-box`。

要理解这些模型如何工作，你需要熟悉CSS盒模型的四个核心概念。让我们快速回顾一下。内容区域是元素内容占据的空间。内边距是内容区域和边框之间的空间。边框是围绕内容区域和内边距的轮廓。外边距是边框外的空间，用于将元素与其他元素分隔开。

在`content-box`模型中，你为元素设置的宽度和高度决定了内容区域的尺寸，但不包括内边距、边框或外边距。当你需要精确控制内容区域的尺寸时，应该使用`content-box`。因此，当你使用`width`和`height`属性设置元素的宽度和高度时，你只是在设置内容区域的尺寸。`width`是内容的宽度，`height`是内容的高度。

要找到元素的总宽度，即你在屏幕上真正看到的，你仍然需要添加左侧和右侧的内边距，以及左侧和右侧的边框。因此，总宽度等于总宽度加上左侧内边距，加上右侧内边距，加上左侧边框，加上右侧边框。

同样，元素的总高度可以通过添加内容高度、顶部和底部边框内边距以及顶部和底部边框来找到。因此，总高度等于内容高度加上顶部内边距，加上底部内边距，加上顶部边框，加上底部边框。

例如，这里我们有一个针对所有`div`元素的CSS类型选择器。

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css">
<div></div>
```

```css
div {
  width: 300px;
  height: 200px;
  padding: 20px;
  border: 4px solid black;
}
```

:::

在这种情况下，如果使用`content-box`，内容区域的宽度将是300像素，高度将是200像素。然而，总宽度，即你在屏幕上看到的，将是内容区域宽度（300像素）加上两侧的内边距（40像素）和两侧的边框（8像素）相加的结果。

同样，总高度将是内容区域高度（200像素）加上顶部和底部内边距（40像素）以及顶部和底部边框（8像素）相加的结果。

很好！现在让我们探讨`border-box`。它们有些不同，使用`border-box`时，元素的宽度和高度包括内容区域、内边距和边框，但不包括外边距。当你需要保持固定的元素尺寸而不受内边距或边框变化的影响时，应该使用`border-box`。它对响应式网页设计也很有帮助，因为内容区域会自动调整以适应尺寸。

内边距和边框在盒子内部，所以当你设置元素的`width`和`height`属性时，你实际上是在设置盒子内部部分的宽度和高度。这是我们之前的`div`示例，具有相同的属性和值：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css">
<div></div>
```

```css
div {
  width: 300px;
  height: 200px;
  padding: 20px;
  border: 4px solid black;
}
```

:::

使用`border-box`时，`width`属性的值将是内容区域宽度、左侧和右侧内边距以及左侧和右侧边框相加的结果。因此，宽度等于内容宽度加上左侧内边距，加上右侧内边距，加上左侧边框，加上右侧边框。

同样，`height`属性的值是内容区域高度、顶部和底部内边距以及顶部和底部边框相加的结果。高度等于内容高度加上顶部内边距，加上底部内边距，加上顶部边框，加上底部边框。外边距不包括在宽度或高度中。

如果你在浏览器中使用`content-box`和`border-box`检查`div`的大小，你会注意到有一个非常重要的区别。这里有两个`div`元素，每个元素具有相同的尺寸但不同的`box-sizing`值：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css">
<div class="box" id="red-div"></div>
<div class="box" id="blue-div"></div>
```

```css
.box {
  width: 300px;
  height: 200px;
  padding: 20px;
  border: 4px solid black;
  margin: 10px;
}

#red-div {
  box-sizing: content-box;
  background-color: red;
}

#blue-div {
  box-sizing: border-box;
  background-color: blue;
}
```

:::

你可以看到它们都有相同的`width`、`height`、`padding`、`border`和`margin`。唯一的区别是颜色和`box-sizing`属性的值。这个小差异对最终尺寸有非常重要的影响。

在`content-box`和`border-box`之间选择真的取决于你项目的特定需求。虽然`border-box`因其简单性和灵活性而变得越来越流行，但理解这两种模型对于实现有效的CSS布局很重要。

# --questions--

## --text--

以下哪项是大多数浏览器中`box-sizing`属性的默认值？

## --answers--

`content-box`

---

`border-box`

### --feedback--

想想元素尺寸调整的默认行为。

---

`padding-box`

### --feedback--

想想元素尺寸调整的默认行为。

---

`margin-box`

### --feedback--

想想元素尺寸调整的默认行为。

## --video-solution--

1

## --text--

使用`border-box`创建响应式布局的主要优势是什么？

## --answers--

它使计算变得更加复杂。

### --feedback--

想想`border-box`模型如何在指定的`width`和`height`内处理`padding`和`border`。

---

它允许对元素尺寸进行更精确的控制。

### --feedback--

想想`border-box`模型如何在指定的`width`和`height`内处理`padding`和`border`。

---

它确保元素在`padding`或`border`变化时保持其指定尺寸。

---

它提高了浏览器兼容性。

### --feedback--

想想`border-box`模型如何在指定的`width`和`height`内处理`padding`和`border`。

## --video-solution--

3

## --text--

在`content-box`模型中，元素的指定`width`代表什么？

## --answers--

元素的总`width`，包括`padding`、`border`和`margin`。

### --feedback--

想想内容区域与`content-box`模型中整体元素尺寸的关系。

---

仅内容区域的`width`。

---

`border`的`width`。

### --feedback--

想想内容区域与`content-box`模型中整体元素尺寸的关系。

---

`padding`的`width`。

### --feedback--

想想内容区域与`content-box`模型中整体元素尺寸的关系。

## --video-solution--

2