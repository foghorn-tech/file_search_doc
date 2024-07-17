
## version 0

原有的prompt

## version 1

修改为 技术方案 替换原有的 prompt

- 相对于 version 0 由于prompt过长，效果变差了很多
- 丢失 build streamlit app的上下文

## version 2

在version 1 的基础上，将技术方案拆分成多个 message 给到GPT

- 代码相对于之前来说更合理了
- build streamlit app 的上下文依旧丢失了


## version 3

修改了下 prompt 强调了最后生成的python代码要是streamlit代码

- 效果接近预期的结果
- 但会把 step 通过 st.header 展示
- Notion 和 Airtable 可以跑通， 但流程上还是不那么丝滑，是技术方案喂的文档有问题


## version 4

修改技术方案notion和airtable的文档

补充了一个chat.completions.create api 文档，希望能修复 An app that ask open ai to generate a dinner list的问题
(实际使用不行，因为prompt里面没提到 chat completions , 也不会检索到这个文档，但tech solution的文档里面带上了错误的代码，会导致生成的代码有问题)

## version 5

不让 tech assistant 里面生成代码， 只保留技术方案
- 结果变得更差了，还在定位原因