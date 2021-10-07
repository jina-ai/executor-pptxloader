# PptxLoader

The `PptxLoader` [Executor](https://docs.jina.ai/fundamentals/executor/) is specialized in transforming PowerPoint files into Jina's [`Document`](https://docs.jina.ai/fundamentals/document/) type. 
It loads the text and images from the slides, using the [pptx](https://python-pptx.readthedocs.io/en/latest/index.html) library.
It detects both images and text, and adds these as chunks to the original `Document`.
Text chunks have the `modality` of `text`, image chunks have the `modality` of `image`.
