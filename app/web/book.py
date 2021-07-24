from flask import jsonify, request

from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm



@web.route("/book/search")
def search():
    """
        q : 普通关键字
        page
    :return:
    """
    # q = request.args["q"]
    # page = request.args["page"]
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)
        # return result, 200, {"content-type":"application/json"}
    else:
        return jsonify({"msg": form.errors})