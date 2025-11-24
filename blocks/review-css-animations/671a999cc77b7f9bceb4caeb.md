---
id: 671a999cc77b7f9bceb4caeb
title: CSS 动画复习
challengeType: 31
dashedName: review-css-animations
---

# --description--

## CSS 动画基础

- **定义**：CSS 动画允许你在网页上创建动态、视觉上引人入胜的效果，而无需 JavaScript 或复杂的编程。它们提供了一种在指定持续时间内平滑过渡元素不同样式的方法。
- **`@keyframes` 规则**：此规则定义动画的阶段和样式。它指定动画期间元素在各个点应具有的样式。

```css
@keyframes slide-in {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}
```

- **`animation` 属性**：这是应用动画的简写属性。
- **`animation-name`**：这指定要使用的 `@keyframes` 规则的名称。
- **`animation-duration`**：这设置动画完成所需的时间。
- **`animation-timing-function`**：这定义动画如何随时间推移（如 ease、linear、ease-in-out）。
- **`animation-delay`**：这指定动画开始前的延迟。
- **`animation-iteration-count`**：这设置动画应重复的次数。
- **`animation-direction`**：这确定动画是应向前播放、向后播放还是交替播放。
- **`animation-fill-mode`**：这指定动画前后元素的样式。
- **`animation-play-state`**：这允许你暂停和恢复动画。

## 可访问性和 `prefers-reduced-motion` 媒体查询

- **`prefers-reduced-motion` 媒体查询**：动画的主要可访问性问题之一是它们可能对某些用户造成不适甚至身体伤害。前庭疾病或运动敏感的人在接触屏幕上的某些类型运动时可能会感到头晕、恶心或头痛。`prefers-reduced-motion` 媒体查询允许 Web 开发人员检测用户是否在系统级别请求最少的动画或运动效果。

```css
.animated-element {
  transition: transform 0.3s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .animated-element {
    transition: none;
  }
}
```

# --assignment--

复习 CSS 动画的主题和概念。