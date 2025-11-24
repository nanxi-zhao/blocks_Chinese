---
id: 66f1aeb60b11aec5abe83c2e
title: CSS 库和框架测验
challengeType: 8
dashedName: quiz-css-libraries-and-frameworks
---

# --description--

要通过测验，你必须正确回答以下 10 道题中的至少 9 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

什么是 CSS 框架？

#### --distractors--

A tool to fix CSS errors.

---

A tool to lint CSS files.

---

A formatter for CSS files.

#### --answer--

A library for CSS styles.

### --question--

#### --text--

以下哪个是流行的实用优先 CSS 框架？

#### --distractors--

Template CSS

---

Loading CSS

---

Minimal CSS

#### --answer--

Tailwind CSS

### --question--

#### --text--

CSS 框架的缺点是什么？

#### --distractors--

Too few components.

---

No customization options.

---

Improved browser support.

#### --answer--

Can bloat CSS files.

### --question--

#### --text--

SCSS 代表什么？

#### --distractors--

Super Cascading Style Sheets.

---

Structured CSS.

---

Simple CSS.

#### --answer--

Sassy CSS.

### --question--

#### --text--

以下哪个是 Sass 的特性？

#### --distractors--

Comments

---

CSS linting.

---

Inline CSS.

#### --answer--

Mixins

### --question--

#### --text--

以下哪个是在 Tailwind CSS 中使用实用类的正确方法？

#### --distractors--

```html
<button class="color-blue text-color font-size allow-hover round-btn">
  Button
</button>
```

---

```html
<button class="blue text font-size hover round-btn margin-full">
  Button
</button>
```

---

```html
<button class="set-blue set-text set-font set-hover round-btn padding-full">
  Button
</button>
```

#### --answer--

```html
<button class="bg-blue-500 text-white font-bold py-2 px-4 rounded-full hover:bg-blue-700">
  Button
</button>
```

### --question--

#### --text--

CSS 框架有哪两种类型？

#### --distractors--

Tablet first CSS frameworks and Component-based CSS frameworks.

---

Utility-first CSS frameworks and Lazy loading CSS frameworks.

---

Minimal CSS frameworks and Utility-first CSS frameworks.

#### --answer--

Utility-first CSS frameworks and Component-based CSS frameworks.

### --question--

#### --text--

SCSS 的文件扩展名是什么？

#### --distractors--

`.sass`

---

`.scsss`

---

`.css`

#### --answer--

`.scss`

### --question--

#### --text--

以下哪个是在 SCSS 中定义变量的正确方法？

#### --distractors--

```css
#primary-color: #3498eb;

header {
  background-color: #primary-color;
}
```

---

```css
>primary-color: #3498eb;

header {
  background-color: >primary-color;
}
```

---

```css
?primary-color: #3498eb;

header {
  background-color: ?primary-color;
}
```

#### --answer--

```css
$primary-color: #3498eb;

header {
  background-color: $primary-color;
}
```

### --question--

#### --text--

以下哪个是定义 mixin 的正确方法？

#### --distractors--

```css
--mixin center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

```css
>mixin center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

```css
mixin center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

#### --answer--

```css
@mixin center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}
```