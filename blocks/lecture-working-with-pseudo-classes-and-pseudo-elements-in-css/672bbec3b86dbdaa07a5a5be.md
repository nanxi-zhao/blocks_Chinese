---
id: 672bbec3b86dbdaa07a5a5be
title: 功能性伪类的示例有哪些？
challengeType: 19
dashedName: what-are-examples-of-functional-pseudo-classes
---

# --interactive--

功能性伪类允许您基于更复杂的条件或关系来选择元素。与基于状态（例如[:hover]、[:focus]）定位元素的常规伪类不同，功能性伪类在括号内接受参数，因此得名"功能性伪类"。

功能性伪类的示例包括：

- [:is()]
- [:where()]
- [:has()]
- [:not()]

让我们更深入地了解这些功能性伪类的每一个，并附上示例。

[:is()]伪类在您想要为具有一些但不是所有特征的元素组设置样式时很有用。例如，您可能想要为网站上的不同类型按钮设置样式，包括[button]元素、样式为按钮的链接以及类型为[submit]和[reset]的[input]元素。这是一个代表该情况的示例。没有[:is()]函数，您将不得不编写像这样的复杂选择器：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<button>示例按钮</button>
<a href="#" class="button">链接样式为按钮</a>
<input type="submit" value="提交" />
<input type="reset" value="重置" />
```

```css
button,
a.button,
input[type='submit'],
input[type='reset'] {
  background-color: darkblue;
  color: white;
  border: 1px solid darkblue;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
  display: inline-block;
  margin: 5px;
  font-size: 16px;
  text-align: center;
}

button:hover,
a.button:hover,
input[type='submit']:hover,
input[type='reset']:hover {
  background-color: blue;
  border-color: blue;
}
```

:::

使用[:is()]函数，您可以编写更紧凑且易于理解的选择器，如下所示：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<button>示例按钮</button>
<a href="#" class="button">链接样式为按钮</a>
<input type="submit" value="提交" />
<input type="reset" value="重置" />
```

```css
:is(button, a.button, input[type='submit'], input[type='reset']) {
  background-color: darkblue;
  color: white;
  border: 1px solid darkblue;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
  display: inline-block;
  margin: 5px;
  font-size: 16px;
  text-align: center;
}

:is(button, a.button, input[type='submit'], input[type='reset']):hover {
  background-color: blue;
  border-color: blue;
}
```

:::

[:where()]伪类的功能类似于[:is()]，但它不会增加选择器的特异性。这使得它非常适合应用样式而不影响其他规则的特异性。

例如，您可以使用[:where()]函数将标题元素的[margin]和[padding]设置为零。这确保重置不会干扰您稍后可能应用的更具体样式。这是一个示例：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<h1>页面标题</h1>
<h2>副标题</h2>
<h3>要点</h3>

<p>示例段落。</p>
<p>示例段落。</p>
<p>示例段落。</p>
```

```css
:where(h1, h2, h3) {
  margin: 0;
  padding: 0;
}
```

:::

在引入[:has()]伪类之前，基于子元素状态为父元素设置样式是很具挑战性的。它允许您根据子元素的存在或状态为父元素应用样式。

例如，下面的CSS将仅应用于包含[h2]的任何[article]元素：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<article>
  <h2>副标题</h2>
  <p>Lorem ipsum dolor sit amet.</p>
</article>

<article>
  <h3>要点</h3>
  <p>Lorem ipsum dolor sit amet.</p>
  <p>Lorem ipsum dolor sit amet.</p>
</article>
```

```css
article:has(h2) {
  border: 2px solid hotpink;
}
```

:::

[:not()]伪类非常适合您想要为一组元素应用样式但排除一个或多个特定例外的情况。在下面的CSS中，任何不是主要按钮的按钮都将具有灰色背景：

:::interactive_editor

```html
<link rel="stylesheet" href="styles.css" />
<button class="primary">主要按钮</button>
<button class="secondary">次要按钮</button>
<button class="danger">另一个次要按钮</button>
```

```css
button {
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  border: none;
  color: white;
}

button.primary {
  background-color: deepskyblue;
}

button:not(.primary) {
  background-color: grey;
}
```

:::

# --questions--

## --text--

哪个伪类的工作方式类似于[:is()]，但不会向您的选择器添加任何特异性？

## --answers--

[:not()]

### --feedback--

这个伪类非常适合应用广泛且非侵入性的样式。

---

[:has()]

### --feedback--

这个伪类非常适合应用广泛且非侵入性的样式。

---

[:where()]

---

[:empty]

### --feedback--

这个伪类非常适合应用广泛且非侵入性的样式。

## --video-solution--

3

## --text--

以下哪项不是功能性伪类？

## --answers--

[:is()]

### --feedback--

功能性伪类使用括号并在其中接受参数。

---

[:first-child]

### --feedback--

功能性伪类使用括号并在其中接受参数。

---

[:has()]

### --feedback--

功能性伪类使用括号并在其中接受参数。

---

[:where()]

### --feedback--

功能性伪类使用括号并在其中接受参数。

## --video-solution--

2

## --text--

哪个伪类非常适合您想要为一组元素应用样式但有一两个例外的情况？

## --answers--

[:has()]

### --feedback--

考虑如何从样式中排除特定元素。

---

[:is()]

### --feedback--

考虑如何从样式中排除特定元素。

---

[:not()]

---

[:where()]

### --feedback--

考虑如何从样式中排除特定元素。

## --video-solution--

3