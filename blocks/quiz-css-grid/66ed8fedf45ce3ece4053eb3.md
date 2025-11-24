---
id: 66ed8fedf45ce3ece4053eb3
title: CSS Grid 测验
challengeType: 8
dashedName: quiz-css-grid
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 道题。

# --quizzes--

## --quiz--

### --question--

#### --text--

什么是 CSS Grid？

#### --distractors--

在网站上显示表格的方法。

---

平铺图像的方法。

---

显示 HTML 元素轮廓的方法。

#### --answer--

用于 HTML 文档的二维布局。

### --question--

#### --text--

以下哪个是创建网格容器的正确方法？

#### --distractors--

`display: grid-area;`

---

`grid: grid-template;`

---

`grid-template: set;`

#### --answer--

`display: grid;`

### --question--

#### --text--

[grid-template-columns](#) 属性做什么？

#### --distractors--

为网格容器定义两列三行。

---

将网格布局中的所有列设置为固定长度。

---

创建一个两列网格布局容器。

#### --answer--

定义网格布局中的列数。

### --question--

#### --text--

[grid-template-rows](#) 属性做什么？

#### --distractors--

指定网格布局中项目的大小和位置。

---

为创建新网格行创建模板。

---

在网格容器中指定默认行大小。

#### --answer--

指定网格布局中每行的数量和高度。

### --question--

#### --text--

[minmax()](#) 函数做什么？

#### --distractors--

根据可用空间在第一个和第二个值之间切换。

---

返回两个输入的平均值。

---

为在全屏模式下工作的浏览器设置元素的最小尺寸。

#### --answer--

设置轨道的最小和最大尺寸。

### --question--

#### --text--

[column-gap](#) 和 [row-gap](#) 属性的简写是什么？

#### --distractors--

`gap-column-row`

---

`gutters`

---

`grid-gap`

#### --answer--

`gap`

### --question--

#### --text--

隐式网格和显式网格有什么区别？

#### --distractors--

隐式网格使用 `grid-template-columns` 属性，而显式网格使用 `grid-template-rows` 属性。

---

显式网格使用 `grid-template-columns` 属性，而隐式网格使用 `grid-template-rows` 属性。

---

隐式网格使用 `grid-template-columns` 或 `grid-template-rows` 属性创建列，而显式网格会自动创建行和列。

#### --answer--

显式网格使用 `grid-template-columns` 或 `grid-template-rows` 属性创建列，而隐式网格会自动创建行和列。

### --question--

#### --text--

以下哪个单位表示网格容器内空间的分数？

#### --distractors--

`fractional`

---

`frac`

---

`f`

#### --answer--

`fr`

### --question--

#### --text--

什么是网格线？

#### --distractors--

行和列的简写。

---

网格元素的轮廓。

---

创建网格行和列的线条。

#### --answer--

网格项目开始和结束的线条。

### --question--

#### --text--

[grid-column](#) 属性做什么？

#### --distractors--

将新的网格元素添加为应用到的元素的子元素。

---

垂直对齐网格项目中的文本。

---

为网格容器设置两列。

#### --answer--

告诉网格项目它应该在哪个网格线上开始和结束。

### --question--

#### --text--

如何创建四个等宽的列？

#### --distractors--

`grid-template-columns: repeat(4);`

---

`grid-template-columns: repeat(1, 4);`

---

`grid-template-columns: repeat(1fr, 4);`

#### --answer--

`grid-template-columns: repeat(4, 1fr);`

### --question--

#### --text--

[grid-template-areas](#) 属性做什么？

#### --distractors--

用于指定项目在网格容器中的起始行。

---

用于在容器中创建轨道之间的间隙。

---

用于重复轨道列表中的部分。

#### --answer--

用于为要在网格上定位的项目提供名称。

### --question--

#### --text--

[grid-auto-flow](#) 属性做什么？

#### --distractors--

控制网格项目显示的顺序。

---

调整网格元素之间的间距。

---

自动调整元素以适应网格。

#### --answer--

控制自动放置的元素如何插入到网格中。

### --question--

#### --text--

以下哪个是使用 [grid-template-areas](#) 属性的正确方法？

#### --distractors--

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr; 
  grid-template-rows: auto 1fr auto; 
  grid-template-areas: set(
    "header header"
    "sidebar main"
    "footer footer" 
  );
  gap: 20px; 
}
```

---

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr; 
  grid-template-rows: auto 1fr auto; 
  grid-template-areas: apply(
    "header header"
    "sidebar main"
    "footer footer" 
  );
  gap: 20px; 
}
```

---

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr; 
  grid-template-rows: auto 1fr auto; 
  grid-template-areas: set-areas;
  gap: 20px; 
}
```

#### --answer--

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr; 
  grid-template-rows: auto 1fr auto; 
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer"; 
  gap: 20px; 
}
```

### --question--

#### --text--

以下哪个是使用 [grid-auto-flow](#) 属性的正确方法？

#### --distractors--

```css
.social-icons {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-auto-flow: none;
  grid-auto-columns: 1fr;
}
```

---

```css
.social-icons {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-auto-flow: allow;
  grid-auto-columns: 1fr;
}
```

---

```css
.social-icons {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-auto-flow: set;
  grid-auto-columns: 1fr;
}
```

#### --answer--

```css
.social-icons {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
}
```

### --question--

#### --text--

以下哪个不是有效的网格属性？

#### --distractors--

`gap`

---

`grid-column`

---

`grid-template-columns`

#### --answer--

`grid-set`

### --question--

#### --text--

以下哪个属性可用于居中网格元素内的项目？

#### --distractors--

`allow-items`

---

`set-items`

---

`center-items`

#### --answer--

`align-items`

### --question--

#### --text--

以下哪个是与 [grid-auto-columns](#) 属性一起使用的正确值？

#### --distractors--

`grid-auto-columns: unset-grid;`

---

`grid-auto-columns: revert-grid;`

---

`grid-auto-columns: set-content(20%);`

#### --answer--

`grid-auto-columns: 1fr;`

### --question--

#### --text--

什么是网格轨道？

#### --distractors--

行和列的简写。

---

可以为网格项目移动设置动画的线条。

---

每个网格项目开始和结束的线条。

#### --answer--

两个相邻网格线之间的空间。

### --question--

#### --text--

以下哪个是使用 [minmax()](#) 函数的正确方法？

#### --distractors--

```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(apply);
}
```

---

```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax();
}
```

---

```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(set);
}
```

#### --answer--

```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(150px, auto);
}
```

## --quiz--

### --question--

#### --text--

如何在由 [grid-template-areas](#) 定义的布局中定位网格项目？

#### --distractors--

通过直接使用 `grid-template-rows` 和 `grid-template-columns` 定义项目在网格中的大小和位置。

---

通过使用 `grid-area` 属性并指定行和列的开始和结束位置。

---

通过设置 `grid-area` 和明确的像素坐标。

#### --answer--

通过将命名区域分配给项目的 `grid-area` 属性。

### --question--

#### --text--

[grid-auto-rows](#) 属性控制什么？

#### --distractors--

显式定义行的高度。

---

网格列的最大宽度。

---

行之间的间距。

#### --answer--

隐式创建行的大小。

### --question--

#### --text--

你会使用哪个属性使网格项目跨越多行？

#### --distractors--

`grid-row-span`

---

`row-span`

---

`span-rows`

#### --answer--

`grid-row`

### --question--

#### --text--

什么定义了显式网格？

#### --distractors--

为适应内容而自动创建的轨道。

---

由 `fr` 单位定义的轨道。

---

使用 `grid-auto-flow` 添加的轨道。

#### --answer--

由 `grid-template-columns` 或 `grid-template-rows` 显式设置的轨道。

### --question--

#### --text--

[grid-auto-flow](#) 的哪个值会使新项目首先填充列？

#### --distractors--

`row`

---

`vertical`

---

`row dense`

#### --answer--

`column`

### --question--

#### --text--

[grid-template-areas](#) 的用途是什么？

#### --distractors--

自动生成隐式轨道。

---

替换 `fr` 单位。

---

设置 `z-index` 值。

#### --answer--

将项目可视化映射到命名网格区域。

### --question--

#### --text--

如何使网格项目从第 2 列线开始到第 4 列线结束？

#### --distractors--

`grid-column: 2 / span 4;`

---

`grid-column: start 2 / end 4;`

---

`grid-column: from 2 to 4;`

#### --answer--

`grid-column: 2 / 4;`

### --question--

#### --text--

[grid-template-columns: 1fr 2fr 1fr](#)` 有什么效果？

#### --distractors--

创建三个等宽列。

---

使中间列是其他列的三倍宽。

---

强制所有列都正好是 `1fr` 宽。

#### --answer--

创建三列，其中中间列是两侧列的两倍宽。

### --question--

#### --text--

如何创建一个有 3 个等列和 20px 列间隙的网格？

#### --distractors--

```css
.container {
  display: grid;
  grid-template: repeat(3, 1fr) / 20px;
} 
```

---

```css
.container {
  display: grid;
  grid: 1fr 1fr 1fr / gap 20px;
}
```

---

```css
.container {
  display: grid;
  grid-template-columns: 20px 1fr 1fr 1fr;
}
```

#### --answer--

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
```

### --question--

#### --text--

[repeat(3, minmax(100px, 1fr))](#)` 创建什么？

#### --distractors--

三个不会缩小到 `100px` 以下的列。

---

三个固定的 `100px` 列。

---

三个最大高度为 `1fr` 的行。

#### --answer--

三个按比例增长但不会缩小到 `100px` 以下的列。

### --question--

#### --text--

关于隐式网格，以下哪个陈述是正确的？

#### --distractors--

隐式网格忽略 `gap` 属性。

---

隐式轨道必须用 `grid-template-areas` 定义。

---

隐式轨道只能使用 `grid-auto-flow` 属性创建。

#### --answer--

当内容不适合显式轨道时，会创建隐式轨道。

### --question--

#### --text--

CSS Grid 中的 [place-items](#) 属性做什么？

#### --distractors--

它根据可用空间自动设置网格项目的大小。

---

它控制网格模板的列和行定义。

---

它调整网格容器内网格项目的顺序。

#### --answer--

它是对齐块轴和行内轴中网格项目的简写。

### --question--

#### --text--

这段 CSS 实现了什么？

```css
.container {
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}
```

#### --distractors--

创建固定 `150px` 的列，这些列会溢出容器。

---

创建正好 `1fr` 宽的列，无论内容如何。

---

每 `150px` 可用宽度创建一个最大列。

#### --answer--

创建至少 `150px` 的灵活列，并在空间有限时折叠。

### --question--

#### --text--

如何创建不对称的网格布局？

#### --distractors--

仅使用 `fr` 单位。

---

在 `grid-template-columns` 中混合不同的长度单位。

---

设置 `grid-asymmetric: true`。

#### --answer--

通过为每个轨道定义不同的尺寸。

### --question--

#### --text--

[grid-column-start: 2](#)` 对网格项目有什么作用？

#### --distractors--

使其跨越 2 列。

---

将其偏移 2 像素。

---

将其定位在从第二条垂直网格线开始的位置。

#### --answer--

使其从第二条列线开始。

### --question--

#### --text--

你会使用哪个属性来控制网格轨道中的溢出行为？

#### --distractors--

`grid-overflow`

---

`track-sizing`

---

`fit-content`

#### --answer--

`minmax()`

### --question--

#### --text--

以下代码的结果是什么？

```css
.container {
  display: grid;
  grid-template-columns: 100px 1fr 2fr;
  grid-template-rows: auto 150px;
  gap: 10px;
}
```

#### --distractors--

容器将有三个等宽列，和两个高度为 `150px` 的行。

---

容器将有三个列，都具有 `100px` 宽度，和两个高度为 `150px` 的行。

---

容器将有两行，每行高度为 `1fr`。

#### --answer--

容器将有三列：100px、`1fr` 和 `2fr` 宽，以及两行：一个自动和一个 `150px` 高度。

### --question--

#### --text--

如何使网格项目跨越所有可用行？

#### --distractors--

`grid-row: full;`

---

`grid-row: auto / -1;`

---

`grid-row: 1 / span infinite;`

#### --answer--

`grid-row: 1 / -1;`

### --question--

#### --text--

哪个属性控制网格项目沿块轴的对齐？

#### --distractors--

`justify-items`

---

`place-items`

---

`align-content`

#### --answer--

`align-items`

### --question--

#### --text--

如何确保网格项目无论网格如何变化都保持在第一列？

#### --distractors--

`grid-column: fixed;`

---

`grid-column: first;`

---

`grid-lock: column;`

#### --answer--

`grid-column: 1;`