from typing import Optional, Dict
import pptx

from jina import Executor, DocumentArray, requests, Document


class PptxLoader(Executor):
    def __init__(self,
                 traversal_paths: list = ['r'],
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.traversal_paths = traversal_paths

    @requests
    def process(self, docs: DocumentArray, parameters: Optional[Dict], **kwargs):
        """Process the documents and extract the text and images
        """
        traversal_paths = parameters.get('traversal_paths', self.traversal_paths)
        for d in docs.traverse_flat(traversal_paths):
            self._process_one(d)

    def _process_one(self, d):
        prs = pptx.Presentation(d.uri)
        nr = 0

        for slide in prs.slides:
            for shape in slide.shapes:
                if shape.has_text_frame:
                    for paragraph in shape.text_frame.paragraphs:
                        for run in paragraph.runs:
                            d.chunks.append(Document(content=run.text))

                if isinstance(shape, pptx.shapes.picture.Picture):
                    d.chunks.append(Document(blob=shape.image.blob))
                    with open(f'{nr}.png', 'wb') as f:
                        f.write(shape.image.blob)
                    nr += 1

