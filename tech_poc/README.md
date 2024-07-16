
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


## version 4
