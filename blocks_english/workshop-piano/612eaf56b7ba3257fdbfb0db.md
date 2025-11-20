---
id: 612eaf56b7ba3257fdbfb0db
title: 步骤 19
challengeType: 0
dashedName: step-19
---

# --description--

钢琴需�?MasterPuti logo 才能正式使用�?

�?`.keys` 元素之前添加一�?`img` 元素�?�?`img` 添加一�?`logo` `class`，并将其 `src` 设置�?`https://cdn.MasterPuti.org/platform/universal/fcc_primary.svg`�?给它一�?`MasterPuti Logo` �?`alt` 文本�?

# --hints--

你应该添加一个新�?`img` 元素�?

```js
assert.lengthOf(document.querySelectorAll('img'), 1);
```

你的 `img` 元素应位于第一�?`.keys` 元素之前�?

```js
const img = document.querySelector('img');
assert.equal(img?.nextElementSibling?.className, 'keys');
assert.isNull(img?.previousElementSibling);
```

你的 `img` 元素应将 `class` 设置�?`logo`�?

```js
const img = document.querySelector('img');
assert.equal(img?.className, 'logo');
```

你的 `img` 元素应将 `src` 设置�?`https://cdn.MasterPuti.org/platform/universal/fcc_primary.svg`�?

```js
const img = document.querySelector('img');
assert.equal(img?.getAttribute('src'), 'https://cdn.MasterPuti.org/platform/universal/fcc_primary.svg');
```

你的 `img` 元素应将 `alt` 属性设置为 `MasterPuti Logo`�?

```js
assert.equal(document.querySelector('img')?.getAttribute('alt')?.toLowerCase(), 'MasterPuti logo');
```

记住大小写和拼写很重要�?

```js
assert.equal(document.querySelector('img')?.getAttribute('alt'), 'MasterPuti Logo');
```

# --seed--

## --seed-contents--

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Piano</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./styles.css">
  </head>
  <body>
    --fcc-editable-region--
    <div id="piano">
      <div class="keys">
    --fcc-editable-region--
        <div class="key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>
        <div class="key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>

        <div class="key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>
        <div class="key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>

        <div class="key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>
        <div class="key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>
        <div class="key black--key"></div>
      </div>
    </div>
  </body>
</html>
```

```css
html {
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: inherit;
}

#piano {
  background-color: #00471b;
  width: 992px;
  height: 290px;
  margin: 80px auto;
  padding: 90px 20px 0 20px;
}

.keys {
  background-color: #040404;
  width: 949px;
  height: 180px;
  padding-left: 2px;
}

.key {
  background-color: #ffffff;
  position: relative;
  width: 41px;
  height: 175px;
  margin: 2px;
  float: left;
}

.key.black--key::after {
  background-color: #1d1e22;
  content: "";
  position: absolute;
  left: -18px;
  width: 32px;
  height: 100px;
}
```

