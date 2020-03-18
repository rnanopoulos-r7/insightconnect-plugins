import komand
from .schema import GetPageInput, GetPageOutput, Input, Output
# Custom imports below
from ...util import util


class GetPage(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_page',
                description='Get Page',
                input=GetPageInput(),
                output=GetPageOutput())

    def run(self, params={}):
        """Return a page."""
        page = params[Input.PAGE]
        space = params[Input.SPACE]
        p = self.connection.client.getPage(page, space)
        if p: 
            p = util.normalize_page(p)
            return {Output.PAGE: p, Output.FOUND: True}

        return {Output.PAGE: {}, Output.FOUND: False}
