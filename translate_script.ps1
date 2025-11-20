$folderPath = "e:\1.work\byy\在线课程\blocks\blocks_english\workshop-todo-app"
$files = Get-ChildItem -Path $folderPath -Filter "*.md"
$count = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # 替换常见的英文短语
    $content = $content -replace "You should use", "你应该使用"
    $content = $content -replace "You should assign", "你应该将"
    $content = $content -replace "Don't forget to use", "别忘了使用"
    $content = $content -replace "to declare the variable", "来声明变量"
    $content = $content -replace "to access the", "来访问"
    $content = $content -replace "element to the variable", "元素赋值给变量"
    $content = $content -replace "You need to", "你需要"
    $content = $content -replace "This time you need the", "这次你需要"
    $content = $content -replace "Save them in the variables", "将它们保存在变量"
    $content = $content -replace "method\. Save them", "方法。将它们保存"
    
    # 保存文件（仅当内容有变化时）
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        $count++
        Write-Host "已处理: $($file.Name)"
    }
}

Write-Host "`n总共处理了 $count 个文件"
