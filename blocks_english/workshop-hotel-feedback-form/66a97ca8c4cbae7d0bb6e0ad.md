---
id: 66a97ca8c4cbae7d0bb6e0ad
title: 步骤 32
challengeType: 0
dashedName: step-32
---

# --description--

在你�?`select` 元素中，添加以下五个 `option` 元素，并�?`option` 文本�?`value` 属性添加相应的值：

**值属性：**

- poor
- satisfactory
- good
- very-good
- excellent

**选项文本�?*

- Poor
- Satisfactory
- Good
- Very Good
- Excellent


不要忘记在值为 `"excellent"` �?`option` 元素中添�?`selected` 属性�?

# --hints--

你应该有一个值设置为 `"poor"` �?`option` 元素�?

```js
assert.exists(document.querySelector('fieldset:nth-of-type(4) select#food option[value="poor"]'));
```

`value` �?`"poor"` �?`option` 应包含文�?`"Poor"`�?

```js
assert.strictEqual(document.querySelector('fieldset:nth-of-type(4) select#food option[value="poor"]')?.textContent.trim(), 'Poor');
```

你应该有一�?`value` 设置�?`"satisfactory"` �?`option` 元素�?

```js
assert.exists(document.querySelector('fieldset:nth-of-type(4) select#food option[value="satisfactory"]'));
```

`value` �?`"satisfactory"` �?`option` 应包含文�?`"Satisfactory"`�?

```js
assert.strictEqual(document.querySelector('fieldset:nth-of-type(4) select#food option[value="satisfactory"]')?.textContent.trim(), 'Satisfactory');
```

你应该有一�?`value` 设置�?`"good"` �?`option` 元素�?

```js
assert.exists(document.querySelector('fieldset:nth-of-type(4) select#food option[value="good"]'));
```

`value` �?`"good"` �?`option` 应包含文�?`"Good"`�?

```js

assert.strictEqual(document.querySelector('fieldset:nth-of-type(4) select#food option[value="good"]')?.textContent.trim(), 'Good');
```

你应该有一个值设置为 `"very-good"` �?`option` 元素�?

```js
assert.exists(document.querySelector('fieldset:nth-of-type(4) select#food option[value="very-good"]'));
```

`value` �?`"very-good"` �?`option` 应包含文�?`"Very Good"`�?

```js
assert.strictEqual(document.querySelector('fieldset:nth-of-type(4) select#food option[value="very-good"]')?.textContent.trim(), 'Very Good');
```

你应该有一个值设置为 `"excellent"` �?`option` 元素�?

```js
assert.exists(document.querySelector('fieldset:nth-of-type(4) select#food option[value="excellent"]'));
```

`value` �?`"excellent"` �?`option` 应包含文�?`"Excellent"`�?

```js
assert.strictEqual(document.querySelector('fieldset:nth-of-type(4) select#food option[value="excellent"]')?.textContent.trim(), 'Excellent');
```

你应将具有`selected` 属性的 `option` 元素设置�?`"excellent"`�?

```js
assert.exists(document.querySelector('fieldset:nth-of-type(4) select#food option[value="excellent"][selected]'));
```

# --seed--

## --seed-contents--

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Hotel Feedback Form</title>
  </head>
  <body>
    <header>
      <h1>Hotel Feedback Form</h1>
      <p>
        Thank you for staying with us. Please provide feedback on your recent
        stay.
      </p>
    </header>
    <main>
      <form method="POST" action="https://hotel-feedback.MasterPuti.org">
        <fieldset>
          <legend>Personal Information</legend>
          <label for="full-name">Name (required):</label>
          <input type="text" id="full-name" name="name" placeholder="e.g., John Doe" required size="20">

          <label for="email">Email address (required):</label>
          <input
            placeholder="example@email.com"
            required
            id="email"
            type="email"
            name="email"
            size="20"
          />
          <label for="age">Age (optional):</label>
          <input type="number" name="age" id="age" min="3" max="100" />
        </fieldset>

        <fieldset>
          <legend>Was this your first time at our hotel?</legend>
          <input id="yes-option" type="radio" name="hotel-stay" />
          <label for="yes-option">Yes</label>
          <input id="no-option" type="radio" name="hotel-stay" />
          <label for="no-option">No</label>
        </fieldset>

        <fieldset>
          <legend>
            Why did you choose to stay at our hotel? (Check all that apply)
          </legend>

          <input type="checkbox" id="ads" name="ads" value="ads" />
          <label for="ads">Social Media Ads</label>

          <input
            type="checkbox"
            id="recommendation"
            name="recommendation"
            value="recommendation"
          />
          <label for="recommendation">Personal Recommendation</label>

          <input type="checkbox" id="location" name="location" value="location" />
          <label for="location">Location</label>

          <input
            checked
            type="checkbox"
            id="reputation"
            name="reputation"
            value="reputation"
          />
          <label for="reputation">Reputation</label>

          <input type="checkbox" id="price" name="price" value="price" />
          <label for="price">Price</label>
        </fieldset>

        <fieldset>
          <legend>Ratings</legend>

          <label for="service">How was the service?</label>

          <select name="service" id="service">
            <option value="poor">Poor</option>
            <option value="satisfactory">Satisfactory</option>
            <option value="good">Good</option>
            <option value="very-good">Very Good</option>
            <option selected value="excellent">Excellent</option>
          </select>

          <label for="food">How was the food?</label>

          --fcc-editable-region--
          <select name="food" id="food">

          </select>
          --fcc-editable-region--
        </fieldset>
      </form>
    </main>
  </body>
</html>
```

