---
id: 66ed8ffcf45ce3ece4053eb5
title: CSS 定位测验
challengeType: 8
dashedName: quiz-css-positioning
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

以下哪个不是 [position](#) 属性的有效值？

#### --distractors--

`fixed`

---

`absolute`

---

`relative`

#### --answer--

`above`

### --question--

#### --text--

CSS 中 [float](#) 属性的主要用途是什么？

#### --distractors--

Floats are used to remove an element from its normal flow on the page and automatically position it in the upper right hand side of the webpage.

---

Floats are used to remove an element from its normal flow on the page and position it to the top of its container.

---

Floats are used to remove an element from its normal flow on the page and automatically position it to the bottom right hand side of webpage.

#### --answer--

Floats are used to remove an element from its normal flow on the page and position it either on the left or right side of its container.

### --question--

#### --text--

以下哪个示例使一个盒子元素向左浮动？

#### --distractors--

```css
.box {
  left: float;
  margin-right: 15px;
  width: 50px;
  height: 50px;
  background-color: black;
}
```

---

```css
.box {
  position: float-left;
  margin-right: 15px;
  width: 50px;
  height: 50px;
  background-color: black;
}
```

---

```css
.box {
  float: left-side;
  margin-right: 15px;
  width: 50px;
  height: 50px;
  background-color: black;
}
```

#### --answer--

```css
.box {
  float: left;
  margin-right: 15px;
  width: 50px;
  height: 50px;
  background-color: black;
}
```

### --question--

#### --text--

[clear](#) 属性的作用是什么？

#### --distractors--

It is used to determine if an element needs to be moved to the bottom of the page.

---

It is used to determine if an element needs to be completely cleared from the page.

---

It is used to determine if an element needs to be fixed to the top of the page.

#### --answer--

It is used to determine if an element needs to be moved below the floated content.

### --question--

#### --text--

哪个 CSS 属性用于控制重叠定位元素在页面上的垂直堆叠顺序？

#### --distractors--

`position`

---

`bg-green`

---

`float`

#### --answer--

`z-index`

### --question--

#### --text--

以下哪个是相对定位的正确语法？

#### --distractors--

```css
.relative {
  position: relative-position;
  top: 30px;
  left: 30px;
}
```

---

```css
.relative {
  relative-position: relative;
  top: 30px;
  left: 30px;
}
```

---

```css
.relative {
  relative: position;
  top: 30px;
  left: 30px;
}
```

#### --answer--

```css
.relative {
  position: relative;
  top: 30px;
  left: 30px;
}
```

### --question--

#### --text--

你会使用哪个 CSS 属性来将一个元素固定在页面的某个位置，使其在滚动时不会移动？

#### --distractors--

`position: no-scroll;`

---

`position: relative;`

---

`display: block;`

#### --answer--

`position: fixed;`

### --question--

#### --text--

绝对定位对元素有什么作用？

#### --distractors--

Absolute positioning is used to determine if an element needs to be moved below the floated content.

---

Absolute positioning is used to position the element within the normal document flow.

---

Absolute positioning is used to control the vertical stacking order of positioned elements that overlap on the page.

#### --answer--

Absolute positioning allows you to take an element out of the normal document flow, making it behave independently from other elements.

### --question--

#### --text--

以下哪个不是你可以用于绝对定位的有效属性？

#### --distractors--

`right`

---

`bottom`

---

`top`

#### --answer--

`side`

### --question--

#### --text--

相对定位和绝对定位的关键区别是什么？

#### --distractors--

Absolute positioning sets the element in a sticky position while relative positioning takes an element out of the normal document flow.

---

Relative positioning sets the element in a fixed position while absolute positioning takes an element out of the normal document flow.

---

Absolute positioning positions the element within the normal document flow while relative positioning takes an element out of the normal document flow.

#### --answer--

Relative positioning positions the element within the normal document flow while absolute positioning takes an element out of the normal document flow.

### --question--

#### --text--

以下哪个示例将一个盒子定位在页面的左上角？

#### --distractors--

```css
.box {
  position: absolute;
  bottom: 0;
  left: 0;
  background-color: coral;
  width: 50px;
  height: 50px;
}
```

---

```css
.box {
  position: absolute;
  top: 0;
  right: 0;
  background-color: coral;
  width: 50px;
  height: 50px;
}
```

---

```css
.box {
  position: absolute;
  bottom: 0;
  right: 0;
  background-color: coral;
  width: 50px;
  height: 50px;
}
```

#### --answer--

```css
.box {
  position: absolute;
  top: 0;
  left: 0;
  background-color: coral;
  width: 50px;
  height: 50px;
}
```

### --question--

#### --text--

哪种定位方法允许元素在你滚动到某个点时粘贴到一个定义的位置？

#### --distractors--

Float positioning.

---

Fixed positioning.

---

Absolute positioning.

#### --answer--

Sticky positioning.

### --question--

#### --text--

以下哪个是使用粘性定位的正确示例？

#### --distractors--

```css
.box {
  sticky: position;
  top: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  background-color: red;
}
```

---

```css
.box {
  position: sticky-fixed;
  top: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  background-color: red;
}
```

---

```css
.box {
  position: sticky-top;
  right: 30px;
  width: 50px;
  height: 50px;
  background-color: red;
}
```

#### --answer--

```css
.box {
  position: sticky;
  top: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  background-color: red;
}
```

### --question--

#### --text--

粘性定位和固定定位有什么区别？

#### --distractors--

Sticky elements can only be used in table layouts while fixed elements can be used in any type of CSS layout.

---

Sticky elements will always remain in the same position while fixed elements will stick to a certain point then behave like relative elements.

---

Fixed elements will be positioned relative to its normal position while sticky elements will only stick to a certain point then behave like relative elements.

#### --answer--

Fixed elements will remain in the same position on the screen while sticky elements will only stick to a certain point then behave like relative elements.

### --question--

#### --text--

[clearfix](#) 黑客解决了使用浮动时的什么问题？

#### --distractors--

The `clearfix` hack helped solve the issue of floated elements being removed from the normal document flow and being placed in a fixed position on the page.

---

The `clearfix` hack helped solve the issue of floated elements not being responsive in mobile and tablet layouts.

---

The `clearfix` hack helped solve the issue of floated elements disappearing from the page.

#### --answer--

The `clearfix` hack helped solve the issue of overlaps and collapsing in the layouts when multiple floated elements were stacked next to each other.

### --question--

#### --text--

以下哪个是使用 [clearfix](#) 黑客的正确示例？

#### --distractors--

```css
.clearfix::before {
  position: fixed;
  top: 0;
  width: 100%;
  clear: both;
}
```

---

```css
.clearfix::after {
  position: relative;
  top: 30px;
  left: 30px;
  clear: all;
}
```

---

```css
.clearfix::before {
  top: 30px;
  clear: none;
}
```

#### --answer--

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

### --question--

#### --text--

什么是静态定位？

#### --distractors--

This is used to remove an element from its normal flow on the page and automatically position it in the upper right hand side of the webpage.

---

This allows you to take an element out of the normal document flow, making it behave independently from other elements.

---

This allows an element to stick to a defined position only when you scroll past a certain point.

#### --answer--

This is the normal flow for the document. Elements are positioned from top to bottom and left to right one after another.

### --question--

#### --text--

以下哪个示例使用固定定位将导航栏设置在页面顶部？

#### --distractors--

```css
.navbar {
  fixed: top;
  top: 0;
  width: 100%;
}
```

---

```css
.navbar {
  upper: fixed;
  width: 100%;
}
```

---

```css
.navbar {
  position: fixed-top;
  top: 0;
  width: 100%;
}
```

#### --answer--

```css
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
}
```

### --question--

#### --text--

以下哪个是可用于 [z-index](#) 属性的有效值？

#### --distractors--

`12.0`

---

`none`

---

`up`

#### --answer--

`1`

### --question--

#### --text--

以下哪个是 [position](#) 属性的默认值？

#### --distractors--

`inherit`

---

`initial`

---

`relative`

#### --answer--

`static`

## --quiz--

### --question--

#### --text--

哪个 [position](#) 值允许你使用 [top](#) 和 [left](#) 调整元素位置，同时保持其在正常文档流中？

#### --distractors--

`position: absolute;`

---

`position: static;`

---

`position: fixed;`

#### --answer--

`position: relative;`

### --question--

#### --text--

具有 `position: sticky;` 的元素最初如何表现？

#### --distractors--

It behaves like a `fixed` element until a scroll position is reached.

---

It is always removed from the normal document flow.

---

It behaves like an `absolute` element within its parent.

#### --answer--

It behaves like a `relative` element until a specified scroll position is met.

### --question--

#### --text--

以下哪个示例演示了有效使用 [z-index](#) 属性使 `.box-two` 出现在 `.box-one` 上方？

#### --distractors--

```css
.box-one {
  position: static;
  z-index: 2;
}
.box-two {
  position: static;
  z-index: 1;
}
```

---

```css
.box-one {
  position: absolute;
  stack-order: 1;
}
.box-two {
  position: absolute;
  stack-order: 2;
}
```

---

```css
.box-one {
  float: left;
  z-index: 1;
}
.box-two {
  float: left;
  z-index: 2;
}
```

#### --answer--

```css
.box-one {
  position: absolute;
  z-index: 1;
}
.box-two {
  position: absolute;
  z-index: 2;
}
```

### --question--

#### --text--

CSS 中的 [z-index](#) 属性用于什么？

#### --distractors--

It sets the zoom level of the page.

---

It controls the horizontal alignment of elements within a flex container.

---

It defines the spacing between an element's content and its border.

#### --answer--

It controls the vertical stacking order of positioned elements that overlap.

### --question--

#### --text--

当你对具有 `position: fixed;` 的元素应用 `top: 10%;` 时，[10%](#) 是相对于什么计算的？

#### --distractors--

The height of the element itself.

---

The height of its parent container.

---

The width of the viewport.

#### --answer--

The height of the viewport.

### --question--

#### --text--

以下哪个代码示例是使用 [z-index](#) 属性将覆盖层置于其他内容之上的正确方法？

#### --distractors--

```css
.overlay {
  z-index: 5;
  background-color: black;
}
```

---

```css
.overlay {
  display: block;
  z-layer: 1;
  background-color: black;
}
```

---

```css
.overlay {
  float: left;
  z-index: 2;
  background-color: black;
}
```

#### --answer--

```css
.overlay {
  position: absolute;
  z-index: 10;
  background-color: black;
}
```

### --question--

#### --text--

哪个 CSS 属性用于控制元素是否应移至浮动元素下方？

#### --distractors--

`float`

---

`overflow`

---

`display`

#### --answer--

`clear`

### --question--

#### --text--

具有 `position: relative;` 和 `bottom: 25px;` 的元素将如何移动？

#### --distractors--

It will move 25px down from its normal position.

---

It will move 25px to the right of its normal position.

---

It will be positioned 25px from the bottom of the viewport.

#### --answer--

It will move 25px up from its normal position.

### --question--

#### --text--

[z-index](#) 属性只会影响应用了什么 CSS 属性的元素？

#### --distractors--

A `float` value other than `none`.

---

A `display` value of `inline-block`.

---

A `background-color` set.

#### --answer--

A `position` value other than `static`.

### --question--

#### --text--

对标题中的徽标应用 `float: right;` 会有什么效果？

#### --distractors--

The logo would be aligned to the right, but would remain in the normal document flow, preventing other content from wrapping.

---

The logo would be taken out of the flow and positioned on the right side of the entire browser viewport, not its container.

---

The logo would become a block-level element that takes up the full width of the header, pushing other elements below it.

#### --answer--

The logo would be removed from its normal flow and placed on the right side of its container, with other content wrapping around it.

### --question--

#### --text--

哪个 CSS 片段将在滚动到元素时将其固定在视口顶部？

#### --distractors--

```css
.header {
  position: fixed;
  top: 0;
}
```

---

```css
.header {
  position: relative;
  top: 0;
}
```

---

```css
.header {
  position: absolute;
  top: 0;
}
```

#### --answer--

```css
.header {
  position: sticky;
  top: 0;
}
```

### --question--

#### --text--

CSS 中 `clear: both;` 的具体用途是什么？

#### --distractors--

It cancels out the `float` property on the element itself, returning it to the normal document flow.

---

It removes any `clear` properties that were inherited from a parent element, restoring the default floating behavior.

---

It only clears floated elements that are on the right side, allowing left-floated elements to remain as they are.

#### --answer--

It ensures the element is moved below any floated elements that appear before it on both the left and right sides.

### --question--

#### --text--

给定以下代码，`.child` 将如何定位？

```css
.parent {
  /* No position property set */
  height: 200px;
}
.child {
  position: absolute;
  top: 10px;
}
```

#### --distractors--

It will be positioned 10px from the top of the `.parent` element, as `absolute` positioning is always relative to the direct parent.

---

It will remain in its default static position because the `absolute` value is invalid without a `z-index` property.

---

It will be positioned 10px from the top of the browser window, remaining fixed in place even when the user scrolls the page.

#### --answer--

It will be positioned 10px from the top of the initial containing block, such as the `<body>`, because its parent is not positioned.

### --question--

#### --text--

以下 CSS 对 `.box` 元素会有什么效果？

```css
.box {
  position: absolute;
  top: 50px;
  left: 50px;
}
```

#### --distractors--

The element will remain in its normal flow but will be indented by 50px from the top and left, pushing other elements away.

---

The element will be fixed to the viewport and will stay 50px from the top and 50px from the left, even when the page is scrolled.

---

The element will be positioned relative to its own starting point, moving 50px down and 50px to the right without leaving the document flow.

#### --answer--

The element will be taken out of the normal flow and placed 50px from the top and 50px from the left of its nearest positioned ancestor.

### --question--

#### --text--

以下哪个 [position](#) 值会将元素完全从文档的正常流中移除？

#### --distractors--

`position: static;`

---

`position: relative;`

---

`position: inherit;`

#### --answer--

`position: absolute;`

### --question--

#### --text--

给定一个 `.parent` 和一个 `.child` 元素，哪个 CSS 片段会正确地将 `.child` 定位在 `.parent` 元素的左上角 20px 处？

#### --distractors--

```css
.parent {
  /* position: static; by default */
}
.child {
  position: absolute;
  top: 20px;
  left: 20px;
}
```

---

```css
.parent {
  position: relative;
}
.child {
  position: relative;
  top: 20px;
  left: 20px;
}
```

---

```css
.parent {
  position: relative;
}
.child {
  float: left;
  top: 20px;
  left: 20px;
}
```

#### --answer--

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 20px;
  left: 20px;
}
```

### --question--

#### --text--

[static](#) 定位和 [relative](#) 定位有什么区别？

#### --distractors--

`static` positioning removes an element from the document flow, while `relative` positioning keeps it in the flow.

---

An element with `position: static;` can be offset with the `top` and `left` properties, while `position: relative;` cannot.

---

`static` positioning is for block-level elements, while `relative` positioning is only intended for inline elements.

#### --answer--

Both keep an element in the normal document flow, but `relative` allows the element to be offset from its original position.

### --question--

#### --text--

哪个 CSS 片段正确地将图像向左浮动，允许其他内容环绕它？

#### --distractors--

```css
.image {
  position: absolute;
  left: 0;
}
```

---

```css
.image {
  display: inline-block;
}
```

---

```css
.image {
  text-align: left;
}
```

#### --answer--

```css
.image {
  float: left;
}
```

### --question--

#### --text--

[absolute](#) 定位和 [fixed](#) 定位有什么区别？

#### --distractors--

`absolute` positioning is relative to the viewport, while `fixed` positioning is relative to the nearest positioned ancestor.

---

`absolute` positioning keeps the element in the normal document flow, while `fixed` positioning removes it from the flow.

---

Both are positioned relative to the viewport, but `fixed` elements will scroll with the page while `absolute` elements will not.

#### --answer--

`absolute` positioning is relative to the nearest positioned ancestor, while `fixed` positioning is relative to the browser viewport.

### --question--

#### --text--

哪个 [position](#) 值将元素放置在正常文档流中，并防止 [top](#) 和 [left](#) 等偏移属性产生任何效果？

#### --distractors--

`position: relative;`

---

`position: absolute;`

---

`position: fixed;`

#### --answer--

`position: static;`