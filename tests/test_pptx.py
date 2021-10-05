import os.path

from jina import Document, DocumentArray

from executor import PptxLoader

cur_dir = os.path.dirname(os.path.abspath(__file__))


def test_pptx_text():
    expected_imgs = [
        open(os.path.join(cur_dir, f'{i}.png'), 'rb').read() for i in range(4)
    ]

    test_file = os.path.join(cur_dir, 'test.pptx')
    docs = DocumentArray([Document(uri=test_file)])
    PptxLoader().process(docs, {})

    c_text = [c.content for c in docs[0].chunks if isinstance(c.content, str)]
    c_img = [c.content for c in docs[0].chunks if isinstance(c.content, bytes)]

    assert ['JINA + EUROPYTHON', 'WORKSHOP', '26 July 2021',
            'Cristian Mitroi, Maximilian Werk ', 'Jina AI', '',
            'github.com/jina-ai/workshops/', 'tree/main', '/pokedex',
            'Please interrupt us and ask questions', 'Who’s that Pokemon?'] == c_text
    assert expected_imgs == c_img