---
id: 68ec6e8d0caee3afaaf142ef
title: 第 5 步
challengeType: 0
dashedName: step-5
---

# --description--

在具有 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 为 [card-container](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 的元素内，创建另一个 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68e97fe79367ad7b5dd6c9cd.md#L58-L58) 元素。这个 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68e97fe79367ad7b5dd6c9cd.md#L58-L58) 将代表第一张书籍卡片。

为这个新的 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68e97fe79367ad7b5dd6c9cd.md#L58-L58) 元素添加一个 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 属性，并将 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 属性的值设置为 [card](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6e8d0caee3afaaf142ef.md#L58-L58)。

# --hints--

你应该有一个 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68e97fe79367ad7b5dd6c9cd.md#L58-L58) 元素嵌套在具有 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 为 [card-container](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 的元素内。

```js
assert.exists(document.querySelector('.card-container div'));
```

你的新 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68e97fe79367ad7b5dd6c9cd.md#L58-L58) 元素应该有一个 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 属性。

```js
assert.isTrue(document.querySelector('.card-container div')?.hasAttribute('class'));
```

你的新 [div](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68e97fe79367ad7b5dd6c9cd.md#L58-L58) 元素应该有一个 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 具有值 [card](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6e8d0caee3afaaf142ef.md#L58-L58)。

```js
assert.exists(document.querySelector('.card-container div.card'));
```

# --seed--

## --seed-contents--

```html
--fcc-editable-region--
<h1>XYZ Bookstore</h1>
<p>Browse our collection of amazing books!</p>
<div class="card-container">

</div>
--fcc-editable-region--
```