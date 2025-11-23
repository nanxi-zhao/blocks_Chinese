---
id: 63eedebb0ec0231ff1cede1a
title: 步骤 22
challengeType: 0
dashedName: step-22
---

# --description--

在新的 `.product` 元素内，但在 `p` 元素之后，添加一个 `button` 元素，文本为 `添加到购物车`。

# --hints--

你应该在新的 `.product` 元素内有一个 `button` 元素。

```js
assert.exists(document.querySelectorAll('.product')[2]?.querySelector('button'));
```

你的 `button` 元素应该在 `p` 元素之后。

```js
const product = document.querySelectorAll('.product')[2];
const p = product.querySelector('p');
const button = product.querySelector('button');
assert.isTrue(p.nextElementSibling === button);
```

你的 `button` 元素应该有文本 `添加到购物车`。

```js
assert.equal(document.querySelectorAll('.product')[2]?.querySelector('button')?.textContent, '添加到购物车');
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
      <section id="products">
        <h2>我们的商品</h2>
        <div class="products-container">
          <div class="product">
            <h3>西瓜</h3>
            <p>$12.99</p>
            <button>添加到购物车</button>
          </div>
          <div class="product">
            <h3>香蕉</h3>
            <p>$0.99</p>
            <button>添加到购物车</button>
          </div>
          <div class="product">
            <h3>橙子</h3>
            --fcc-editable-region--
            <p>$0.89</p>

            --fcc-editable-region--
          </div>
        </div>
      </section>
      <section id="cart">
        <h2>购物车</h2>
        <div class="cart-items"></div>
        <div class="cart-total">
          <h3>总计: $0</h3>
        </div>
      </section>
    </main>
    <script src="./script.js"></script>
  </body>
</html>
```