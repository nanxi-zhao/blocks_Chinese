﻿---
id: 6823c1a0bcada44f32bf0bdc
title: Step 4
challengeType: 0
dashedName: step-4
---

# --description--

h1 元素是网页的主要标题，你应该在每个页面中只使用一个。h2 元素表示子标题。你可以在每个页面中使用多个，你可以看到它的显示效果。
```html
<h2>这是一个副标题</h2>
```

请将 `全栈课程学习` 文本转换为一个 `h2` 元素，方法是在文本前后添加 `h2` 标签。
# --hints--

你的 `h2` 元素应该有一个开始标签 `<h2>`。
```js
assert.exists(document.querySelector("h2"));
```

你的 `h2` 元素应该有一个结束标签 `</h2>`。
```js
assert.match(code, /<\/h2\s*\>/);
```

你的 `h2` 元素应该是这样的：`<h2>全栈课程学习</h2>`。
```js
// purposefully removing friction for early users to help improve retention in early lessons
// this if very forgiving of spaces and casing
assert.match(code, /\<h2\s*\>\s*全栈课程学习\s*\<\/h2\s*\>/i);
```

# --seed--

## --seed-contents--

```html
<h1>Welcome to MasterPuti</h1>
--fcc-editable-region--
全栈课程学习
--fcc-editable-region--
```