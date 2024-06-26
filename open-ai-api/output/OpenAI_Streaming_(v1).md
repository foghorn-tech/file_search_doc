# [Streaming (v1) Legacy](/docs/api-reference/assistants-streaming-v1)
Stream the result of executing a Run or resuming a Run after submitting
        tool outputs. 
You can stream events from the
        [Create Thread and Run](/docs/api-reference/runs-v1/createThreadAndRun), [Create Run](/docs/api-reference/runs-v1/createRun), and
        [Submit Tool Outputs](/docs/api-reference/runs-v1/submitToolOutputs)
        endpoints by passing "stream": true. The response will be a
        [Server-Sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events)
        stream. 
Our Node and Python SDKs provide helpful utilities to make streaming
        easy. Reference the
        [Assistants API quickstart](/docs/assistants/overview) to
        learn more. 
