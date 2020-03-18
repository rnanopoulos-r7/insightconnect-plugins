import komand
from .schema import GetPageContentInput, GetPageContentOutput, Input, Output
# Custom imports below
from ...util import util


class GetPageContent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_page_content',
                description='Get Page Content',
                input=GetPageContentInput(),
                output=GetPageContentOutput())

    def run(self, params={}):
        page = params[Input.PAGE]
        space = params[Input.SPACE]
        p = self.connection.client.getPage(page, space)
        if p:
            p = util.normalize_page(p)
            return {Output.CONTENTS: p['content'], Output.FOUND: True }

        return {Output.FOUND: False, Output.CONTENTS: ''}
