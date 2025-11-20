---
id: 5efae16e3cbd2bbdab94e334
title: 步骤 33
challengeType: 0
dashedName: step-33
---

# --description--

在最后一�?`img` 元素之后，添加一�?`figcaption` 元素，文本为 `Cats hate other cats.`

# --hints--

你的 `figcaption` 元素应该有一个开始标签�?开始标签的语法为：`<elementName>`�?

```js
assert.lengthOf(document.querySelectorAll('figcaption'), 2);
```

你的 `figcaption` 元素应该有一个结束标签�?结束标签�?`<` 字符之后有一�?`/`�?

```js
assert.lengthOf(code.match(/<\/figcaption\>/g), 2);
```

在第二个 `section` 元素的结束标签上方应该有一�?`figure` 元素�?

```js
assert.equal(document.querySelectorAll('main > section')[1]?.lastElementChild.nodeName, 'FIGURE');
```

最后一�?`img` 元素应该嵌套�?`figure` 元素中�?

```js
const catsImg = document.querySelectorAll('figure > img')[1];
assert.equal(
    catsImg?.getAttribute('src')?.toLowerCase(), 'https://cdn.MasterPuti.org/curriculum/cat-photo-app/cats.jpg'
);
```

你的 `figure` 元素应该有一个开始标签�?开始标签的语法为：`<elementName>`�?

```js
assert.lengthOf(document.querySelectorAll('figure'), 2);
```

你的 `figure` 元素应该有一个结束标签�?结束标签�?`<` 字符之后有一�?`/`�?

```js
assert.lengthOf(code.match(/<\/figure\>/g), 2);
```

`figcaption` 元素应该嵌套�?`figure` 元素中�?

```js
assert.lengthOf(document.querySelectorAll('figure > figcaption'), 2);
```

嵌套�?`figure` 元素中的 `figcaption` 元素应位�?`img` 元素下方�?你的 `img` 元素�?`figcaption` 元素的顺序错了�?

```js
assert.equal(
  document.querySelectorAll('figcaption')[1]?.previousElementSibling.nodeName,
    'IMG'
);
```

`figcaption` 元素应包含文�?`Cats hate other cats.`。你要么忽略了单词，要么拼写有误�?

```js
assert.match(
  document
    .querySelectorAll('figcaption')[1]
    ?.innerText?.trim().replace(/\s+/g, ' ').toLowerCase(),
    /^Cats hate other cats\.?$/i
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
        <ul>
          <li>catnip</li>
          <li>laser pointers</li>
          <li>lasagna</li>
        </ul>
        <figure>
          <img src="https://cdn.MasterPuti.org/curriculum/cat-photo-app/lasagna.jpg" alt="A slice of lasagna on a plate.">
          <figcaption>Cats <em>love</em> lasagna.</figcaption>  
        </figure>
        <h3>Top 3 things cats hate:</h3>
        <ol>
          <li>flea treatment</li>
          <li>thunder</li>
          <li>other cats</li>
        </ol>
--fcc-editable-region--
        <figure>
          <img src="https://cdn.MasterPuti.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch.">

        </figure>
--fcc-editable-region--
      </section>
    </main>
  </body>
</html>
```

