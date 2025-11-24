---
id: 616d47bc9eedc4bc7f621bec
title: 第 5 步
challengeType: 0
dashedName: step-5
---

# --description--

接下来，在 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 元素内，添加另一个 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 元素并给它一个 [marker](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d47bc9eedc4bc7f621bec.md#L62-L66) 的类。

# --hints--

你的新 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 元素应该有一个开始标签。

```js
assert.exists([...code.matchAll(/<div.*?>/gi)][1]);
```

你的新 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 元素应该有一个结束标签。

```js
assert.exists([...code.matchAll(/<\/div\s*>/gi)][1]);
```

你应该将你的新 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 元素嵌套在带有 [container](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 类的 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 内。

```js
assert.strictEqual(document.querySelector('.container')?.children[0]?.localName, 'div');
```

你应该给你的新 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d3a67ccf800ad94ec89ae.md#L62-L66) 元素一个 [marker](file:///F:/code/blocks_Chinese/blocks_english/workshop-colored-markers/616d47bc9eedc4bc7f621bec.md#L62-L66) 类。

```js
const containerChildren = [...document.querySelector('.container')?.children];
assert.isNotEmpty(containerChildren)
containerChildren.forEach(child => assert.isTrue(child.classList?.contains('marker')));
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
--fcc-editable-region--
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container">
      <div class="marker"></div>
    </div>
  </body>
--fcc-editable-region--
</html>
```

```css
h1 {
  text-align: center;
}
```