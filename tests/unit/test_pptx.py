import os.path

from jina import Document, DocumentArray

from executor import PptxLoader

cur_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(cur_dir, '..', 'data')


def test_pptx():
    expected_imgs = [
        open(os.path.join(data_dir, f'{i}.png'), 'rb').read() for i in range(4)
    ]

    test_file = os.path.join(data_dir, 'test.pptx')
    docs = DocumentArray([Document(uri=test_file)])
    PptxLoader().process(docs, {})

    c_text = [c.content for c in docs[0].chunks if c.modality == 'text']
    c_img = [c.content for c in docs[0].chunks if c.modality == 'image']

    assert ['JINA + EUROPYTHON', 'WORKSHOP', '26 July 2021',
            'Cristian Mitroi, Maximilian Werk ', 'Jina AI', '',
            'github.com/jina-ai/workshops/', 'tree/main', '/pokedex',
            'Please interrupt us and ask questions', 'Who’s that Pokemon?'] == c_text
    assert expected_imgs == c_img
