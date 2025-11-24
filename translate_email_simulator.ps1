# 定义函数来翻译单个文件
function Translate-File {
    param(
        [string]$FilePath
    )
    
    # 读取文件内容
    $content = Get-Content $FilePath -Raw
    
    # 翻译标题
    $content = $content -replace "Step (\d+)", "第 `$1 步"
    
    # 翻译描述部分
    $content = $content -replace "In this workshop, you are going to build an \*Email Simulator\* that simulates sending, receiving, and managing emails between different users. You'll learn about classes, objects, and how to organize code in an object-oriented way.", "在这个工作坊中，你将会构建一个*电子邮件模拟器*，它可以模拟不同用户之间发送、接收和管理电子邮件的过程。通过这个项目，你会学到类、对象以及如何以面向对象的方式组织代码。"
    
    $content = $content -replace "Begin by creating a class named `Email` using the `class` keyword.", "让我们从创建一个名为 Email 的类开始吧，要使用 class 关键字哦！"
    
    $content = $content -replace "Your `Email` class needs to store information about each email when it's created.", "你的 Email 类需要在创建每封邮件时存储相关信息。"
    
    $content = $content -replace "Inside your `Email` class, remove the existing `pass` keyword and create the `__init__` method that takes `self`, `sender`, `receiver`, `subject`, and `body` as parameters.", "在你的 Email 类中，移除现有的 pass 关键字并创建 __init__ 方法，该方法接受 self、sender、receiver、subject 和 body 作为参数。"
    
    $content = $content -replace "Inside the `__init__` method, you need to assign the parameter values to the object's attributes so each email can store its information.", "在 __init__ 方法中，你需要将参数值分配给对象的属性，这样每封邮件都可以存储自己的信息。"
    
    $content = $content -replace "Inside your `__init__` method, remove the `pass` keyword and assign the parameters to `self.sender`, `self.receiver`, `self.subject`, and `self.body`.", "在你的 __init__ 方法中，移除 pass 关键字并将参数分配给 self.sender、self.receiver、self.subject 和 self.body。"
    
    $content = $content -replace "You should create a class named `Email`.", "你应该创建一个名为 Email 的类。"
    
    $content = $content -replace "You should define an `__init__` method inside the `Email` class.", "你应该在 Email 类中定义一个 __init__ 方法。"
    
    $content = $content -replace "Your `__init__` method should have parameters: `self`, `sender`, `receiver`, `subject`, and `body`.", "你的 __init__ 方法应该有参数：self、sender、receiver、subject 和 body。"
    
    $content = $content -replace "You should assign the `sender` parameter to `self.sender`.", "你应该将 sender 参数分配给 self.sender。"
    
    $content = $content -replace "You should assign the `receiver` parameter to `self.receiver`.", "你应该将 receiver 参数分配给 self.receiver。"
    
    $content = $content -replace "You should assign the `subject` parameter to `self.subject`.", "你应该将 subject 参数分配给 self.subject。"
    
    # 写入翻译后的内容回原文件
    $content | Out-File -FilePath $FilePath -Encoding UTF8
}

# 获取所有Markdown文件
$files = Get-ChildItem -Path "f:\code\blocks_Chinese\blocks_english\workshop-email-simulator" -Filter "*.md"

# 遍历每个文件并翻译
foreach ($file in $files) {
    Write-Host "正在翻译文件: $($file.Name)"
    Translate-File -FilePath $file.FullName
    Write-Host "已完成翻译: $($file.Name)"
}

Write-Host "所有文件翻译完成！"