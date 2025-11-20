---
id: 5efada803cbd2bbdab94e332
title: 步骤 31
challengeType: 0
dashedName: step-31
---

# --description--

在你刚刚添加�?`figure` 元素中，嵌套一�?`img` 元素�?`src` 属性设置为 `https://cdn.MasterPuti.org/curriculum/cat-photo-app/cats.jpg`�?

# --hints--

你的第二�?`figure` 元素应该有一个开始标签�?开始标签的语法为：`<elementName>`�?

```js
assert.isAtLeast(document.querySelectorAll('figure').length, 2);
```

你的第二�?`figure` 元素应该有一个结束标签�?结束标签�?`<` 字符之后有一�?`/`�?

```js
assert.isAtLeast(code.match(/<\/figure>/g)?.length, 2);
```

在第二个 `section` 元素的结束标签上方应该有一�?`figure` 元素�?你把它们的顺序写错了�?

```js
assert.equal(document.querySelectorAll('main > section')[1]?.lastElementChild.nodeName, 'FIGURE');
```

你应该在 `figure` 元素中嵌套第三个 `img` 元素�?

```js
const catsImg = document.querySelectorAll('figure > img')[1];
assert.exists(
  catsImg
);
```

第三张图像应该有一个设置为 `https://cdn.MasterPuti.org/curriculum/cat-photo-app/cats.jpg` �?`src` 属性�?

```js
const catsImg = document.querySelectorAll('figure > img')[1];
assert.equal(
    catsImg?.getAttribute('src')?.toLowerCase(), 'https://cdn.MasterPuti.org/curriculum/cat-photo-app/cats.jpg'
);
```

虽然你已将新图像�?`src` 设置为正确的 URL，但建议始终将属性的值用引号括起来�?

```js
assert.notMatch(code, /\<img\s+.+\s+src\s*=\s*https:\/\/cdn\.MasterPuti\.org\/curriculum\/cat-photo-app\/cats\.jpg/);
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

        </figure>
--fcc-editable-region--
      </section>
    </main>
  </body>
</html>
```

