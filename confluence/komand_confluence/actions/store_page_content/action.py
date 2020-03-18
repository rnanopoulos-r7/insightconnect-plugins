import komand
from .schema import StorePageContentInput, StorePageContentOutput, Input, Output
# Custom imports below
from ...util import util


class StorePageContent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='store_page_content',
                description='Store Page Content',
                input=StorePageContentInput(),
                output=StorePageContentOutput())

    def run(self, params={}):
        """Store a page"""
        content = params[Input.CONTENTS]
        page = params[Input.PAGE]
        space = params[Input.SPACE]
        p = self.connection.client.storePageContent(page, space, content)
        p = util.normalize_page(p)
        return {Output.PAGE: p}
