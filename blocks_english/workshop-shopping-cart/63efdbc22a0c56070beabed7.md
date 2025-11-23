---
id: 63efdbc22a0c56070beabed7
title: 步骤 23
challengeType: 0
dashedName: step-23
---

# --description--

现在你需要为每个商品添加一个唯一的标识符，这样你就可以在购物车中跟踪它们。给每个 `.product` 元素添加一个 `data-id` 属性，值分别为 `1`、`2` 和 `3`。

# --hints--

第一个 `.product` 元素应该有一个 `data-id` 属性，值为 `1`。

```js
assert.equal(document.querySelectorAll('.product')[0]?.dataset.id, '1');
```

第二个 `.product` 元素应该有一个 `data-id` 属性，值为 `2`。

```js
assert.equal(document.querySelectorAll('.product')[1]?.dataset.id, '2');
```

第三个 `.product` 元素应该有一个 `data-id` 属性，值为 `3`。

```js
assert.equal(document.querySelectorAll('.product')[2]?.dataset.id, '3');
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
          --fcc-editable-region--
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
            <p>$0.89</p>
            <button>添加到购物车</button>
          </div>
          --fcc-editable-region--
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