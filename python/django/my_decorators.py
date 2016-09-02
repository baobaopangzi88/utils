ALLOWED_ORIGINS_PAT = re.compile(r"https?://(\w+\.)?(wantjr)\.(com|cn|cc)")

def json_decorator(func):
    """ 
        web应用中，常常会需要返回json数据给前端调用。
        为了前后端交互更方便,可以简单的把域名的前缀替换即可

        样例:
        @json_decorator
        def my_view(request,a,b,c,template="home.html"):
            context = {"name":"bob"}
            return context

        访问 json.wantjr.com 返回数据
        访问 www.wantjr.com 返回正常网页

    """
    def _deco(request,*args, **kwargs):
        # 正式context
        context = func(request, *args, **kwargs)
        # 判断是否请求数据
        if request.get_host()[:4] == "json":
            response =  HttpResponse(json.dumps(context), content_type="application/json")
            origin_addr = request.META.get("HTTP_ORIGIN", "")
            # 处理跨域请求
            if ALLOWED_ORIGINS_PAT.match(origin_addr):
                response['Access-Control-Allow-Origin'] = origin_addr
        # 后端可能有重定向的需求
        elif context.get("redirect_url"):
            response = HttpResponseRedirect(context.get("redirect_url"))
        else:
            template = kwargs.get("template","home.html")
            # 可能有返回不同模板到需求
            if context.get("template"):
                template = context.get("template")
            response = render(request,template,context)

        return response
    return _deco
return json_decorator




