---
id: 618a0b2befb143baefab632b
title: 第 32 步
challengeType: 0
dashedName: step-32
---

# --description--

请注意红色和青色在彼此旁边时非常明亮。如果在网站上过度使用这种对比会让人分心，并且如果将文字放在互补色背景上会使文字难以阅读。

更好的做法是选择一种颜色作为主色，并使用其互补色作为强调色来吸引人们对页面上某些内容的注意。

首先，在 [h1](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616968c2c94c8071b349c146.md#L57-L57) 规则中，使用 [rgb](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/617b65579ce424bf5f02ca73.md#L57-L57) 函数将其 [background-color](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d4a84b756d9c4b8255093.md#L57-L57) 设置为青色。

# --hints--

你不应该删除或修改 [text-align](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616968c2c94c8071b349c146.md#L57-L57) 属性及其值。

```js
assert.strictEqual(new __helpers.CSSHelp(document).getStyle('h1')?.textAlign, 'center');
```

你的 [h1](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616968c2c94c8071b349c146.md#L57-L57) CSS 规则应该有一个 [background-color](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d4a84b756d9c4b8255093.md#L57-L57) 属性，设置为 [rgb(0, 255, 255)](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/617bb77353188166af43f3ac.md#L57-L57)。

```js
assert.strictEqual(new __helpers.CSSHelp(document).getStyle('h1')?.backgroundColor, 'rgb(0, 255, 255)');
```

# --seed--

## --seed-contents--

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container">
      <div class="marker one">
      </div>
      <div class="marker two">
      </div>
      <div class="marker three">
      </div>
    </div>
  </body>
</html>
```

```css
--fcc-editable-region--
h1 {
  text-align: center;
  background-color: rgb(0, 255, 255);
}
--fcc-editable-region--

.container {
  background-color: rgb(255, 255, 255);
  padding: 10px 0;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: rgb(0, 255, 255);
}

.three {
  background-color: rgb(0, 0, 0);
}

```