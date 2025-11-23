---
id: bd7158d8c442eddfaeb5bd18
title: 构建一个致敬页面
challengeType: 25
demoType: onClick
dashedName: build-a-tribute-page
---

# --description--

**目标：** 实现以下用户需求并通过所有测试以完成实验。

**用户需求：**

1. 你的致敬页面应该有一个 `main` 元素，对应的 `id` 为 `main`，它包含所有其他元素。
2. 你应该看到一个 `id` 为 `title` 的元素，其中包含一个字符串（即文本），描述致敬页面的主题（例如"Dr. Norman Borlaug"）。
3. 你应该看到一个 `figure` 或 `div` 元素，`id` 为 `img-div`。
4. 在 `#img-div` 元素内，你应该看到一个 `img` 元素，对应的 `id="image"`。
5. 在 `#img-div` 元素内，你应该看到一个 `id="img-caption"` 的元素，其中包含描述 `#img-div` 中显示的图像的文本内容。
6. 你应该看到一个 `id="tribute-info"` 的元素，其中包含描述致敬页面主题的文本内容。
7. 你应该看到一个 `a` 元素，对应的 `id="tribute-link"`，链接到外部网站，其中包含关于致敬页面主题的附加信息。提示：你必须给你的元素一个 `target` 属性并将其设置为 `_blank`，以便你的链接在新标签页中打开。
8. 你的 `#image` 应该使用 `max-width` 和 `height` 属性来相对于其父元素的宽度进行响应式调整大小，而不超过其原始大小。
9. 你的 `img` 元素应该在其父元素内居中。

**注意：** 确保在HTML中链接你的样式表并应用CSS。

# --hints--

你应该有一个 `main` 元素，`id` 为 `main`。

```js
const el = document.getElementById('main');
assert.isNotNull(el);
assert.strictEqual(el.tagName, 'MAIN');
```

你的 `#img-div`、`#image`、`#img-caption`、`#tribute-info` 和 `#tribute-link` 都应该是 `#main` 的后代元素。

```js
const el1 = document.querySelector('#main #img-div');
const el2 = document.querySelector('#main #image');
const el3 = document.querySelector('#main #img-caption');
const el4 = document.querySelector('#main #tribute-info');
const el5 = document.querySelector('#main #tribute-link');
assert.isNotNull(el1);
assert.isNotNull(el2);
assert.isNotNull(el3);
assert.isNotNull(el4);
assert.isNotNull(el5);
```

你应该有一个 `id` 为 `title` 的元素。

```js
const el = document.getElementById('title');
assert.isNotNull(el);
```

你的 `#title` 不应该为空。

```js
const el = document.getElementById('title');
assert.isNotNull(el);
assert.isNotEmpty(el.innerText.trim());
```

你应该有一个 `figure` 或 `div` 元素，`id` 为 `img-div`。

```js
const el = document.getElementById('img-div');
assert.isNotNull(el);
assert.isTrue(el.tagName === 'DIV' || el.tagName === 'FIGURE');
```

你应该有一个 `img` 元素，`id` 为 `image`。

```js
const el = document.getElementById('image');
assert.isNotNull(el);
assert.strictEqual(el.tagName, 'IMG');
```

你的 `#image` 应该是 `#img-div` 的后代元素。

```js
const el = document.querySelector('#img-div #image');
assert.isNotNull(el);
```

你应该有一个 `figcaption` 或 `div` 元素，`id` 为 `img-caption`。

```js
const el = document.getElementById('img-caption');
assert.isNotNull(el);
assert.isTrue(el.tagName === 'DIV' || el.tagName === 'FIGCAPTION');
```

你的 `#img-caption` 应该是 `#img-div` 的后代元素。

```js
const el = document.querySelector('#img-div #img-caption');
assert.isNotNull(el);
```

你的 `#img-caption` 不应该为空。

```js
const el = document.getElementById('img-caption');
assert.isNotNull(el);
assert.isNotEmpty(el.innerText);
```

你应该有一个 `id` 为 `tribute-info` 的元素。

```js
const el = document.getElementById('tribute-info');
assert.isNotNull(el);
```

你的 `#tribute-info` 不应该为空。

```js
const el = document.getElementById('tribute-info');
assert.isNotNull(el);
assert.isNotEmpty(el.innerText);
```

你应该有一个 `a` 元素，`id` 为 `tribute-link`。

```js
const el = document.getElementById('tribute-link');
assert.isNotNull(el);
assert.strictEqual(el.tagName, 'A');
```

你的 `#tribute-link` 应该有一个 `href` 属性和值。

```js
const el = document.getElementById('tribute-link');
assert.isNotNull(el);
assert.isNotNull(el.href);
assert.isNotEmpty(el.href);
```

你的 `#tribute-link` 应该有一个 `target` 属性设置为 `_blank`。

```js
const el = document.getElementById('tribute-link');
assert.isNotNull(el);
assert.strictEqual(el.target, '_blank');
```

你的 `img` 元素应该有 `display` 为 `block`。

```js
const img = document.getElementById('image');
const imgStyle = window.getComputedStyle(img);
const style = imgStyle?.getPropertyValue('display');
assert.strictEqual(style, 'block');
```

你的 `#image` 应该有 `max-width` 为 `100%`。

```js
const img = document.getElementById('image');
const imgStyle = window.getComputedStyle(img);
const style = imgStyle?.getPropertyValue('max-width');
assert.strictEqual(style, '100%');
```

你的 `#image` 应该有 `height` 为 `auto`。

```js
// taken from the testable-projects repo
const img = document.getElementById('image');
const imgStyle = window.getComputedStyle(img);
const oldDisplayValue = imgStyle.getPropertyValue('display');
const oldDisplayPriority = imgStyle.getPropertyPriority('display');
img?.style.setProperty('display', 'none', 'important');
const heightValue = imgStyle?.getPropertyValue('height');
img?.style.setProperty('display', oldDisplayValue, oldDisplayPriority);
assert.strictEqual(heightValue, 'auto');
```

你的 `#image` 应该在其父元素内居中。

```js
// taken from the testable-projects repo
const img = document.getElementById('image'),
  imgParent = img?.parentElement,
  imgLeft = img?.getBoundingClientRect().left,
  imgRight = img?.getBoundingClientRect().right,
  parentLeft = imgParent?.getBoundingClientRect().left,
  parentRight = imgParent?.getBoundingClientRect().right,
  leftMargin = imgLeft - parentLeft,
  rightMargin = parentRight - imgRight;
assert.isBelow(leftMargin - rightMargin, 6);
assert.isBelow(rightMargin - leftMargin, 6);
```

# --seed--

## --seed-contents--

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>致敬页面</title>
  </head>

  <body></body>
</html>
```

```css

```

# --solutions--

```html
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <main id="main">
      <h1 id="title">Dr. Norman Borlaug</h1>
      <p>拯救了十亿人生命的人</p>
      <figure id="img-div">
        <img
          id="image"
          src="https://cdn.MasterPuti.org/testable-projects-fcc/images/tribute-page-main-image.jpg"
          alt="Dr. Norman Borlaug seen standing in Mexican wheat field with a group of biologists"
        />
        <figcaption id="img-caption">
          Dr. Norman Borlaug，从左边数第三位，在墨西哥培训生物学家如何提高小麦产量——这是他毕生对抗饥饿的事业的一部分。
        </figcaption>
      </figure>
      <section id="tribute-info">
        <h3 id="headline">以下是Dr. Borlaug生平的时间线：</h3>
        <ul>
          <li><strong>1914</strong> - 出生在爱荷华州的Cresco</li>
          <li>
            <strong>1933</strong> - 离开家庭农场，通过大萧条时期被称为"国家青年管理局"的项目进入明尼苏达大学学习
          </li>
          <li>
            <strong>1935</strong> - 不得不停学并攒更多钱。在民间资源保护队工作，帮助饥饿的美国人。"我看到了食物是如何改变他们的，"他说。"所有这些都在我身上留下了伤痕。"
          </li>
          <li>
            <strong>1937</strong> - 完成大学学业并在美国林业局找到一份工作
          </li>
          <li>
            <strong>1938</strong> - 与妻子Margret Gibson结婚69年。由于预算削减而被解雇。受到Elvin Charles Stakman的启发，他回到学校在Stakman的指导下学习，Stakman教他如何培育抗病植物。
          </li>
          <li>
            <strong>1941</strong> - 珍珠港事件后试图参军，但被拒绝。相反，军方要求他的实验室研究防水胶水、DDT控制疟疾、消毒剂和其他应用科学。
          </li>
          <li>
            <strong>1942</strong> - 获得遗传学和植物病理学博士学位
          </li>
          <li>
            <strong>1944</strong> - 拒绝了杜邦公司100%的加薪，离开怀孕的妻子，飞往墨西哥领导一个新的植物病理学项目。在接下来的16年里，他的团队培育了6000种不同的抗病小麦品种——包括适合地球上每个主要气候的不同品种。
          </li>
          <li>
            <strong>1945</strong> - 发现了一种每年种植两次小麦的方法，使小麦产量翻倍
          </li>
          <li>
            <strong>1953</strong> - 将一种矮壮的小麦品种与高产的美国品种杂交，创造出对肥料反应良好的品种。它后来提供了墨西哥95%的小麦。
          </li>
          <li>
            <strong>1962</strong> - 访问德里，将他的高产小麦品种带到印度次大陆，及时帮助缓解了由于人口快速增长而导致的大规模饥荒
          </li>
          <li><strong>1970</strong> - 获得诺贝尔和平奖</li>
          <li>
            <strong>1983</strong> - 帮助七个非洲国家大幅提高玉米和高粱产量
          </li>
          <li>
            <strong>1984</strong> - 成为德克萨斯A&M大学的杰出教授
          </li>
          <li>
            <strong>2005</strong> - 表示"到2050年，我们必须将世界粮食供应量增加一倍。"他认为转基因作物是我们满足需求的唯一途径，因为我们的可耕地正在耗尽。他说转基因作物本质上并不危险，因为"我们一直在改良植物和动物。早在我们称之为科学之前，人们就在选择最好的品种。"
          </li>
          <li><strong>2009</strong> - 95岁时去世。</li>
        </ul>
        <blockquote
          cite="http://news.rediff.com/report/2009/sep/14/pm-pays-tribute-to-father-of-green-revolution-borlaug.htm"
        >
          <p>
            "Borlaug的生平和成就证明了一个人的卓越智慧、坚持不懈和科学远见对人类和平与进步所能做出的深远贡献。"
          </p>
          <cite>-- 印度总理曼莫汉·辛格</cite>
        </blockquote>
        <h3>
          如果你有时间，你应该在他的
          <a
            id="tribute-link"
            href="https://en.wikipedia.org/wiki/Norman_Borlaug"
            target="_blank"
            >维基百科条目</a
          >中了解更多关于这位不可思议的人的信息。
        </h3>
      </section>
    </main>
  </body>
</html>
```

```css
html {
  /* 设置10px的基础字体大小，让我们更容易计算rem
       信息：1rem === 10px，1.5rem === 15px，2rem === 20px，以此类推
     */
  font-size: 10px;
}

body {
  /* 原生字体栈 https://getbootstrap.com/docs/4.2/content/reboot/#native-font-stack */
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto',
    'Helvetica Neue', Arial, sans-serif;
  font-size: 1.6rem;
  line-height: 1.5;
  text-align: center;
  color: #333;
  margin: 0;
}

h1 {
  font-size: 4rem;
  margin-bottom: 0;
}

@media (max-width: 460px) {
  h1 {
    font-size: 3.5rem;
    line-height: 1.2;
  }
}

h2 {
  font-size: 3.25rem;
}

a {
  color: #477ca7;
}

a:visited {
  color: #74638f;
}

#main {
  margin: 30px 8px;
  padding: 15px;
  border-radius: 5px;
  background: #eee;
}

@media (max-width: 460px) {
  #main {
    margin: 0;
  }
}

img {
  max-width: 100%;
  display: block;
  height: auto;
  margin: 0 auto;
}

#img-div {
  background: white;
  padding: 10px;
  margin: 0;
}

#img-caption {
  margin: 15px 0 5px 0;
}

@media (max-width: 460px) {
  #img-caption {
    font-size: 1.4rem;
  }
}

#headline {
  margin: 50px 0;
  text-align: center;
}

ul {
  max-width: 550px;
  margin: 0 auto 50px auto;
  text-align: left;
  line-height: 1.6;
}

li {
  margin: 16px 0;
}

blockquote {
  font-style: italic;
  max-width: 545px;
  margin: 0 auto 50px auto;
  text-align: left;
}
```