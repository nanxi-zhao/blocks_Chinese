---
id: 66ed8fc1f45ce3ece4053ead
title: CSS可访问性测验
challengeType: 8
dashedName: quiz-css-accessibility
---

# --description--

要通过测验，你必须正确回答以下 10 道题中的至少 9 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

为什么你需要在网页上有良好的颜色对比度？

#### --distractors--

让页面更加生动

---

满足搜索引擎优化(SEO)的要求

---

让页面的重要元素突出显示

#### --answer--

让页面内容可访问且可读

### --question--

#### --text--

以下哪个工具允许你输入背景色和前景色并检查它们的对比度？

#### --distractors--

TPGi颜色对比度分析器

---

Figma

---

Canva

#### --answer--

WebAIM颜色对比度检查器

### --question--

#### --text--

以下哪个工具允许你从实时网页中选择背景色和前景色并检查它们的对比度？

#### --distractors--

Figma

---

Canva

---

WebAIM颜色对比度检查器

#### --answer--

TPGi颜色对比度分析器

### --question--

#### --text--

为什么你不应该使用[display: none]和[visibility: hidden]来视觉上隐藏内容？

#### --distractors--

这些方法使得只有辅助技术如屏幕阅读器可以访问隐藏内容

---

这些方法使得内容只有在用户将鼠标移动到内容上时才隐藏

---

这些方法在某些浏览器中不起作用

#### --answer--

这些方法从可访问性树中移除内容，使得屏幕阅读器无法访问隐藏内容

### --question--

#### --text--

什么是可访问性树？

#### --distractors--

网页布局的视觉表示

---

屏幕阅读器用来读取网页文本内容的结构

---

DOM树的副本

#### --answer--

屏幕阅读器用来解释和交互网页内容的结构

### --question--

#### --text--

以下哪项确保图像的最小宽度为[400px]，但当视口宽度大于[1000px]时变得更宽？

#### --distractors--

```css
img {
  width: max(400px, 10vw);
}
```

---

```css
img {
  width: max(400px, 30vw);
}
```

---

```css
img {
  width: max(400px, 20vw);
}
```

#### --answer--

```css
img {
  width: max(400px, 40vw);
}
```

### --question--

#### --text--

以下哪个[scroll-behavior]值允许平滑滚动行为？

#### --distractors--

`auto`

---

`inherit`

---

`revert`

#### --answer--

`smooth`

### --question--

#### --text--

以下哪个功能用于检测用户的动画偏好？

#### --distractors--

`prefers-contrast`

---

`display-mode`

---

`animation`

#### --answer--

`prefers-reduce-motion`

### --question--

#### --text--

以下哪项是[input]元素中[placeholder]属性的可访问性问题？

#### --distractors--

占位符文本阻止屏幕阅读器读取输入标签文本

---

占位符文本阻止屏幕阅读器读取输入值

---

占位符文本太小而无法阅读

#### --answer--

占位符文本可能与实际输入值混淆

### --question--

#### --text--

[hidden]属性做什么？

#### --distractors--

它隐藏内容并在悬停时显示

---

它仅从可访问性树中隐藏内容

---

它在视觉上隐藏内容，但内容在可访问性树中可用

#### --answer--

它既在视觉上隐藏内容，也从可访问性树中隐藏内容