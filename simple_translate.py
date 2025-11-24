import os
import re

# 定义需要翻译的文件夹路径
folder_path = r'f:\code\blocks_Chinese\blocks_english\workshop-email-simulator'

# 获取所有markdown文件
files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

# 简单的翻译映射
translations = [
    (r'title: Step (\d+)', r'title: 第 \1 步'),
    (r'You should', r'你应该'),
    (r'In this workshop', r'在这个工作坊中'),
    (r'Email', r'电子邮件'),
    (r'class', r'类'),
    (r'method', r'方法'),
    (r'function', r'函数'),
    (r'parameter', r'参数'),
    (r'attribute', r'属性'),
    (r'object', r'对象'),
    (r'user', r'用户'),
    (r'print', r'打印'),
    (r'create', r'创建'),
    (r'add', r'添加'),
    (r'remove', r'移除'),
    (r'delete', r'删除'),
    (r'read', r'阅读'),
    (r'send', r'发送'),
    (r'receive', r'接收'),
    (r'inbox', r'收件箱'),
    (r'subject', r'主题'),
    (r'body', r'正文'),
    (r'sender', r'发件人'),
    (r'receiver', r'收件人'),
    (r'datetime', r'日期时间'),
    (r'module', r'模块'),
    (r'import', r'导入'),
    (r'format', r'格式化'),
    (r'timestamp', r'时间戳'),
    (r'list', r'列表'),
    (r'empty', r'空的'),
    (r'begin', r'开始'),
    (r'start', r'开始'),
    (r'end', r'结束'),
    (r'first', r'第一'),
    (r'second', r'第二'),
    (r'third', r'第三'),
    (r'call', r'调用'),
    (r'name', r'名字'),
    (r'check', r'检查'),
    (r'Great', r'太棒了'),
    (r'Now', r'现在'),
    (r'Let\'s', r'让我们'),
    (r'After', r'之后'),
    (r'Before', r'之前'),
    (r'Inside', r'在...内部'),
    (r'outside', r'外部'),
    (r'default', r'默认'),
    (r'assign', r'分配'),
    (r'value', r'值'),
    (r'variable', r'变量'),
    (r'test', r'测试'),
    (r'verify', r'验证'),
    (r'correct', r'正确'),
    (r'incorrect', r'不正确'),
    (r'working', r'工作'),
    (r'completed', r'完成'),
    (r'simulator', r'模拟器')
]

# 遍历所有文件并翻译
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 应用翻译
    for pattern, replacement in translations:
        content = re.sub(pattern, replacement, content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'已翻译文件: {file_name}')

print('所有文件翻译完成！')