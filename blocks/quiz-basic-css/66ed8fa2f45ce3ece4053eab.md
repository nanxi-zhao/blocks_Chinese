---
id: 66ed8fa2f45ce3ece4053eab
title: CSS 基础知识测验
challengeType: 8
dashedName: quiz-basic-css
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

CSS 是什么的缩写？

#### --distractors--

Cascading Style Script

---

Concatenating Style Script

---

Castor Sage Style

#### --answer--

Cascading Style Sheets

### --question--

#### --text--

以下哪一个是正确的 CSS 规则？

#### --distractors--

`p=red`

---

`p (color: red)`

---

`{p color: red;}`

#### --answer--

`p {color: red;}`

### --question--

#### --text--

`<meta name="viewport">` 标签的作用是什么？

#### --distractors--

It links external stylesheets to a webpage for responsive design.

---

It specifies the metadata used by search engines to index a webpage.

---

It specifies the character encoding used on the webpage.

#### --answer--

It controls the shape and size of a web page on different screen sizes.

### --question--

#### --text--

使用内联 CSS 的正确语法是哪个？

#### --distractors--

`<p color =  blue></p>`

---

`<p><style = blue></p>`

---

`p {color: blue;}`

#### --answer--

`<p style="color: blue;"></p>`

### --question--

#### --text--

使用内部 CSS 时，`style` 元素应该放在 HTML 的哪个位置？

#### --distractors--

In the `meta` element.

---

In the `script` element.

---

In the `body` element.

#### --answer--

In the `head` element.

### --question--

#### --text--

设置宽度和高度的正确 CSS 规则是哪个？

#### --distractors--

`height-width: 50px;`

---

`width-and-height: 50px;`

---

`flex-width: 50px; flex-height: 50px;`

#### --answer--

`width: 50px; height: 50px;`

### --question--

#### --text--

哪个选择器能正确选中 `div` 内部的 `h1` 元素？

#### --distractors--

`div, h1 {}`

---

`div ~ h1 {}`

---

`div + h1 {}`

#### --answer--

`div h1 {}`

### --question--

#### --text--

哪个选择器能正确选中 `footer` 的直接子元素？

#### --distractors--

`footer ~ ul {}`

---

`footer + ul {}`

---

`footer ul {}`

#### --answer--

`footer > ul {}`

### --question--

#### --text--

哪个选择器能正确选中 `img` 元素的下一个兄弟元素？

#### --distractors--

`img h1 {}`

---

`img > h1 {}`

---

`img ~ h1 {}`

#### --answer--

`img + h1 {}`

### --question--

#### --text--

哪个选择器能正确选中由 `img` 元素前置的所有兄弟元素？

#### --distractors--

`img > caption {}`

---

`img caption {}`

---

`img + caption {}`

#### --answer--

`img ~ caption {}`

### --question--

#### --text--

关于块级元素，以下哪个陈述是正确的？

#### --distractors--

Block-level elements stack horizontally by default.

---

`width` and `height` properties usually do not apply to block-level elements unless you set their `display` property to `inline-block`.

---

Block-level elements cannot contain inline elements inside them.

#### --answer--

Block-level elements start on a new line and take up the full width of their container.

### --question--

#### --text--

使用 `inline-block` 值时，以下哪个陈述是正确的？

#### --distractors--

Elements stack vertically, always taking up the full width of their container.

---

Elements align horizontally but cannot apply vertical padding or margin.

---

Elements respect width and height settings but cannot contain other elements inside them.

#### --answer--

Elements retain inline flow but allow setting width and height.

### --question--

#### --text--

给定以下选择器，哪个具有最高的特异性？

#### --distractors--

`div`

---

`h1`

---

`p`

#### --answer--

`#id`

### --question--

#### --text--

给定以下选择器，哪个具有最低的特异性？

#### --distractors--

`#id`

---

`.class`

---

`div h1`

#### --answer--

`h1`

### --question--

#### --text--

`*` 选择器的作用是什么？

#### --distractors--

Targets some elements on the page.

---

Targets elements that have children on the page.

---

Targets all `p` elements on the page.

#### --answer--

Targets all elements on the page.

### --question--

#### --text--

CSS 中的 `!important` 有什么作用？

#### --distractors--

It makes the CSS rule work exclusively for inline styles and ignores styles defined in external or internal stylesheets.

---

It disables all other CSS properties applied to the same element, effectively making it the only rule that affects the element's styling.

---

It applies on to a certain selector or group of elements.

#### --answer--

It overrides any other values applied to the property for that selector.

### --question--

#### --text--

CSS 层叠算法是如何工作的？

#### --distractors--

It determines styles of the element based on order of declaration, regardless of other factors.

---

It applies styles based solely on the order they are written, ignoring specificity.

---

It applies styles prioritizing specificity, ignoring origin and relevance.

#### --answer--

It determines styles of the element based on specificity and order of declaration.

### --question--

#### --text--

哪条规则会在所有边应用 `32px` 的外边距？

#### --distractors--

`margin-top: 32px;`

---

`margin: 32px 0;`

---

`margin: 0 32px;`

#### --answer--

`margin: 32px;`

### --question--

#### --text--

哪条规则会在顶部和底部应用 `24px` 的内边距？

#### --distractors--

`padding: 24px;`

---

`padding-top-bottom: 24px;`

---

`padding: 0 24px;`

#### --answer--

`padding: 24px 0;`

### --question--

#### --text--

对于 `padding: 10px 20px 30px 40px`，值的正确顺序是什么？

#### --distractors--

Right, Top, Left, Bottom.

---

Top, Left, Bottom, Right.

---

Top, Bottom, Right, Left.

#### --answer--

Top, Right, Bottom, Left.

## --quiz--

### --question--

#### --text--

CSS 规则的主要组成部分是什么？

#### --distractors--

Elements and attributes

---

Style and sheets

---

Scripts and values

#### --answer--

Selectors and declaration blocks

### --question--

#### --text--

以下哪一个是 CSS 规则的正确语法？

#### --distractors--

```css
body [
  font-family: Arial;
]
```

---

```css
font-family {
  body: Arial;
}
```

---

```css
body {
  font-family; Arial:
}
```

#### --answer--

```css
body {
  font-family: Arial;
}
```

### --question--

#### --text--

什么是浏览器默认样式？

#### --distractors--

HTML elements that have the same styling properties regardless of the browser.

---

They are mandatory styles that you must use for specific HTML elements.

---

They are the color themes for the various browsers.

#### --answer--

The CSS rules that browsers apply automatically.

### --question--

#### --text--

`width` 属性的默认值是什么？

#### --distractors--

`none`

---

`0`

---

`100%`

#### --answer--

`auto`

### --question--

#### --text--

`min-height` 属性指定了什么？

#### --distractors--

The starting height for an element.

---

The height for an element.

---

The maximum height for an element.

#### --answer--

The minimum height for an element.

### --question--

#### --text--

以下关于通用选择器 `*` 的陈述哪个是正确的？

#### --distractors--

It has the highest specificity because it can style all the elements on a page.

---

It contributes 1 to all parts of the specificity value.

---

It cannot reset styles across different browsers.

#### --answer--

It has the lowest specificity value of any selector.

### --question--

#### --text--

哪个选择器能正确选中有序列表的 `li` 元素？

#### --distractors--

`li {}`

---

`ul li {}`

---

`ol + li {}`

#### --answer--

`ol li {}`

### --question--

#### --text--

哪个选择器能选中 `div` 元素的段落元素？

#### --distractors--

`p div {}`

---

`div, p {}`

---

`p, div {}`

#### --answer--

`div p {}`

### --question--

#### --text--

`margin` 属性在哪里应用样式？

#### --distractors--

The space inside element.

---

Between the content and the border.

---

On the border of the element.

#### --answer--

The space outside the element.

### --question--

#### --text--

`padding` 属性在哪里应用样式？

#### --distractors--

Between the elements border and the surrounding elements.

---

The space outside the element.

---

On the border of the element.

#### --answer--

The space inside the element.

### --question--

#### --text--

关于块级元素，以下哪个陈述是错误的？

#### --distractors--

They can stretch to fit the width of their container.

---

Common block level elements include `div`, `paragraph`, and `section`.

---

Block-level elements start on a new line and take up the full width of their container.

#### --answer--

They cannot take up the full width available as they are blocked from doing so.

### --question--

#### --text--

使用 `inline-block` 值时，以下哪个陈述是错误的？

#### --distractors--

`inline-block` elements behave like inline elements.

---

They can have `width` and `height` properties.

---

Elements retain inline flow but allow setting `width` and `height`.

#### --answer--

They do not share properties with inline or block level elements.

### --question--

#### --text--

关于 `!important` 关键字，以下哪个陈述是正确的？

#### --distractors--

They are used to make comments for an important CSS property.

---

They make sure a CSS property has the correct syntax.

---

They make CSS rules easier to maintain.

#### --answer--

They override the specificity of other selectors.

### --question--

#### --text--

类选择器名称前面是什么字符？

#### --distractors--

`#`

---

`$`

---

`*`

#### --answer--

`.`

### --question--

#### --text--

关于内联级元素，以下哪个陈述是错误的？

#### --distractors--

They take up only as much space as they need.

---

They do not start on a new line.

---

Common inline elements include `span` and `img`.

#### --answer--

They always start on a new line.

### --question--

#### --text--

内部 CSS 样式在哪里访问？

#### --distractors--

They are styles that are important to the project, so are not shared externally.

---

Since they form the core styling of the project, they are saved in the `styles.css` file so other web pages can access them.

---

They are stored inside the `body` element when there is only one web page to style.

#### --answer--

They are written within the `style` section within the `head` element.

### --question--

#### --text--

使用简写语法时，`padding` 属性的应用顺序是什么？

#### --distractors--

`top`, `bottom`, `left`, `right`

---

`left`, `right`, `top`, `bottom`

---

`right`, `top`, `left`, `bottom`

#### --answer--

`top`, `right`, `bottom`, `left`

### --question--

#### --text--

使用简写语法时，`margin` 属性的应用顺序是什么？

#### --distractors--

`left`, `right`, `top`, `bottom`

---

`right`, `top`, `left`, `bottom`

---

`top`, `bottom`, `left`, `right`

#### --answer--

`top`, `right`, `bottom`, `left`

### --question--

#### --text--

内联 CSS 样式是用来做什么的？

#### --distractors--

They are used to style inline elements only.

---

They are used to style elements only when they all appear on the same line of the browser viewport.

---

They are used to resolve the issue with separation of concerns.

#### --answer--

They are used to directly style within the element, instead of using internal or external CSS.

### --question--

#### --text--

ID 选择器前面是什么符号？

#### --distractors--

`.`

---

`*`

---

`$`

#### --answer--

`#`