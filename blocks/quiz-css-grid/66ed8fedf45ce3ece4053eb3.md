---
id: 66ed8fedf45ce3ece4053eb3
title: CSS Grid 测验
challengeType: 8
dashedName: quiz-css-grid
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

什么是 CSS Grid？

#### --distractors--

A method used for displaying tables on a website.

---

A method used for tiling images.

---

A way to display outlines around HTML elements.

#### --answer--

A two-dimensional layout for HTML documents.

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

Defines two columns and three rows for a grid container.

---

Sets all columns for the grid layout to a fixed length.

---

Creates a two column grid layout container.

#### --answer--

Defines the number of columns in a grid layout.

### --question--

#### --text--

[grid-template-rows](#) 属性做什么？

#### --distractors--

Specifies a grid item's size and location in a grid layout.

---

Creates a template for creating new grid rows.

---

Specifies a default row size in the grid container.

#### --answer--

Specifies the number and height for each row in a grid layout.

### --question--

#### --text--

[minmax()](#) 函数做什么？

#### --distractors--

Toggles between the first and second value, depending on available space.

---

Returns the average of the two inputs.

---

Sets the minimal size of the element for browser working in full-screen mode.

#### --answer--

Sets the minimum and maximum sizes for a track.

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

Implicit grids use the `grid-template-columns` property while explicit grids use the `grid-template-rows` property.

---

Explicit grids use the `grid-template-columns` property while implicit grids use the `grid-template-rows` property.

---

Implicit grids use the `grid-template-columns` or `grid-template-rows` properties to create columns while rows and columns are automatically created in explicit grids.

#### --answer--

Explicit grids use the `grid-template-columns` or `grid-template-rows` properties to create columns while rows and columns are automatically created in implicit grids.

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

Shorthand for rows and columns.

---

Outlines of a grid element.

---

Lines along which grid columns and rows are created.

#### --answer--

Lines on which each of the grid items begin and end.

### --question--

#### --text--

[grid-column](#) 属性做什么？

#### --distractors--

Adds a new grid element as a child of the element it's applied to.

---

Aligns text in the grid item vertically.

---

Sets two columns for a grid container.

#### --answer--

Tells the grid item on which grid line it should start and end at.

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

It is used to specify where the item begins on a line in the grid container.

---

It is used to create gaps between tracks in the container.

---

It is used to repeat sections in the track listing.

#### --answer--

It is used to provide a name for the items you are going to position on the grid.

### --question--

#### --text--

[grid-auto-flow](#) 属性做什么？

#### --distractors--

Controls the order in which grid items are displayed.

---

Adjusts the spacing between the grid elements.

---

Automatically adjusts the element to fit in the grid.

#### --answer--

Controls how auto-placed elements get inserted to the grid.

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

Shorthand for rows and columns.

---

Lines along which you can animate movement of the grid items.

---

Lines on which each of the grid items begins and ends.

#### --answer--

Spaces between two adjacent grid lines.

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

By directly defining the item's size and location within the grid using `grid-template-rows` and `grid-template-columns`.

---

By using the `grid-area` property and specifying both row and column start and end positions.

---

By setting both `grid-area` and explicit pixel coordinates.

#### --answer--

By assigning the named area to the item's `grid-area` property.

### --question--

#### --text--

[grid-auto-rows](#) 属性控制什么？

#### --distractors--

The height of explicitly defined rows.

---

The maximum width of grid columns.

---

The spacing between rows.

#### --answer--

The size of implicitly created rows.

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

Tracks created automatically to fit content.

---

Tracks defined by the `fr` unit.

---

Tracks added with `grid-auto-flow`.

#### --answer--

Tracks explicitly set by `grid-template-columns` or `grid-template-rows`.

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

To auto-generate implicit tracks.

---

To replace the `fr` unit.

---

To set `z-index` values.

#### --answer--

To visually map items to named grid areas.

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

Creates three equal-width columns.

---

Makes the middle column three times as wide as the others.

---

Forces all columns to be exactly `1fr` wide.

#### --answer--

Creates three columns where the middle is twice as wide as the sides.

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

Three columns that can't shrink below `100px`.

---

Three fixed `100px` columns.

---

Three rows with maximum height of `1fr`.

#### --answer--

Three columns that grow proportionally but won't shrink below `100px`.

### --question--

#### --text--

关于隐式网格，以下哪个陈述是正确的？

#### --distractors--

Implicit grids ignore the `gap` property.

---

Implicit tracks must be defined with `grid-template-areas`.

---

Implicit tracks can only be created using the `grid-auto-flow` property.

#### --answer--

Implicit tracks are created when content doesn't fit explicit tracks.

### --question--

#### --text--

CSS Grid 中的 [place-items](#) 属性做什么？

#### --distractors--

It sets the size of grid items automatically based on available space.

---

It controls the grid template's column and row definitions.

---

It adjusts the order of grid items within the container.

#### --answer--

It is a shorthand for aligning grid items in both the block and inline axes.

### --question--

#### --text--

这段 CSS 实现了什么？

```css
.container {
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}
```

#### --distractors--

Creates fixed `150px` columns that overflow the container.

---

Creates columns that are exactly `1fr` wide regardless of content.

---

Creates a maximum of one column per `150px` of available width.

#### --answer--

Creates flexible columns that are at least `150px` and collapse when space is limited.

### --question--

#### --text--

如何创建不对称的网格布局？

#### --distractors--

By using only `fr` units.

---

By mixing different length units in `grid-template-columns`.

---

By setting `grid-asymmetric: true`.

#### --answer--

By defining different sizes for each track.

### --question--

#### --text--

[grid-column-start: 2](#)` 对网格项目有什么作用？

#### --distractors--

Makes it span 2 columns.

---

Offsets it by 2 pixels.

---

Positions it starting at the second vertical grid line.

#### --answer--

Makes it start at the second column line.

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

The container will have three columns of equal width, and two rows with `150px` height each.

---

The container will have three columns, all with `100px` width, and two rows with `150px` height.

---

The container will have two rows, each with a height of `1fr`.

#### --answer--

The container will have three columns: 100px, `1fr` and `2fr` wide and two rows: one auto and one with `150px` height.

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