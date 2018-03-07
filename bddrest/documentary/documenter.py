
class Documenter:
    def __init__(self, formatter_factory):
        self.formatter_factory = formatter_factory

    def document(self, story, outfile):
        basecall = story.base_call
        formatter = self.formatter_factory(outfile)
        formatter.write_header1(basecall.title)
        formatter.write_header2(f'{basecall.verb} {basecall.url}')
        if basecall.description:
            formatter.write_paragraph(basecall.description)

