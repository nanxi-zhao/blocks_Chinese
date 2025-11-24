import os
import re

# 定义需要翻译的文件夹路径
folder_path = r'f:\code\blocks_Chinese\blocks_english\workshop-email-simulator'

# 获取所有markdown文件
files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

# 翻译映射字典
translations = {
    # 标题翻译
    r'title: Step (\d+)': r'title: 第 \1 步',
    
    # 常见短语翻译
    r'In this workshop, you are going to build an \*Email Simulator\* that simulates sending, receiving, and managing emails between different users. You\'ll learn about classes, objects, and how to organize code in an object-oriented way.': 
    r'在这个工作坊中，你将会构建一个*电子邮件模拟器*，它可以模拟不同用户之间发送、接收和管理电子邮件的过程。通过这个项目，你会学到类、对象以及如何以面向对象的方式组织代码。',
    
    r'Begin by creating a class named `Email` using the `class` keyword.': 
    r'让我们从创建一个名为 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 的类开始吧，要使用 [class](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 关键字哦！',
    
    r'Your `Email` class needs to store information about each email when it\'s created.': 
    r'你的 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类需要在创建每封邮件时存储相关信息。',
    
    r'Inside your `Email` class, remove the existing `pass` keyword and create the `__init__` method that takes `self`, `sender`, `receiver`, `subject`, and `body` as parameters.': 
    r'在你的 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类中，移除现有的 [pass](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ef95ccc27660275692cd.md#L21-L21) 关键字并创建 [__init__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 方法，该方法接受 [self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40)、[sender](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21)、[receiver](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21)、[subject](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 和 [body](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 作为参数。',
    
    r'Inside the `__init__` method, you need to assign the parameter values to the object\'s attributes so each email can store its information.': 
    r'在 [__init__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 方法中，你需要将参数值分配给对象的属性，这样每封邮件都可以存储自己的信息。',
    
    r'Inside your `__init__` method, remove the `pass` keyword and assign the parameters to `self.sender`, `self.receiver`, `self.subject`, and `self.body`.': 
    r'在你的 [__init__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 方法中，移除 [pass](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ef95ccc27660275692cd.md#L21-L21) 关键字并将参数分配给 [self.sender](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L22-L22)、[self.receiver](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L23-L23)、[self.subject](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L24-L24) 和 [self.body](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L25-L25)。',
    
    r'You should create a class named `Email`.': 
    r'你应该创建一个名为 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 的类。',
    
    r'You should define an `__init__` method inside the `Email` class.': 
    r'你应该在 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类中定义一个 [__init__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 方法。',
    
    r'Your `__init__` method should have parameters: `self`, `sender`, `receiver`, `subject`, and `body`.': 
    r'你的 [__init__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 方法应该有参数：[self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40)、[sender](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21)、[receiver](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21)、[subject](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 和 [body](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21)。',
    
    r'You should assign the `sender` parameter to `self.sender`.': 
    r'你应该将 [sender](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 参数分配给 [self.sender](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L22-L22)。',
    
    r'You should assign the `receiver` parameter to `self.receiver`.': 
    r'你应该将 [receiver](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 参数分配给 [self.receiver](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L23-L23)。',
    
    r'You should assign the `subject` parameter to `self.subject`.': 
    r'你应该将 [subject](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 参数分配给 [self.subject](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L24-L24)。',
    
    r'You should assign the `body` parameter to `self.body`.': 
    r'你应该将 [body](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 参数分配给 [self.body](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L25-L25)。',
    
    r'Now let\'s test the `Email` class by creating an email object and checking that it stores information correctly. You\'ll print a couple of attributes to verify everything works.': 
    r'现在让我们通过创建一个电子邮件对象来测试 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类，并检查它是否正确地存储了信息。你可以打印几个属性来验证一切是否正常工作。',
    
    r'Create an email object named `email_obj` with `alice@example.com` as the sender, `bob@example.com` as the receiver,  `Hello` as the subject, and `Hi Bob!` as the body. Then print the `sender` and `subject` attributes as separate print statements to verify they are stored correctly.': 
    r'创建一个名为 [email_obj](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f0c3fcedb964ab959921.md#L21-L21) 的电子邮件对象，发件人设置为 alice@example.com，收件人设置为 bob@example.com，主题设置为 [Hello](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f70470f45d9c280af659.md#L23-L23)，正文设置为 Hi Bob!。然后分别打印 [sender](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 和 [subject](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f01116912861c7d1b0e6.md#L21-L21) 属性，以验证它们被正确存储。',
    
    r'You should create an email object named `email_obj` with the specified parameters.': 
    r'你应该创建一个名为 [email_obj](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f0c3fcedb964ab959921.md#L21-L21) 的电子邮件对象，并指定相应参数。',
    
    r'You should print `email_obj.sender`.': 
    r'你应该打印 [email_obj.sender](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f0c3fcedb964ab959921.md#L23-L23)。',
    
    r'You should print `email_obj.subject`.': 
    r'你应该打印 [email_obj.subject](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f0c3fcedb964ab959921.md#L24-L24)。',
    
    r'Now let\'s test that the `read` attribute was added correctly to your `Email` class. Since you already have an email object from the previous steps, print the `read` attribute to see that it\'s now `False` by default.': 
    r'现在让我们测试一下 [read](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68593ea22eac7e228ed585ce.md#L21-L21) 属性是否已正确添加到你的 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类中。由于你已经在前面的步骤中有了一个电子邮件对象，所以打印 [read](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68593ea22eac7e228ed585ce.md#L21-L21) 属性，看看它现在默认为 [False](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68593ea22eac7e228ed585ce.md#L21-L21)。',
    
    r'You should print `email_obj.read` to test the read attribute.': 
    r'你应该打印 [email_obj.read](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68593ea22eac7e228ed585ce.md#L21-L21) 来测试 [read](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68593ea22eac7e228ed585ce.md#L21-L21) 属性。',
    
    r'Now let\'s test the `has_been_read` attribute. Print `email_obj.has_been_read` to see that it\'s `False` by default.': 
    r'现在让我们测试一下 [has_been_read](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f06fdde1b4634a263f03.md#L21-L21) 属性。打印 [email_obj.has_been_read](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f06fdde1b4634a263f03.md#L21-L21) 看看它默认是 [False](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f06fdde1b4634a263f03.md#L21-L21)。',
    
    r'You should print `email_obj.has_been_read` to test the attribute.': 
    r'你应该打印 [email_obj.has_been_read](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f06fdde1b4634a263f03.md#L21-L21) 来测试这个属性。',
    
    r'Now that users can send emails, they need a way to store emails they receive. Each user should have an inbox to collect their emails.': 
    r'现在用户可以发送电子邮件了，他们还需要一种方式来存储收到的邮件。每个用户都应该有一个收件箱来收集他们的邮件。',
    
    r'Add an `inbox` attribute to the `User` class `__init__` method and initialize it as an empty list `[]`. This will store all emails that the user receives.': 
    r'在 [User](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L21-L21) 类的 [__init__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L22-L22) 方法中添加一个 [inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f2da9b8ed891e9fdc5fc.md#L27-L27) 属性，并将其初始化为空列表 []。这将存储用户收到的所有邮件。',
    
    r'You should add `self.inbox = []` to the `User` class `__init__` method.': 
    r'你应该在 [User](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L21-L21) 类的 [__init__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L22-L22) 方法中添加 [self.inbox = []](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f2da9b8ed891e9fdc5fc.md#L27-L27)。',
    
    r'Now let\'s display the sender and receiver information. To show who sent and received the email, add two print statements to the `display_full_email` method in this format:': 
    r'现在让我们显示发件人和收件人信息。为了显示谁发送和接收了邮件，向 [display_full_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L31-L31) 方法中添加两个打印语句，格式如下：',
    
    r'- `From: sender` where `sender` is replaced with the sender\'s name': 
    r'- From: sender 其中 sender 被替换为发件人的名字',
    
    r'- `To: receiver` where `receiver` is replaced with the receiver\'s name': 
    r'- To: receiver 其中 receiver 被替换为收件人的名字',
    
    r'You should use f-strings to print the sender\'s name using `From: {self.sender.name}`.': 
    r'你应该使用 f-string 来打印发件人姓名，使用 From: {self.sender.name}。',
    
    r'You should use f-strings to print the receiver\'s name using `To: {self.receiver.name}`.': 
    r'你应该使用 f-string 来打印收件人姓名，使用 To: {self.receiver.name}。',
    
    r'Let\'s add a string representation to our `Email` class so we can display brief email summaries.': 
    r'让我们为 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类添加一个字符串表示形式，这样我们就可以显示简短的邮件摘要了。',
    
    r'Add a `__str__` method to the `Email` class that takes `self` as a parameter.': 
    r'在 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类中添加一个接受 [self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40) 作为参数的 [__str__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L49-L49) 方法。',
    
    r'You should define a `__str__` method in the `Email` class.': 
    r'你应该在 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类中定义一个 [__str__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L49-L49) 方法。',
    
    r'Now you\'ll create a method to list all emails in the inbox. This method should handle the case where the inbox is empty and display a numbered list of emails when there are emails present.': 
    r'现在你将创建一个方法来列出收件箱中的所有邮件。这个方法应该处理收件箱为空的情况，并在有邮件时显示编号列表。',
    
    r'Add a method called `list_emails` to your `Inbox` class that takes `self` as a parameter. First, create an `if` statement to check if the inbox is empty by testing the `emails` list. If it\'s empty, print the message `Your inbox is empty.\\n`. Add a `return` statement to exit the method.': 
    r'在你的 [Inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f34ff93594934f6636d9.md#L37-L37) 类中添加一个名为 [list_emails](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L39-L47) 的方法，该方法接受 [self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40) 作为参数。首先，创建一个 [if](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L40-L40) 语句，通过测试 [emails](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f34ff93594934f6636d9.md#L39-L39) 列表来检查收件箱是否为空。如果为空，打印消息 Your inbox is empty.\\n。添加一个 [return](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L43-L43) 语句退出该方法。',
    
    r'You should define a method named `list_emails` in the `Inbox` class that takes `self` as a parameter.': 
    r'你应该在 [Inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f34ff93594934f6636d9.md#L37-L37) 类中定义一个名为 [list_emails](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L39-L47) 的方法，该方法接受 [self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40) 作为参数。',
    
    r'You should check if `self.emails` is empty using `if not self.emails`.': 
    r'你应该使用 [if not self.emails](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L40-L40) 来检查 [self.emails](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f34ff93594934f6636d9.md#L39-L39) 是否为空。',
    
    r'You should print the message `Your inbox is empty.\\n` if there are no emails.': 
    r'如果没有邮件，你应该打印消息 Your inbox is empty.\\n。',
    
    r'You should have a `return` statement at the end of the `if` statement.': 
    r'你应该在 [if](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L40-L40) 语句的末尾有一个 [return](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L43-L43) 语句。',
    
    r'After the empty inbox check, print the message `\\nYour Emails:`. After that, iterate over all emails in the inbox using a `for` loop with enumeration. This is the syntax for enumeration with a starting number: `enumerate\(iterable, start=start_number\)`.': 
    r'在检查收件箱是否为空之后，打印消息 \\nYour Emails:。之后，使用带有枚举的 [for](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45) 循环遍历收件箱中的所有邮件。这是带起始数字的枚举语法：enumerate(iterable, start=start_number)。',
    
    r'Use enumeration to number the emails starting from `1`. Use `i` \(the index\) and `email` \(the email object\) as the iteration variables.': 
    r'使用枚举从 1 开始对邮件进行编号。使用 [i](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45)（索引）和 [email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45)（邮件对象）作为迭代变量。',
    
    r'Inside the loop, print an f-string with the iteration index followed by a `\.`, then a space and the string representation of the email object in this format:': 
    r'在循环内部，打印一个 f-string，包含迭代索引后跟一个 .，然后是一个空格和邮件对象的字符串表示形式，格式如下：',
    
    r'```md': r'',
    r'i\. string_representation': r'i. string_representation',
    r'```': r'',
    
    r'Where `i` is the index and `string_representation` is the representation of the email object.': 
    r'其中 [i](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45) 是索引，string_representation 是邮件对象的表示形式。',
    
    r'You should print the header `\\nYour Emails:` outside the `if` statement.': 
    r'你应该在 [if](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L40-L40) 语句外部打印头部 \\nYour Emails:。',
    
    r'You should have a `for` loop that iterates over `enumerate\(self\.emails, start=1\)`.': 
    r'你应该有一个 [for](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45) 循环，遍历 enumerate(self.emails, start=1)。',
    
    r'Your `for` loop should use `i` and `email` to iterate over `enumerate\(self\.emails, start=1\)`.': 
    r'你的 [for](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45) 循环应该使用 [i](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45) 和 [email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L45-L45) 遍历 enumerate(self.emails, start=1)。',
    
    r'Inside the loop, you should print each email summary with a numbered prefix followed by the formatted string from the `__str__` method\. Don\'t forget to add a `.` after the number.': 
    r'在循环内部，你应该打印每个带有编号前缀的邮件摘要，后面跟着 [__str__](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L49-L49) 方法中的格式化字符串。别忘了在数字后面加上一个 .。',
    
    r'Now we\'re ready to add timestamps to our emails to track when they were sent and received.': 
    r'现在我们准备为电子邮件添加时间戳，以跟踪它们的发送和接收时间。',
    
    r'First, import the `datetime` module at the top of your file.': 
    r'首先，在文件顶部导入 [datetime](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f553d90a2f9874ff9d0e.md#L17-L17) 模块。',
    
    r'You should import the datetime module at the top of the file using `import datetime`.': 
    r'你应该使用 [import datetime](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f553d90a2f9874ff9d0e.md#L17-L17) 在文件顶部导入 datetime 模块。',
    
    r'Great! Now that you\'ve practiced datetime formatting, remove the `current_time` variable and the print statement from the bottom of your code. We\'ll integrate timestamps into the `Email` class in the next step.': 
    r'太棒了！现在你已经练习了 datetime 格式化，从代码底部删除 [current_time](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f68dd3affa9adb2e6d99.md#L107-L107) 变量和打印语句。我们将在下一步将时间戳集成到 [Email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852ea0c3cadb54e897acdac.md#L17-L17) 类中。',
    
    r'You should not have the the statement `current_time = datetime\.datetime\.now\(\)"` in your code.': 
    r'你的代码中不应该有语句 [current_time = datetime.datetime.now()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f68dd3affa9adb2e6d99.md#L107-L107)。',
    
    r'You should not have the practice print statement with `strftime\(\)` in your code.': 
    r'你的代码中不应该有使用 [strftime()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f68dd3affa9adb2e6d99.md#L108-L108) 的练习打印语句。',
    
    r'Now let\'s show the timestamp when displaying the full email.': 
    r'现在让我们在显示完整邮件时显示时间戳。',
    
    r'Below the subject, print the received timestamp using `strftime` to format it as `\'%Y-%m-%d %H:%M\'`\. Use the following format:': 
    r'在主题下方，使用 [strftime](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f68dd3affa9adb2e6d99.md#L108-L108) 打印接收时间戳，并将其格式化为 [%Y-%m-%d %H:%M](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f70470f45d9c280af659.md#L25-L25)。使用以下格式：',
    
    r'Received: date': r'Received: date',
    
    r'Where `date` is formatted as `\'%Y-%m-%d %H:%M\'`\.': 
    r'其中 [date](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f553d90a2f9874ff9d0e.md#L17-L17) 格式化为 [%Y-%m-%d %H:%M](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f70470f45d9c280af659.md#L25-L25)。',
    
    r'You should print the formatted timestamp using `self\.timestamp\.strftime\(\'%Y-%m-%d %H:%M\'\)`. Add `Received:` followed by a space before it.': 
    r'你应该使用 [self.timestamp.strftime('%Y-%m-%d %H:%M')](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f70470f45d9c280af659.md#L21-L21) 打印格式化的时间戳。在它前面添加 [Received:](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f70470f45d9c280af659.md#L25-L25) 和一个空格。',
    
    r'Users should be able to check their inbox, read emails, and delete emails directly through their User object.': 
    r'用户应该能够直接通过他们的 User 对象查看收件箱、阅读邮件和删除邮件。',
    
    r'For checking the inbox, add a method called `check_inbox` to the `User` class\. This method should print a personalized header with the user\'s name and then display all their emails.': 
    r'对于查看收件箱，在 [User](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L21-L21) 类中添加一个名为 [check_inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L51-L54) 的方法。这个方法应该打印一个包含用户名的个性化头部，然后显示他们的所有邮件。',
    
    r'The header should be formatted as: `\\nName\'s Inbox:`, where `Name` is replaced with the name of the user.': 
    r'头部应该格式化为：[\nName's Inbox:](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L53-L53)，其中 [Name](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f2da9b8ed891e9fdc5fc.md#L27-L27) 被替换为用户的姓名。',
    
    r'After printing the header, call the `list_emails\(\)` method on the user\'s inbox.': 
    r'打印头部后，调用用户收件箱的 [list_emails()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L39-L47) 方法。',
    
    r'You should define a method named `check_inbox` in the `User` class that takes `self` as a parameter.': 
    r'你应该在 [User](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L21-L21) 类中定义一个名为 [check_inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L51-L54) 的方法，该方法接受 [self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40) 作为参数。',
    
    r'Within `check_inbox`, you should print a header that includes the user\'s name in the format `\\n\[user\]\'s Inbox:`.': 
    r'在 [check_inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L51-L54) 中，你应该打印一个包含用户名的头部，格式为 [\n[user]'s Inbox:](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L53-L53)。',
    
    r'Within `check_inbox`, you should call `self\.inbox\.list_emails\(\)` to display the emails.': 
    r'在 [check_inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L51-L54) 中，你应该调用 [self.inbox.list_emails()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4584f508e95cc7a9f4d.md#L39-L47) 来显示邮件。',
    
    r'For reading and deleting emails, add two methods to your `User` class: `read_email` and `delete_email`\. Both should take an `index` parameter and call the corresponding method on `self\.inbox`\.': 
    r'对于阅读和删除邮件，在你的 [User](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L21-L21) 类中添加两个方法：[read_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f996671e63a0b4fbf143.md#L21-L21) 和 [delete_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4ded9f84896ff182dd8.md#L90-L90)。两者都应该接受一个 [index](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4ded9f84896ff182dd8.md#L80-L80) 参数并调用 [self.inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L54-L54) 上的相应方法。',
    
    r'You should define a method named `read_email` in the `User` class that takes `self` and `index` as parameters.': 
    r'你应该在 [User](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L21-L21) 类中定义一个名为 [read_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f996671e63a0b4fbf143.md#L21-L21) 的方法，该方法接受 [self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40) 和 [index](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4ded9f84896ff182dd8.md#L80-L80) 作为参数。',
    
    r'The `read_email` method should call `self\.inbox\.read_email\(index\)`.': 
    r'[read_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f996671e63a0b4fbf143.md#L21-L21) 方法应该调用 [self.inbox.read_email(index)](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f996671e63a0b4fbf143.md#L21-L21)。',
    
    r'You should define a method named `delete_email` in the `User` class that takes `self` and `index` as parameters.': 
    r'你应该在 [User](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6852f11d412c29665985a915.md#L21-L21) 类中定义一个名为 [delete_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4ded9f84896ff182dd8.md#L90-L90) 的方法，该方法接受 [self](file:///F:/code/blocks_Chinese/blocks_english/lecture-working-with-classes-and-objects/6852d829161bd898603c0643.md#L35-L40) 和 [index](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4ded9f84896ff182dd8.md#L80-L80) 作为参数。',
    
    r'The `delete_email` method should call `self\.inbox\.delete_email\(index\)`.': 
    r'[delete_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4ded9f84896ff182dd8.md#L90-L90) 方法应该调用 [self.inbox.delete_email(index)](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f996671e63a0b4fbf143.md#L29-L29)。',
    
    r'Before sending the emails, add the standard Python idiom `if __name__ == \'__main__\':` followed by a call to `main\(\)`\. This ensures that the main function only runs when the script is executed directly, not when it\'s imported as a module.': 
    r'在发送邮件之前，添加标准的 Python 习惯用法 [if __name__ == '__main__':](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/685409f3f6c765aa4cd44a26.md#L127-L128) 然后调用 [main()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/685409f3f6c765aa4cd44a26.md#L128-L128)。这确保了主函数只在直接执行脚本时运行，而不是在作为模块导入时运行。',
    
    r'You should add the `if __name__ == \'__main__\':` check outside the `main` function.': 
    r'你应该在 [main](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/685409f3f6c765aa4cd44a26.md#L117-L125) 函数外部添加 [if __name__ == '__main__':](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/685409f3f6c765aa4cd44a26.md#L127-L128) 检查。',
    
    r'You should call `main\(\)` inside the `if __name__ == \'__main__\':` block.': 
    r'你应该在 [if __name__ == '__main__':](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/685409f3f6c765aa4cd44a26.md#L127-L128) 代码块内调用 [main()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/685409f3f6c765aa4cd44a26.md#L128-L128)。',
    
    r'Now you\'ll simulate sending some emails between the users.': 
    r'现在你将模拟用户之间发送一些邮件。',
    
    r'In your `main` function, after creating the users, use the `send_email` method to:': 
    r'在你的 [main](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L123-L128) 函数中，创建用户后，使用 [send_email](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L46-L46) 方法来：',
    
    r'- Have Tory send an email to the `ramy` user object with subject `Hello` and body `Hi Ramy, just saying hello!`\.': 
    r'- 让 Tory 向 [ramy](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L125-L125) 用户对象发送邮件，主题为 [Hello](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f70470f45d9c280af659.md#L23-L23)，正文为 [Hi Ramy, just saying hello!](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L25-L25)。',
    
    r'- Have Ramy send an email to the `tory` user object with subject `Re: Hello` and body `Hi Tory, hope you are fine.`\.': 
    r'- 让 Ramy 向 [tory](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L124-L124) 用户对象发送邮件，主题为 [Re: Hello](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L28-L28)，正文为 [Hi Tory, hope you are fine.](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L28-L28)。',
    
    r'You should have Tory send an email to `ramy`, subject `Hello`, and body `Hi Ramy, just saying hello!`\.': 
    r'你应该让 Tory 向 [ramy](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L125-L125) 发送邮件，主题为 [Hello](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f70470f45d9c280af659.md#L23-L23)，正文为 [Hi Ramy, just saying hello!](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L25-L25)。',
    
    r'You should have Ramy send an email to `tory`, subject `Re: Hello`, and body `Hi Tory, hope you are fine.`\.': 
    r'你应该让 Ramy 向 [tory](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L124-L124) 发送邮件，主题为 [Re: Hello](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L28-L28)，正文为 [Hi Tory, hope you are fine.](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L28-L28)。',
    
    r'Now you\'ll demonstrate the inbox functionality\. Ramy will check his inbox, read the first email, delete the second email, and then check his inbox again to see the changes.': 
    r'现在你将演示收件箱功能。Ramy 将检查他的收件箱，阅读第一封邮件，删除第二封邮件，然后再次检查他的收件箱以查看变化。',
    
    r'In your `main` function, after sending the emails, add code to:': 
    r'在你的 [main](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/68540a534c56aeabae6afd58.md#L123-L128) 函数中，发送邮件后，添加代码来：',
    
    r'- Have Ramy check his inbox  using the `check_inbox` method.': 
    r'- 使用 [check_inbox](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L51-L54) 方法让 Ramy 检查他的收件箱。',
    
    r'- Have Ramy read the first email.': 
    r'- 让 Ramy 阅读第一封邮件。',
    
    r'- Have Ramy delete the first email.': 
    r'- 让 Ramy 删除第一封邮件。',
    
    r'- Have Ramy check his inbox again.': 
    r'- 让 Ramy 再次检查他的收件箱。',
    
    r'With this, you have completed the email simulator!': 
    r'完成这些后，你就完成了电子邮件模拟器！',
    
    r'You should call `ramy\.check_inbox\(\)` to show Ramy\'s emails.': 
    r'你应该调用 [ramy.check_inbox()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L51-L54) 来显示 Ramy 的邮件。',
    
    r'You should call `ramy\.read_email\(1\)` to read the first email.': 
    r'你应该调用 [ramy.read_email(1)](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f996671e63a0b4fbf143.md#L21-L21) 来阅读第一封邮件。',
    
    r'You should call `ramy\.delete_email\(1\)` to delete the first email.': 
    r'你应该调用 [ramy.delete_email(1)](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f4ded9f84896ff182dd8.md#L90-L90) 来删除第一封邮件。',
    
    r'You should call `ramy\.check_inbox\(\)` again to show the updated inbox.': 
    r'你应该再次调用 [ramy.check_inbox()](file:///F:/code/blocks_Chinese/blocks_english/workshop-email-simulator/6853f90fd03acc9fd75ff860.md#L51-L54) 来显示更新后的收件箱。'
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