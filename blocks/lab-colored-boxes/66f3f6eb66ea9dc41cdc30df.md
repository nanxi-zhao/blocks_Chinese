---
id: 66f3f6eb66ea9dc41cdc30df
title: Design a Set of Colored Boxes
challengeType: 25
dashedName: set-of-colored-boxes
demoType: onClick
---

# --description--

在这个练习中，你将通过设计一组彩色盒子来练习 CSS 颜色的使用。

**目标：**实现下面的用户需求并通过所有测试，完成本练习。

**用户需求：**

1. 请将 `body` 的背景色设置为 `#f4f4f4`。
2. 页面应包含一个 class 为 `color-grid` 的 `div`，用于容纳所有颜色盒子。
3. `.color-grid` 内应包含五个 `div` 元素。
4. 这五个 `div` 分别应有 `color-box` 和 `color#` 两个类名，其中 `#` 表示该 `div` 的顺序编号（例如第一个为 `color1`，第二个为 `color2`，依此类推）。
5. `.color-box` 类应设置固定的 `width` 和 `height`，以便盒子在页面上可见。
6. `.color1` 的 `background-color` 应使用十六进制颜色值。
7. `.color2` 的 `background-color` 应使用 RGB 颜色值。
8. `.color3` 的 `background-color` 应使用预定义颜色名（单词）。
9. `.color4` 的 `background-color` 应使用 HSL 颜色值。
10. `.color5` 的 `background-color` 应被设置为任意颜色。

**注意：** 请确保在 HTML 中正确链接你的样式表并应用 CSS。

# --hints--

下面是一些小提示，帮助你实现要求：

`body` 的背景色应为 `#f4f4f4`。

```js
const body = document.body;
const bodyBgColor = getComputedStyle(body).backgroundColor;
assert.strictEqual(bodyBgColor, 'rgb(244, 244, 244)');
```

页面应包含一个 `class="color-grid"` 的 `div`。

```js
const colorGrid = document.querySelector('div.color-grid');
assert.exists(colorGrid);
```

`.color-grid` 内应有五个 `div`。

```js
const colorGridChildren = document.querySelectorAll('div.color-grid > div');
assert.strictEqual(colorGridChildren.length, 5);
```

每个盒子应同时拥有 `color-box` 和 `color#`（按顺序编号）两个类名。

```js
const colorGridChildren = document.querySelectorAll('div.color-grid > div');
assert.strictEqual(colorGridChildren.length, 5);

colorGridChildren.forEach((child, index) => {
    const colorClass = `color${index + 1}`;
    assert.isTrue(child.classList.contains('color-box'));
    assert.isTrue(child.classList.contains(colorClass));
});
```

`.color-box` 应设置可见的宽高。

```js
const colorBox = document.querySelector('.color-box');
assert.exists(colorBox);

const colorBoxStyles = getComputedStyle(colorBox);
const width = colorBoxStyles.width;
const height = colorBoxStyles.height;

assert.notStrictEqual(width, '0px');
assert.notStrictEqual(height, '0px');
```

`.color1` 请使用十六进制颜色值。

```js
const hexChars = "[0-9a-fA-F]"
const hexRegex = new RegExp(`\\.color1\\s*{[^}]*\\bbackground-color\\s*:\\s*#((${hexChars}{3,4})||(${hexChars}{6})||(${hexChars}{8}))\\s*;?[^}]*}`);
assert.match(__helpers.removeCssComments(code), hexRegex);
```

`.color2` 请使用 RGB 背景颜色。

```js
assert.match(__helpers.removeCssComments(code), /\.color2\s*{[^}]*\bbackground-color\s*:\s*rgb\s*\(\s*\d+(?:\.\d+)?\s*(,|\s+)\s*\d+(?:\.\d+)?\s*\1\s*\d+(?:\.\d+)?\s*(\/\s*\d{1,2}(?:\.\d+)?%\s*)?\)\s*;?[^}]*}/);
```

`.color3` 请使用预定义的颜色名（单词）。

```js
const colorSet = new Set(["black", "silver", "gray", "white", "maroon", "red", "purple", "fuchsia", "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua", "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "aqua", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "gray", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "fuchsia", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "rebeccapurple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "transparent", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]);
const matchedColor = __helpers.removeCssComments(code).match(/\.color3\s*{[^}]*\bbackground-color\s*:\s*(?<color>[a-zA-Z]+)\s*;?[^}]*}/);
assert.isTrue(colorSet.has(matchedColor.groups.color.toLowerCase()));
```

`.color4` 请使用 HSL 颜色值。

```js
const absHSLVals = '\\s*(none|\\d+(?:\\.\\d+)?(?:deg)?)\\s*\\d+(?:\\.\\d+)?%?\\s*\\d+(?:\\.\\d+)?%?\\s*(\\/\\s*\\d{1,2}(?:\\.\\d+)?%\\s*)?';
const legacyHSLVals = '\\s*\\d+(?:\\.\\d+)?(?:deg)?\\s*,\\s*\\d+(?:\\.\\d+)?%\\s*,\\s*\\d+(?:\\.\\d+)?%\\s*(?:,\\s*\\d+(?:\\.\\d+)?\\s*)?';
const hslRegex = new RegExp(`\\.color4\\s*{[^}]*\\bbackground-color\\s*:\\s*hsl\\s*\\((${absHSLVals}|${legacyHSLVals})\\)\\s*;?[^}]*}`);
assert.match(__helpers.removeCssComments(code), hslRegex);
```

`.color5` 应设置背景颜色。

```js
assert.isNotEmpty(new __helpers.CSSHelp(document).getStyle('.color5')?.getPropVal('background-color', true));
```

# --seed--

## --seed-contents--

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Boxes</title>
</head>
<body>

</body>
</html>
```

```css

```

# --solutions--

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Boxes</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Colored Boxes</h1>
    <div class="color-grid"> 
        <div class="color-box color1"></div>
        <div class="color-box color2"></div>
        <div class="color-box color3"></div>
        <div class="color-box color4"></div>
        <div class="color-box color5"></div>
    </div>
</body>
</html>
```

```css
body {
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    margin-bottom: 20px;
}

.color-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 10px;
    width: 100%;
    max-width: 800px;
}

.color-box {
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    border-radius: 8px;
    text-align: center;
    width: 100px;
    height: 100px;
}

.color1 {
    background-color: #33FF57;
}

.color2 {
    background-color: rgb(128,0,128);
}

.color3 {
    background-color: orange;
}

.color4 {
    background-color: hsl(59, 61%, 26%);
}

.color5 {
    background-color: red;
}