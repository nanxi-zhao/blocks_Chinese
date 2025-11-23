---
id: 66ed8fc9f45ce3ece4053eae
title: CSS动画测验
challengeType: 8
dashedName: quiz-css-animations
---

# --description--

要通过测验，你必须正确回答以下 20 道题中的至少 18 题。

# --quizzes--

## --quiz--

### --question--

#### --text--

CSS中的[transform]属性的用途是什么？

#### --distractors--

改变元素的可见性

---

对文本应用视觉效果

---

设置元素的尺寸

#### --answer--

修改元素的位置、大小和形状

### --question--

#### --text--

CSS [animation-direction]属性如何影响动画？

#### --distractors--

指定动画是否应该重复

---

设置动画的持续时间

---

定义动画的速度

#### --answer--

定义动画应该如何播放

### --question--

#### --text--

哪个CSS属性使动画运行3次？

#### --distractors--

`animation-repeat: 3`

---

`animation-loop: 3`

---

`animation-delay: 3`

#### --answer--

`animation-iteration-count: 3`

### --question--

#### --text--

哪个CSS时间函数使动画从开始到结束以一致的速度运行？

#### --distractors--

`ease`

---

`ease-in`

---

`ease-in-out`

#### --answer--

`linear`

### --question--

#### --text--

CSS中的[@keyframes]规则定义了什么？

#### --distractors--

CSS渐变的颜色

---

CSS旋转的角度

---

元素的尺寸

#### --answer--

CSS动画的阶段

### --question--

#### --text--

CSS中[translateX()]函数的用途是什么？

#### --distractors--

改变元素的不透明度

---

旋转元素

---

垂直重新定位元素

#### --answer--

水平重新定位元素

### --question--

#### --text--

以下哪项不是CSS动画的潜在问题？

#### --distractors--

它们可能引起某些用户的不适或身体伤害

---

用户可能觉得它们分散注意力

---

过度使用可能导致性能不佳

#### --answer--

它们可以增强用户体验

### --question--

#### --text--

[@keyframes]规则在哪里定义？

#### --distractors--

在HTML文件的[body]元素内

---

在HTML文件的[head]元素内

---

在CSS类定义内

#### --answer--

在顶层，任何CSS选择器之外

### --question--

#### --text--

哪个CSS属性允许你暂停和恢复动画？

#### --distractors--

`animation-timing-function`

---

`animation-delay`

---

`animation-direction`

#### --answer--

`animation-play-state`

### --question--

#### --text--

CSS中[animation-name]属性应该分配什么值？

#### --distractors--

动画的持续时间（秒）

---

动画使用的时间函数

---

动画开始前的延迟时间（秒）

#### --answer--

由[@keyframes]定义的动画名称

### --question--

#### --text--

这个[@keyframe]规则对动画元素做了什么？

```css
@keyframes animation {
  0% {
    transform: translateX(-50px);
  }
  100% {
    transform: translateX(100px);
  }
}
```

#### --distractors--

将元素顺时针旋转90度

---

将元素颜色更改为蓝色

---

将元素缩放到初始大小的50%，然后缩放到初始大小的100%

#### --answer--

将元素水平从-50px移动到100px，相对于其起始点

### --question--

#### --text--

哪个CSS属性定义了动画随时间的进展情况？

#### --distractors--

`animation-delay`

---

`animation-fill-mode`

---

`animation-iteration-count`

#### --answer--

`animation-timing-function`

### --question--

#### --text--

哪个CSS属性用于指定动画应该花费5秒钟完成？

#### --distractors--

```css
animation-name: 5s;
```

---

```css
animation-delay: 5s;
```

---

```css
animation-timing-function: 5s;
```

#### --answer--

```css
animation-duration: 5s;
```

### --question--

#### --text--

在以下CSS [@keyframe]规则中，[50%]代表什么？

```css
@keyframes animation {
  0% {
    transform: translateX(-50px);
  }
  50% {
    transform: translateX(25px);
  }
  100% {
    transform: translateX(100px);
  }
}
```

#### --distractors--

动画的起始点

---

动画的结束点

---

动画的速度

#### --answer--

动画的中点

### --question--

#### --text--

当应用[transform: translateX(200px);]属性时会发生什么？

#### --distractors--

元素将向左移动200px

---

元素将向底部移动200px

---

元素将顺时针旋转200度

#### --answer--

元素将向右移动200px

### --question--

#### --text--

如果[animation-iteration-count]设置为[infinite]，动画将如何表现？

#### --distractors--

它将运行一次然后停止

---

它将在第一次迭代后暂停

---

它将在三次迭代后停止

#### --answer--

它将无限重复

### --question--

#### --text--

哪个[@keyframes]选择器指定动画的起始点？

#### --distractors--

`50%`

---

`25%`

---

`100%`

#### --answer--

`0%`

### --question--

#### --text--

可以使用[animation]简写CSS属性指定哪些属性？

#### --distractors--

仅动画的名称

---

动画的名称和持续时间

---

动画的名称、持续时间和延迟

#### --answer--

所有动画属性

### --question--

#### --text--

哪个CSS属性用于应用由[@keyframes]规则定义的动画？

#### --distractors--

`animation-duration`

---

`apply`

---

`translate`

#### --answer--

`animation`

### --question--

#### --text--

哪个CSS属性允许你设置动画开始前的时间？

#### --distractors--

`animation-fill-mode`

---

`animation-timing-function`

---

`animation-iteration-count`

#### --answer--

`animation-delay`

## --quiz--

### --question--

#### --text--

CSS [animation-delay]属性做什么？

#### --distractors--

设置动画持续多长时间

---

指定时间函数

---

定义动画方向

#### --answer--

延迟动画的开始

### --question--

#### --text--

哪个动画属性指定元素在动画之前和之后应该如何样式化？

#### --distractors--

`animation-delay`

---

`animation-direction`

---

`animation-iteration-count`

#### --answer--

`animation-fill-mode`

### --question--

#### --text--

为什么应该适度使用CSS动画？

#### --distractors--

太多CSS动画可能导致样式破坏以及在不同浏览器中样式不一致

---

太多CSS动画可能导致搜索引擎结果排名较低或不存在

---

太多CSS动画将自动崩溃服务器并增加安全风险的可能性

#### --answer--

太多CSS动画可能导致性能不佳，并且可能分散注意力或对某些有特殊需求的用户造成问题

### --question--

#### --text--

哪个动画属性确定动画应该向前播放、向后播放还是交替播放？

#### --distractors--

`animation-fill-mode`

---

`animation-delay`

---

`animation-timing-function`

#### --answer--

`animation-direction`

### --question--

#### --text--

哪个CSS媒体查询检测用户是否请求了最小动画或运动效果？

#### --distractors--

`reduce-motion`

---

`min-motion-preference`

---

`motion-preferences`

#### --answer--

`prefers-reduced-motion`

### --question--

#### --text--

哪个属性设置[animation]重复的次数？

#### --distractors--

`animation-duration`

---

`animation-count`

---

`animation-delay`

#### --answer--

`animation-iteration-count`

### --question--

#### --text--

哪个CSS规则用于定义动画在其持续时间内的各个阶段和样式？

#### --distractors--

`@style`

---

`@transition`

---

`@transform`

#### --answer--

`@keyframes`

### --question--

#### --text--

在[reduced‑motion]媒体查询内，哪个声明禁用过渡？

#### --distractors--

`animation: none;`

---

`transition: remove;`

---

`animation-play-state: paused;`

#### --answer--

`transition: none;`

### --question--

#### --text--

[animation-play-state]属性允许你做什么？

#### --distractors--

设置动画重复的次数

---

指定动画完成所需的时间

---

确定动画播放的方向

#### --answer--

暂停和恢复动画

### --question--

#### --text--

在处理动画时，以下哪项是良好的实践？

#### --distractors--

尽可能多地使用闪烁的颜色和快速移动来吸引注意力

---

避免在不同设备或屏幕尺寸上测试动画

---

让动画尽可能长时间运行以确保用户注意到它们

#### --answer--

避免每秒闪烁超过三次的内容，以防止引发癫痫发作或造成不适

### --question--

#### --text--

为什么在CSS规则中使用[!important]声明？

#### --distractors--

防止其他媒体查询加载

---

将样式限制在第一个子元素

---

更容易调试CSS

#### --answer--

确保这些规则优先于其他样式

### --question--

#### --text--

CSS中[animation-iteration-count: 1 !important;]确保什么？

#### --distractors--

动画被暂停

---

动画无限运行

---

动画在每个周期反转方向

#### --answer--

任何循环动画只播放一次

### --question--

#### --text--

哪个CSS属性用于指定动画应该花费多长时间完成？

#### --distractors--

`animation-delay`

---

`animation-timing-function`

---

`animation-iteration-count`

#### --answer--

`animation-duration`

### --question--

#### --text--

哪个属性不是[animation]简写的一部分？

#### --distractors--

`animation-delay`

---

`animation-timing-function`

---

`animation-direction`

#### --answer--

`animation-transform`

### --question--

#### --text--

[@keyframes]规则定义了什么？

#### --distractors--

动画的时间函数

---

元素的默认状态

---

动画的媒体查询

#### --answer--

动画中不同点的样式序列

### --question--

#### --text--

这个[@keyframe]规则对动画元素做了什么？

```css
@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
```

#### --distractors--

将元素从0%缩放到100%

---

将元素从左到右移动

---

将文本颜色更改为黑色

#### --answer--

通过逐渐增加透明度使元素淡入

### --question--

#### --text--

在关键帧规则中，[100%]代表什么？

#### --distractors--

动画的开始

---

中点

---

缓动函数

#### --answer--

动画的结束

### --question--

#### --text--

哪个属性控制[animation]在其持续时间内的节奏？

#### --distractors--

`animation-duration`

---

`animation-delay`

---

`animation-iteration-count`

#### --answer--

`animation-timing-function`

### --question--

#### --text--

在实现动画以保持可访问性时，开发人员应该考虑什么？

#### --distractors--

完全依赖JavaScript进行所有动画

---

添加频繁而激烈的动画以产生影响

---

仅包含大胆、快速和令人惊讶的效果

#### --answer--

使用微妙、有意的效果，尊重用户偏好，并提供用户控制

### --question--

#### --text--

以下哪项是正确的语法，使元素从左侧滑入？

#### --distractors--

```css
@keyframes slide-in {
  0 { 
    transform: translate(-100%); 
  }
  100 { 
    transform: translate(0); 
  }
}
```

---

```css
@keyframes slide-in {
  from { 
    translateX(-100%); 
  }
  to { 
    translateX(0); 
  }
}
```

---

```css
@keyframes slide-in {
  start { 
    transform: moveX(-100%); 
  }
  end { 
    transform: moveX(0); 
  }
}
```

#### --answer--

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