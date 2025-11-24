---
id: 60f85a62fb30c80bcea0cedb
title: 步骤 18
challengeType: 0
dashedName: step-18
---

# --description--

在第二个 fieldset 元素内添加一个 label 元素，其文本为 `Input your age (years):`。

# --hints--

你应该添加第二个 label 元素。

```js
assert.exists(document.querySelectorAll('label')?.[4]);
```

你的 label 元素应该在第二个 fieldset 元素内。

```js
assert.exists(document.querySelectorAll('label')?.[4]?.parentElement?.tagName === 'FIELDSET');
```

你的 label 元素的文本应该是 `Input your age (years):`。

```js
assert.strictEqual(document.querySelectorAll('label')?.[4]?.innerText, 'Input your age (years):');
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
        <input type="submit" value="Submit" />
      </fieldset>
      <fieldset>
        <label>Input your age (years):</label>
      </fieldset>
    </form>
  </body>
</html>
```

```css

```