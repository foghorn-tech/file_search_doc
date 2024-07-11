# Assistants API Guide

## OpenAI

The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and files to respond to user queries. The Assistants API currently supports three types of tools: Code Interpreter, File Search, and Function calling.

You can explore the capabilities of the Assistants API using the Assistants playground or by building a step-by-step integration outlined in this guide.

A typical integration of the Assistants API has the following flow:

1. Create an Assistant by defining its custom instructions and picking a model. If helpful, add files and enable tools like Code Interpreter, File Search, and Function calling.
2. Create a Thread when a user starts a conversation.
3. Add Messages to the Thread as the user asks questions.
4. Run the Assistant on the Thread to generate a response by calling the model and the tools.