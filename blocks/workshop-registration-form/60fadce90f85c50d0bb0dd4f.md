---
id: 60fadce90f85c50d0bb0dd4f
title: 步骤 37
challengeType: 0
dashedName: step-37
---

# --description--

在刚刚添加的 [label](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素下方添加一个 [input](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素。给它一个 [type](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/axios/lib/core/settle.js#L13-L22) 属性，其值为 `file`，一个 [name](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/axios/lib/core/settle.js#L13-L22) 属性，其值为 `profile-picture`，以及一个 [id](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/axios/lib/core/settle.js#L13-L22) 属性，其值为 `profile-picture`。

# --hints--

你应该添加一个 [input](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素。

```js
assert.exists(document.querySelector('input[type="file"]'));
```

你的 [input](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素应该在第二个 [fieldset](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素内。

```js
const sel = document.querySelectorAll('fieldset')[1];
assert.exists(sel?.children?.[sel?.children?.length - 2]?.tagName === 'INPUT');
```

你的 [input](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素应该在带有 `profile-picture` 文本的 [label](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素之后。

```js
const sel = document.querySelectorAll('fieldset')[1];
assert.exists(sel?.children?.[sel?.children?.length - 2]?.previousElementSibling?.tagName === 'LABEL');
```

你的 [input](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素应该有一个 [type](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/axios/lib/core/settle.js#L13-L22) 属性，其值为 `file`。

```js
assert.strictEqual(document.querySelector('input[type="file"]')?.type, 'file');
```

你的 [input](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素应该有一个 [name](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/axios/lib/core/settle.js#L13-L22) 属性，其值为 `profile-picture`。

```js
assert.strictEqual(document.querySelector('input[type="file"]')?.name, 'profile-picture');
```

你的 [input](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/@types/node/stream.d.ts#L53-L53) 元素应该有一个 [id](file:///e:/1.work/byy/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/blocks/node_modules/axios/lib/core/settle.js#L13-L22) 属性，其值为 `profile-picture`。

```js
assert.strictEqual(document.querySelector('input[type="file"]')?.id, 'profile-picture');
```

# --seed--

## --seed-contents--

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Registration Form</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <h1>Registration Form</h1>
    <p>Please fill out this form with the required information</p>
    <form>
      <fieldset>
        <label>Enter Your First Name:</label>
        <input type="text" required />
        <label>Enter Your Last Name:</label>
        <input type="text" required />
        <label>Enter Your Email:</label>
        <input type="email" required />
        <label>Create a New Password:</label>
        <input type="password" required />
        <input type="submit" value="Submit" name="submit" />
      </fieldset>
      <fieldset>
        <label>Input your age (years):</label>
        <input type="number" required />
        <label>How did you hear about us?</label>
        <select>
          <option value="">(select one)</option>
          <option value="freeCodeCamp News">freeCodeCamp News</option>
          <option value="freeCodeCamp YouTube Channel">freeCodeCamp YouTube Channel</option>
          <option value="freeCodeCamp Forum">freeCodeCamp Forum</option>
          <option value="Other">Other</option>
        </select>
        <label for="terms-and-conditions">I accept the terms and conditions</label>
        <input type="checkbox" id="terms-and-conditions" name="terms-and-conditions" required />
        <label for="file">Upload a profile picture:</label>
        <input type="file" name="file" id="file" />
        <hr>
        <label for="profile-picture">Upload a profile picture:</label>

        <input type="submit" value="Submit" name="submit" />
      </fieldset>
    </form>
  </body>
</html>

```

```css

```
