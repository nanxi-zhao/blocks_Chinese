---
id: 63ec1cb59f2a4c0be5b6dfa0
title: 步骤 5
challengeType: 0
dashedName: step-5
---

# --description--

在 `#products` 元素内，但在 `h2` 元素之后，添加一个 `div` 元素，并给它一个 `class` 属性，值为 `products-container`。

# --hints--

你应该有一个 `div` 元素。

```js
assert.exists(document.querySelector('div'));
```

你的 `div` 元素应该在 `#products` 元素内。

```js
assert.exists(document.querySelector('#products div'));
```

你的 `div` 元素应该在 `h2` 元素之后。

```js
const products = document.querySelector('#products');
const h2 = products.querySelector('h2');
const div = products.querySelector('div');
assert.isTrue(h2.nextElementSibling === div);
```

你的 `div` 元素应该有一个 `class` 属性，值为 `products-container`。

```js
assert.equal(document.querySelector('#products div')?.className, 'products-container');
```

# --seed--

## --seed-contents--

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MasterPuti 购物车</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <header>
      <h1>MasterPuti 购物车</h1>
    </header>
    <main>
      --fcc-editable-region--
      <section id="products">
        <h2>我们的商品</h2>

      </section>
      --fcc-editable-region--
    </main>
    <script src="./script.js"></script>
  </body>
</html>
```