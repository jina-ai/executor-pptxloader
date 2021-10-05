# PptxLoader

The `PptxLoader` [Executor](https://docs.jina.ai/fundamentals/executor/) is specialized in processing Powerpoint files into Jina's [`Document`](https://docs.jina.ai/fundamentals/document/) type. 
It loads the text and images from the slides, using the [pptx](https://python-pptx.readthedocs.io/en/latest/index.html) library.
It detects both images and text, and adds these as chunks to the original `Document`.

<!-- version=v0.1 -->
