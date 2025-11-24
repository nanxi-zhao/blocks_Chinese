import os
import re

# 定义需要翻译的文件夹路径
folder_path = r'f:\code\blocks_Chinese\blocks_english\workshop-email-simulator'

# 获取所有markdown文件
files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

# 翻译映射字典
translations = {
    r'Step (\d+)': r'第 \1 步',
    r'In this workshop, you are going to build an \*Email Simulator\* that simulates sending, receiving, and managing emails between different users. You\'ll learn about classes, objects, and how to organize code in an object-oriented way.': 
    '在这个工作坊中，你将会构建一个*电子邮件模拟器*，它可以模拟不同用户之间发送、接收和管理电子邮件的过程。通过这个项目，你会学到类、对象以及如何以面向对象的方式组织代码。',
    r'Begin by creating a class named `Email` using the `class` keyword.': 
    '让我们从创建一个名为 Email 的类开始吧，要使用 class 关键字哦！',
    r'Your `Email` class needs to store information about each email when it\'s created.': 
    '你的 Email 类需要在创建每封邮件时存储相关信息。',
    r'Inside your `Email` class, remove the existing `pass` keyword and create the `__init__` method that takes `self`, `sender`, `receiver`, `subject`, and `body` as parameters.': 
    '在你的 Email 类中，移除现有的 pass 关键字并创建 __init__ 方法，该方法接受 self、sender、receiver、subject 和 body 作为参数。',
    r'Inside the `__init__` method, you need to assign the parameter values to the object\'s attributes so each email can store its information.': 
    '在 __init__ 方法中，你需要将参数值分配给对象的属性，这样每封邮件都可以存储自己的信息。',
    r'Inside your `__init__` method, remove the `pass` keyword and assign the parameters to `self.sender`, `self.receiver`, `self.subject`, and `self.body`.': 
    '在你的 __init__ 方法中，移除 pass 关键字并将参数分配给 self.sender、self.receiver、self.subject 和 self.body。',
    r'You should create a class named `Email`.': 
    '你应该创建一个名为 Email 的类。',
    r'You should define an `__init__` method inside the `Email` class.': 
    '你应该在 Email 类中定义一个 __init__ 方法。',
    r'Your `__init__` method should have parameters: `self`, `sender`, `receiver`, `subject`, and `body`.': 
    '你的 __init__ 方法应该有参数：self、sender、receiver、subject 和 body。',
    r'You should assign the `sender` parameter to `self.sender`.': 
    '你应该将 sender 参数分配给 self.sender。',
    r'You should assign the `receiver` parameter to `self.receiver`.': 
    '你应该将 receiver 参数分配给 self.receiver。',
    r'You should assign the `subject` parameter to `self.subject`.': 
    '你应该将 subject 参数分配给 self.subject。',
    r'You should assign the `body` parameter to `self.body`.': 
    '你应该将 body 参数分配给 self.body。',
    r'Now let\'s test the `Email` class by creating an email object and checking that it stores information correctly. You\'ll print a couple of attributes to verify everything works.': 
    '现在让我们通过创建一个电子邮件对象来测试 Email 类，并检查它是否正确地存储了信息。你可以打印几个属性来验证一切是否正常工作。',
    r'Create an email object named `email_obj` with `alice@example.com` as the sender, `bob@example.com` as the receiver,  `Hello` as the subject, and `Hi Bob!` as the body. Then print the `sender` and `subject` attributes as separate print statements to verify they are stored correctly.': 
    '创建一个名为 email_obj 的电子邮件对象，发件人设置为 alice@example.com，收件人设置为 bob@example.com，主题设置为 Hello，正文设置为 Hi Bob!。然后分别打印 sender 和 subject 属性，以验证它们被正确存储。',
    r'You should create an email object named `email_obj` with the specified parameters.': 
    '你应该创建一个名为 email_obj 的电子邮件对象，并指定相应参数。',
    r'You should print `email_obj.sender`.': 
    '你应该打印 email_obj.sender。',
    r'You should print `email_obj.subject`.': 
    '你应该打印 email_obj.subject。',
    r'Now let\'s test that the `read` attribute was added correctly to your `Email` class. Since you already have an email object from the previous steps, print the `read` attribute to see that it\'s now `False` by default.': 
    '现在让我们测试一下 read 属性是否已正确添加到你的 Email 类中。由于你已经在前面的步骤中有了一个电子邮件对象，所以打印 read 属性，看看它现在默认为 False。',
    r'You should print `email_obj.read` to test the read attribute.': 
    '你应该打印 email_obj.read 来测试 read 属性。',
    r'Now let\'s test the `has_been_read` attribute. Print `email_obj.has_been_read` to see that it\'s `False` by default.': 
    '现在让我们测试一下 has_been_read 属性。打印 email_obj.has_been_read 看看它默认是 False。',
    r'You should print `email_obj.has_been_read` to test the attribute.': 
    '你应该打印 email_obj.has_been_read 来测试这个属性。',
    r'Now that users can send emails, they need a way to store emails they receive. Each user should have an inbox to collect their emails.': 
    '现在用户可以发送电子邮件了，他们还需要一种方式来存储收到的邮件。每个用户都应该有一个收件箱来收集他们的邮件。',
    r'Add an `inbox` attribute to the `User` class `__init__` method and initialize it as an empty list `[]`. This will store all emails that the user receives.': 
    '在 User 类的 __init__ 方法中添加一个 inbox 属性，并将其初始化为空列表 []。这将存储用户收到的所有邮件。',
    r'You should add `self.inbox = []` to the `User` class `__init__` method.': 
    '你应该在 User 类的 __init__ 方法中添加 self.inbox = []。',
    r'Now let\'s display the sender and receiver information. To show who sent and received the email, add two print statements to the `display_full_email` method in this format:': 
    '现在让我们显示发件人和收件人信息。为了显示谁发送和接收了邮件，向 display_full_email 方法中添加两个打印语句，格式如下：',
    r'- `From: sender` where `sender` is replaced with the sender\'s name': 
    '- From: sender 其中 sender 被替换为发件人的名字',
    r'- `To: receiver` where `receiver` is replaced with the receiver\'s name': 
    '- To: receiver 其中 receiver 被替换为收件人的名字',
    r'You should use f-strings to print the sender\'s name using `From: {self.sender.name}`.': 
    '你应该使用 f-string 来打印发件人姓名，使用 From: {self.sender.name}。',
    r'You should use f-strings to print the receiver\'s name using `To: {self.receiver.name}`.': 
    '你应该使用 f-string 来打印收件人姓名，使用 To: {self.receiver.name}。',
    r'Let\'s add a string representation to our `Email` class so we can display brief email summaries.': 
    '让我们为 Email 类添加一个字符串表示形式，这样我们就可以显示简短的邮件摘要了。',
    r'Add a `__str__` method to the `Email` class that takes `self` as a parameter.': 
    '在 Email 类中添加一个接受 self 作为参数的 __str__ 方法。',
    r'You should define a `__str__` method in the `Email` class.': 
    '你应该在 Email 类中定义一个 __str__ 方法。',
    r'Now you\'ll create a method to list all emails in the inbox. This method should handle the case where the inbox is empty and display a numbered list of emails when there are emails present.': 
    '现在你将创建一个方法来列出收件箱中的所有邮件。这个方法应该处理收件箱为空的情况，并在有邮件时显示编号列表。',
    r'Add a method called `list_emails` to your `Inbox` class that takes `self` as a parameter. First, create an `if` statement to check if the inbox is empty by testing the `emails` list. If it\'s empty, print the message `Your inbox is empty.\\n`. Add a `return` statement to exit the method.': 
    '在你的 Inbox 类中添加一个名为 list_emails 的方法，该方法接受 self 作为参数。首先，创建一个 if 语句，通过测试 emails 列表来检查收件箱是否为空。如果为空，打印消息 Your inbox is empty.\\n。添加一个 return 语句退出该方法。',
    r'You should define a method named `list_emails` in the `Inbox` class that takes `self` as a parameter.': 
    '你应该在 Inbox 类中定义一个名为 list_emails 的方法，该方法接受 self 作为参数。',
    r'You should check if `self.emails` is empty using `if not self.emails`.': 
    '你应该使用 if not self.emails 来检查 self.emails 是否为空。',
    r'You should print the message `Your inbox is empty.\\n` if there are no emails.': 
    '如果没有邮件，你应该打印消息 Your inbox is empty.\\n。',
    r'You should have a `return` statement at the end of the `if` statement.': 
    '你应该在 if 语句的末尾有一个 return 语句。',
    r'After the empty inbox check, print the message `\\nYour Emails:`. After that, iterate over all emails in the inbox using a `for` loop with enumeration. This is the syntax for enumeration with a starting number: `enumerate\(iterable, start=start_number\)`.': 
    '在检查收件箱是否为空之后，打印消息 \\nYour Emails:。之后，使用带有枚举的 for 循环遍历收件箱中的所有邮件。这是带起始数字的枚举语法：enumerate(iterable, start=start_number)。',
    r'Use enumeration to number the emails starting from `1`. Use `i` \(the index\) and `email` \(the email object\) as the iteration variables.': 
    '使用枚举从 1 开始对邮件进行编号。使用 i（索引）和 email（邮件对象）作为迭代变量。',
    r'Inside the loop, print an f-string with the iteration index followed by a `\.`, then a space and the string representation of the email object in this format:': 
    '在循环内部，打印一个 f-string，包含迭代索引后跟一个 .，然后是一个空格和邮件对象的字符串表示形式，格式如下：',
    r'```md': '',
    r'i\. string_representation': 'i. string_representation',
    r'```': '',
    r'Where `i` is the index and `string_representation` is the representation of the email object.': 
    '其中 i 是索引，string_representation 是邮件对象的表示形式。',
    r'You should print the header `\\nYour Emails:` outside the `if` statement.': 
    '你应该在 if 语句外部打印头部 \\nYour Emails:。',
    r'You should have a `for` loop that iterates over `enumerate\(self\.emails, start=1\)`.': 
    '你应该有一个 for 循环，遍历 enumerate(self.emails, start=1)。',
    r'Your `for` loop should use `i` and `email` to iterate over `enumerate\(self\.emails, start=1\)`.': 
    '你的 for 循环应该使用 i 和 email 遍历 enumerate(self.emails, start=1)。',
    r'Inside the loop, you should print each email summary with a numbered prefix followed by the formatted string from the `__str__` method\. Don\'t forget to add a `.` after the number.': 
    '在循环内部，你应该打印每个带有编号前缀的邮件摘要，后面跟着 __str__ 方法中的格式化字符串。别忘了在数字后面加上一个 .。',
    r'Now we\'re ready to add timestamps to our emails to track when they were sent and received.': 
    '现在我们准备为电子邮件添加时间戳，以跟踪它们的发送和接收时间。',
    r'First, import the `datetime` module at the top of your file.': 
    '首先，在文件顶部导入 datetime 模块。',
    r'You should import the datetime module at the top of the file using `import datetime`.': 
    '你应该使用 import datetime 在文件顶部导入 datetime 模块。',
    r'Great! Now that you\'ve practiced datetime formatting, remove the `current_time` variable and the print statement from the bottom of your code. We\'ll integrate timestamps into the `Email` class in the next step.': 
    '太棒了！现在你已经练习了 datetime 格式化，从代码底部删除 current_time 变量和打印语句。我们将在下一步将时间戳集成到 Email 类中。',
    r'You should not have the the statement `current_time = datetime\.datetime\.now\(\)"` in your code.': 
    '你的代码中不应该有语句 current_time = datetime.datetime.now()。',
    r'You should not have the practice print statement with `strftime\(\)` in your code.': 
    '你的代码中不应该有使用 strftime() 的练习打印语句。',
    r'Now let\'s show the timestamp when displaying the full email.': 
    '现在让我们在显示完整邮件时显示时间戳。',
    r'Below the subject, print the received timestamp using `strftime` to format it as `\'%Y-%m-%d %H:%M\'`\. Use the following format:': 
    '在主题下方，使用 strftime 打印接收时间戳，并将其格式化为 \'%Y-%m-%d %H:%M\'。使用以下格式：',
    r'Received: date': 'Received: date',
    r'Where `date` is formatted as `\'%Y-%m-%d %H:%M\'`\.': 
    '其中 date 格式化为 \'%Y-%m-%d %H:%M\'。',
    r'You should print the formatted timestamp using `self\.timestamp\.strftime\(\'%Y-%m-%d %H:%M\'\)`. Add `Received:` followed by a space before it.': 
    '你应该使用 self.timestamp.strftime(\'%Y-%m-%d %H:%M\') 打印格式化的时间戳。在它前面添加 Received: 和一个空格。',
    r'Users should be able to check their inbox, read emails, and delete emails directly through their User object.': 
    '用户应该能够直接通过他们的 User 对象查看收件箱、阅读邮件和删除邮件。',
    r'For checking the inbox, add a method called `check_inbox` to the `User` class\. This method should print a personalized header with the user\'s name and then display all their emails.': 
    '对于查看收件箱，在 User 类中添加一个名为 check_inbox 的方法。这个方法应该打印一个包含用户名的个性化头部，然后显示他们的所有邮件。',
    r'The header should be formatted as: `\\nName\'s Inbox:`, where `Name` is replaced with the name of the user.': 
    '头部应该格式化为：\\nName\'s Inbox:，其中 Name 被替换为用户的姓名。',
    r'After printing the header, call the `list_emails\(\)` method on the user\'s inbox.': 
    '打印头部后，调用用户收件箱的 list_emails() 方法。',
    r'You should define a method named `check_inbox` in the `User` class that takes `self` as a parameter.': 
    '你应该在 User 类中定义一个名为 check_inbox 的方法，该方法接受 self 作为参数。',
    r'Within `check_inbox`, you should print a header that includes the user\'s name in the format `\\n\[user\]\'s Inbox:`.': 
    '在 check_inbox 中，你应该打印一个包含用户名的头部，格式为 \\n[user]\'s Inbox:。',
    r'Within `check_inbox`, you should call `self\.inbox\.list_emails\(\)` to display the emails.': 
    '在 check_inbox 中，你应该调用 self.inbox.list_emails() 来显示邮件。',
    r'For reading and deleting emails, add two methods to your `User` class: `read_email` and `delete_email`\. Both should take an `index` parameter and call the corresponding method on `self\.inbox`\.': 
    '对于阅读和删除邮件，在你的 User 类中添加两个方法：read_email 和 delete_email。两者都应该接受一个 index 参数并调用 self.inbox 上的相应方法。',
    r'You should define a method named `read_email` in the `User` class that takes `self` and `index` as parameters.': 
    '你应该在 User 类中定义一个名为 read_email 的方法，该方法接受 self 和 index 作为参数。',
    r'The `read_email` method should call `self\.inbox\.read_email\(index\)`.': 
    'read_email 方法应该调用 self.inbox.read_email(index)。',
    r'You should define a method named `delete_email` in the `User` class that takes `self` and `index` as parameters.': 
    '你应该在 User 类中定义一个名为 delete_email 的方法，该方法接受 self 和 index 作为参数。',
    r'The `delete_email` method should call `self\.inbox\.delete_email\(index\)`.': 
    'delete_email 方法应该调用 self.inbox.delete_email(index)。',
    r'Before sending the emails, add the standard Python idiom `if __name__ == \'__main__\':` followed by a call to `main\(\)`\. This ensures that the main function only runs when the script is executed directly, not when it\'s imported as a module.': 
    '在发送邮件之前，添加标准的 Python 习惯用法 if __name__ == \'__main__\': 然后调用 main()。这确保了主函数只在直接执行脚本时运行，而不是在作为模块导入时运行。',
    r'You should add the `if __name__ == \'__main__\':` check outside the `main` function.': 
    '你应该在 main 函数外部添加 if __name__ == \'__main__\': 检查。',
    r'You should call `main\(\)` inside the `if __name__ == \'__main__\':` block.': 
    '你应该在 if __name__ == \'__main__\': 代码块内调用 main()。',
    r'Now you\'ll simulate sending some emails between the users.': 
    '现在你将模拟用户之间发送一些邮件。',
    r'In your `main` function, after creating the users, use the `send_email` method to:': 
    '在你的 main 函数中，创建用户后，使用 send_email 方法来：',
    r'- Have Tory send an email to the `ramy` user object with subject `Hello` and body `Hi Ramy, just saying hello!`\.': 
    '- 让 Tory 向 ramy 用户对象发送邮件，主题为 Hello，正文为 Hi Ramy, just saying hello!。',
    r'- Have Ramy send an email to the `tory` user object with subject `Re: Hello` and body `Hi Tory, hope you are fine.`\.': 
    '- 让 Ramy 向 tory 用户对象发送邮件，主题为 Re: Hello，正文为 Hi Tory, hope you are fine.。',
    r'You should have Tory send an email to `ramy`, subject `Hello`, and body `Hi Ramy, just saying hello!`\.': 
    '你应该让 Tory 向 ramy 发送邮件，主题为 Hello，正文为 Hi Ramy, just saying hello!。',
    r'You should have Ramy send an email to `tory`, subject `Re: Hello`, and body `Hi Tory, hope you are fine.`\.': 
    '你应该让 Ramy 向 tory 发送邮件，主题为 Re: Hello，正文为 Hi Tory, hope you are fine.。',
    r'Now you\'ll demonstrate the inbox functionality\. Ramy will check his inbox, read the first email, delete the second email, and then check his inbox again to see the changes.': 
    '现在你将演示收件箱功能。Ramy 将检查他的收件箱，阅读第一封邮件，删除第二封邮件，然后再次检查他的收件箱以查看变化。',
    r'In your `main` function, after sending the emails, add code to:': 
    '在你的 main 函数中，发送邮件后，添加代码来：',
    r'- Have Ramy check his inbox  using the `check_inbox` method.': 
    '- 使用 check_inbox 方法让 Ramy 检查他的收件箱。',
    r'- Have Ramy read the first email.': 
    '- 让 Ramy 阅读第一封邮件。',
    r'- Have Ramy delete the first email.': 
    '- 让 Ramy 删除第一封邮件。',
    r'- Have Ramy check his inbox again.': 
    '- 让 Ramy 再次检查他的收件箱。',
    r'With this, you have completed the email simulator!': 
    '完成这些后，你就完成了电子邮件模拟器！',
    r'You should call `ramy\.check_inbox\(\)` to show Ramy\'s emails.': 
    '你应该调用 ramy.check_inbox() 来显示 Ramy 的邮件。',
    r'You should call `ramy\.read_email\(1\)` to read the first email.': 
    '你应该调用 ramy.read_email(1) 来阅读第一封邮件。',
    r'You should call `ramy\.delete_email\(1\)` to delete the first email.': 
    '你应该调用 ramy.delete_email(1) 来删除第一封邮件。',
    r'You should call `ramy\.check_inbox\(\)` again to show the updated inbox.': 
    '你应该再次调用 ramy.check_inbox() 来显示更新后的收件箱。'
}

# 遍历所有文件并翻译
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 应用翻译
    for pattern, replacement in translations.items():
        content = re.sub(pattern, replacement, content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'已翻译文件: {file_name}')

print('所有文件翻译完成！')