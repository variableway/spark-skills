# Task Features

## Task 1: 创建Local Task Tracking

当前github workflow skill是把任务内容和更新内容会写到github，这个skill是在执行任务的时候更新到GITHUB的内容
在本地也记录一下：
1. 把Task原始内容和Agent解析过后的内容本地记录到tracing folder
2. Task完成之后Update Issue的内容也更新到步骤1写入的文件中
3. 写入的文件是markdown文件，名字按照task文件名称命名，如果后续还是这个文件里面的Task，可以继续往这个文件添加内容
4. 更新github task init skill，加入tracing folder