---
id: 67d301cc87b84eaa42bdcdbe
title: What Is a tsconfig File, and Why Is It Important to Include in Your TypeScript Projects?
challengeType: 19
dashedName: what-is-a-tsconfig-file-and-why-is-it-important-to-include-in-your-typescript-projects
---

# --description--

TypeScript 的编译器设置可以根据项目需求进行配置。这些配置通常放在项目根目录下的 `tsconfig.json` 文件中。事实上，如果没有该文件，编译器通常不会运行（除非你在命令行中显式传入参数）。那么这个文件具体做了什么呢？我们来看一个示例：

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

看起来选项挺多的，我们逐项拆解。`compilerOptions` 是配置的核心——在这里你控制 TypeScript 编译器的行为。

`rootDir` 和 `outDir` 告诉 TypeScript 源代码所在目录和编译后 JavaScript 应输出到哪个目录。

`lib` 决定编译器使用哪些类型定义，比如包含特定 ECMAScript 版本、DOM 等支持。

`module` 与 `moduleResolution` 配合控制模块系统的使用方式，例如 CommonJS 或 ECMAScript 模块。

`esModuleInterop` 可以在 CommonJS 与 ES 模块间提供更顺滑的互操作性，自动为导入创建命名空间对象，使不同模块系统的模块更易一起使用；`skipLibCheck` 则跳过对未被代码导入引用的 `.d.ts` 类型声明文件的校验以加快编译。

最后来说 `strict` 模式。有人认为如果不启用该标志，TypeScript 的帮助意义会大打折扣；`strict` 会开启一系列更严格的检查，例如要求合理处理可空类型，或在无法推断类型而回退到 `any` 时提示警告。

另外补充一下顶层 `exclude` 属性：当你指定了源目录后，可能会有一些 TypeScript 文件位于该目录之外（例如测试代码），你不希望它们被编译进生产代码中。`exclude` 数组会告诉编译器在编译时忽略这些文件，但像 Intellisense 这样的工具仍然可以暴露潜在问题。

TypeScript 还有很多其他编译选项（50 多项），建议你查阅文档并尝试不同配置，找到适合你项目的方案。

# --questions--

## --text--

Which property in the `tsconfig.json` file affects how the compiler behaves?

## --answers--

`rootDir`

### --feedback--

This property is an object containing options for the compiler.

---

`compilerOptions`

---

`exclude`

### --feedback--

This property is an object containing options for the compiler.

---

`lib`

### --feedback--

This property is an object containing options for the compiler.

## --video-solution--

2

## --text--

What does the `strict` option in the `tsconfig.json` file do?

## --answers--

It only checks for nullable types.

### --feedback--

This option enables various checks, including handling of nullable types.

---

It enforces the use of CommonJS modules.

### --feedback--

This option enables various checks, including handling of nullable types.

---

It toggles several type-checking options.

---

It excludes test files from compilation.

### --feedback--

This option enables various checks, including handling of nullable types.

## --video-solution--

3

## --text--

What is the purpose of the `exclude` array in the `tsconfig.json` file?

## --answers--

To specify which files to compile.

### --feedback--

You can use this to exclude test code from compilation.

---

To list additional libraries to include.

### --feedback--

You can use this to exclude test code from compilation.

---

To ignore certain files during compilation.

---

To define output directories for compiled files.

### --feedback--

You can use this to exclude test code from compilation.

## --video-solution--

3
