---
id: 68eca3cfeebef2cd8cc5f814
title: 第 11 步
challengeType: 0
dashedName: step-11
---

# --description--

为第二个具有 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 为 [card](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6e8d0caee3afaaf142ef.md#L58-L58) 的元素添加一个 [id](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec9332a9b5b2b32487bd00.md#L58-L58) 属性，并将其值设置为 [dave-cooking-book](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68eca3cfeebef2cd8cc5f814.md#L58-L58)。记住每个 [id](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec9332a9b5b2b32487bd00.md#L58-L58) 必须是唯一的。

# --hints--

第二个具有 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 为 [card](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6e8d0caee3afaaf142ef.md#L58-L58) 的元素应该有一个 [id](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec9332a9b5b2b32487bd00.md#L58-L58) 属性。

```js
const cards = document.querySelectorAll('.card');
assert.isTrue(cards[1]?.hasAttribute('id'));
```

第二个具有 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6d9a315221aa31e54816.md#L58-L58) 为 [card](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec6e8d0caee3afaaf142ef.md#L58-L58) 的元素应该有一个 [id](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68ec9332a9b5b2b32487bd00.md#L58-L58) 属性，值为 [dave-cooking-book](file:///F:/code/blocks_Chinese/blocks_english/workshop-bookstore-page/68eca3cfeebef2cd8cc5f814.md#L58-L58)。

```js
const cards = document.querySelectorAll('.card');
assert.equal(cards[1]?.id, 'dave-cooking-book');
```

# --seed--

## --seed-contents--

```html
<h1>XYZ Bookstore</h1>
<p>Browse our collection of amazing books!</p>
<div class="card-container">
  <div class="card" id="sally-adventure-book">
    <h2>Sally's SciFi Adventure</h2>
    <p>This is an epic story of Sally and her dog Rex as they navigate through other worlds.</p>
    <button class="btn">Buy Now</button>
  </div>
  --fcc-editable-region--
  <div class="card">

  </div>
  --fcc-editable-region--
</div>
```