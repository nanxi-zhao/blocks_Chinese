---
id: 67d301cc87b84eaa42bdcdbe
title: 什么是 tsconfig 文件，为什么在 TypeScript 项目中包含它很重要？
challengeType: 19
dashedName: what-is-a-tsconfig-file-and-why-is-it-important-to-include-in-your-typescript-projects
---

# --description--

TypeScript 的编译器设置可以配置以满足你的项目需求。该配置位于项目根目录中的 `tsconfig.json` 文件中。实际上，没有它，除非你直接传递命令标志，否则编译器将无法运行。但这个文件到底是做什么的呢？让我们来看一个示例文件：

```json
{
  "compilerOptions": {
    "rootDir": "./src",
    "outDir": "./prod",
    "lib": ["ES2023"],
    "target": "ES2023",
    "module": "ES2022",
    "moduleResolution": "Node",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "strict": true
  },
  "exclude": ["test/"]
}
```

这看起来很多！让我们分解一下。`compilerOptions` 属性将包含你配置的"核心内容" - 这里你可以控制 TypeScript 编译器的行为。看看那个嵌套对象...

`rootDir` 和 `outDir` 告诉 TypeScript 哪个目录包含你的源文件，哪个目录应该包含编译后的 JavaScript 代码。

`lib` 属性确定编译器使用哪些类型定义，并允许你包含对特定 ES 版本、DOM 等的支持。

`module` 和 `moduleResolution` 实际上协同工作来管理你的包如何使用模块 - 无论是 CommonJS 还是 ECMAScript。

`esModuleInterop` 通过自动为导入创建命名空间对象，允许 CommonJS 和 ES 模块之间更顺畅的互操作性，使你在 TypeScript 项目中更容易一起使用来自不同系统的模块，而 `skipLibCheck` 选项在你的代码中不被导入引用的 `.d.ts` 文件时跳过验证。

最后我们到达了 `strict` 模式。有人可能会争辩说，没有启用这个标志，TypeScript 真的没有帮助，因为它切换了相当多的其他检查，比如要求你正确处理可空类型，或者在 TypeScript 无法推断类型并回退到 any 时发出警告。

在我们结束之前，关于顶层 `exclude` 属性的快速说明 - 当你定义了源目录后，你可能在该目录之外有 TypeScript 代码，但你不希望将其编译为生产代码的一部分。例如，你的测试代码。`exclude` 数组告诉编译器在编译期间忽略这些 TypeScript 文件，但仍允许像 Intellisense 这样的工具暴露潜在问题。

还有许多其他编译器选项你可以探索 - 超过 50 个！我鼓励你探索文档并进行实验，找到适合你项目需求的配置。

# --questions--

## --text--

`tsconfig.json` 文件中的哪个属性影响编译器的行为？

## --answers--

`rootDir`

### --feedback--

这个属性是一个包含编译器选项的对象。

---

`compilerOptions`

---

`exclude`

### --feedback--

这个属性是一个包含编译器选项的对象。

---

`lib`

### --feedback--

这个属性是一个包含编译器选项的对象。

## --video-solution--

2

## --text--

`tsconfig.json` 文件中的 `strict` 选项是做什么的？

## --answers--

它只检查可空类型。

### --feedback--

这个选项启用了各种检查，包括可空类型的处理。

---

它强制使用 CommonJS 模块。

### --feedback--

这个选项启用了各种检查，包括可空类型的处理。

---

它切换几种类型检查选项。

---

它在编译期间排除测试文件。

### --feedback--

这个选项启用了各种检查，包括可空类型的处理。

## --video-solution--

3

## --text--

`tsconfig.json` 文件中的 `exclude` 数组的目的是什么？

## --answers--

指定要编译的文件。

### --feedback--

你可以使用它来在编译期间排除测试代码。

---

列出要包含的其他库。

### --feedback--

你可以使用它来在编译期间排除测试代码。

---

在编译期间忽略某些文件。

---

定义编译文件的输出目录。

### --feedback--

你可以使用它来在编译期间排除测试代码。

## --video-solution--

3