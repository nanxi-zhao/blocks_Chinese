---
id: 672bccae6e556cd81cef6af2
title: 什么是外边距合并，它是如何工作的？
challengeType: 19
dashedName: what-is-margin-collapsing
---

# --interactive--

外边距合并是CSS中的一个基本概念，经常让Web开发新手感到困惑。

当相邻元素的垂直外边距重叠时，这种行为就会发生，导致产生一个等于两者中较大值的单一外边距。

理解外边距合并对于精确控制Web设计中的间距和布局很重要。那么，让我们深入了解外边距合并的工作原理，并探讨一些常见的发生场景。

在CSS中，当两个垂直外边距相互接触时，它们会合并，这意味着不是将它们相加，而是较大的外边距获胜并决定元素之间的空间。这种行为仅适用于垂直外边距（顶部和底部），而不适用于水平外边距（左侧和右侧）。下面是一个示例来说明这个概念：

:::interactive_editor

```html
<style>
  .box1 {
    margin-bottom: 20px;
    background-color: lightblue;
  }
  .box2 {
    margin-top: 30px;
    background-color: lightgreen;
  }
</style>

<div class="box1">Box 1</div>
<div class="box2">Box 2</div>
```

:::

在这个示例中，你可能期望`.box1`和`.box2`之间的总空间为50像素（20像素加30像素）。然而，由于外边距合并，实际空间将是30像素，这是两个外边距中较大的一个。

正如我们在前面的示例中看到的，相邻兄弟元素的外边距会合并。这是外边距合并最直接的情况。让我们探讨更多可能发生外边距合并的情况。

外边距也可以在父元素与其第一个或最后一个子元素之间合并。如果没有边框、内边距、内联内容或清除来分隔父元素的外边距和子元素的外边距，它们就会合并。

:::interactive_editor

```html
<style>
  .parent {
    margin-top: 40px;
    background-color: lightyellow;
  }
  .child {
    margin-top: 30px;
    background-color: lightpink;
  }
</style>

<div class="parent">
  <div class="child">子元素</div>
</div>
```

:::

在这种情况下，你可能期望子元素距离顶部70像素（40像素加30像素）。然而，外边距会合并，使用较大的外边距40像素。

如果一个元素没有内容、内边距或边框，其顶部和底部外边距可以合并成一个单一的外边距。

:::interactive_editor

```html
<style>
  .empty-block {
    margin-top: 20px;
    margin-bottom: 10px;
    height: 0;
  }
  .next-block {
    background-color: lightgray;
  }
</style>

<div class="empty-block"></div>
<div class="next-block">下一个块</div>
```

:::

在这个示例中，`empty-block`的顶部和底部外边距合并成一个20像素的单一外边距，这是两者中较大的一个。

这是另一个使用内边距防止合并的示例：

:::interactive_editor

```html
<style>
  .parent {
    margin-top: 40px;
    padding-top: 1px;
    background-color: lightyellow;
  }
  .child {
    margin-top: 30px;
    background-color: lightpink;
  }
</style>

<div class="parent">
  <div class="child">子元素</div>
</div>
```

:::

在这种情况下，父元素上的1像素内边距防止了外边距合并，导致从父元素顶部到子内容顶部的总空间为71像素。

理解外边距合并对于精确控制CSS中的布局和间距很重要。虽然它有时会导致意外结果，但这是一个旨在为文档创建更美观和一致间距的特性。通过了解外边距合并何时发生以及如何在必要时防止它，你可以在Web设计中创建更可预测和可维护的布局。

# --questions--

## --text--

外边距合并在哪个方向发生？

## --answers--

仅水平外边距。

### --feedback--

想想哪些外边距（顶部、底部、左侧、右侧）受这种行为影响。

---

仅垂直外边距。

---

水平和垂直外边距都受影响。

### --feedback--

想想哪些外边距（顶部、底部、左侧、右侧）受这种行为影响。

---

对角线外边距。

### --feedback--

想想哪些外边距（顶部、底部、左侧、右侧）受这种行为影响。

## --video-solution--

2

## --text--

当两个相邻元素具有不同的外边距值时会发生什么？

## --answers--

外边距相加。

### --feedback--

考虑合并发生时哪个外边距"获胜"。

---

使用较小的外边距。

### --feedback--

考虑合并发生时哪个外边距"获胜"。

---

使用较大的外边距。

---

使用两个外边距的平均值。

### --feedback--

考虑合并发生时哪个外边距"获胜"。

## --video-solution--

3

## --text--

以下哪项不会防止父元素与其第一个子元素之间的外边距合并？

## --answers--

给父元素添加`border`。

### --feedback--

想想哪些属性在父元素和子元素外边距之间创建分隔。

---

在父元素上设置`padding-top: 1px;`。

### --feedback--

想想哪些属性在父元素和子元素外边距之间创建分隔。

---

在子元素上使用`display: inline-block;`。

### --feedback--

想想哪些属性在父元素和子元素外边距之间创建分隔。

---

在子元素上设置`margin-top: 0;`。

## --video-solution--

4