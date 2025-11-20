---
id: 5dfb5ecbeacea3f48c6300b1
title: 步骤 23
challengeType: 0
dashedName: step-23
---

# --description--

`li` 元素用于在有序或无序列表中创建列表项�?

这是一个无序列表中列表项的示例�?

```html
<ul>
  <li>milk</li>
  <li>cheese</li>
</ul>
```

�?`ul` 元素中嵌套三个列表项来显示猫喜欢的三样东西：

`catnip`

`laser pointers`

`lasagna`

# --hints--

你应该有三个 `li` 元素�?每个 `li` 元素都应该有自己的开始和结束标签�?

```js
assert.lengthOf(document.querySelectorAll('li'), 3);
assert.lengthOf(code.match(/<\/li\>/g), 3);
```

你应该有三个 `li` 元素，可按任意顺序包含文�?`catnip`、`laser pointers` �?`lasagna`�?你要么遗漏了某些文本，要么拼写有误�?

```js
assert.deepStrictEqual(
  [...document.querySelectorAll('li')]
    .map((item) => item.innerText?.trim().replace(/\s+/g, ' ').toLowerCase())
    .sort((a, b) => a.localeCompare(b)),
  ['catnip', 'lasagna', 'laser pointers']
);
```

三个 `li` 元素应位�?`ul` 元素的开始和结束标签之间�?

```js
assert.lengthOf(
  [...document.querySelectorAll('li')].filter(
    (item) => item.parentNode.nodeName === 'UL'
  ), 3
);
```

# --seed--

## --seed-contents--

```html
<html>
  <body>
    <main>
      <h1>CatPhotoApp</h1>
      <section>
        <h2>Cat Photos</h2>
        <p>Everyone loves <a href="https://cdn.MasterPuti.org/curriculum/cat-photo-app/running-cats.jpg">cute cats</a> online!</p>
        <p>See more <a target="_blank" href="https://freecatphotoapp.com">cat photos</a> in our gallery.</p>
        <a href="https://freecatphotoapp.com"><img src="https://cdn.MasterPuti.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute orange cat lying on its back."></a>
      </section>
      <section>
        <h2>Cat Lists</h2>
        <h3>Things cats love:</h3>
--fcc-editable-region--
        <ul>

        </ul>
--fcc-editable-region--
      </section>
    </main>
  </body>
</html>
```

