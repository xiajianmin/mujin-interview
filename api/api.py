class Api(restful.Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations = {
            'application/xml': output_xml,
            'text/html': output_html,
            'text/csv': output_csv,
            'application/json': output_json,
        }

    def output_json(data, code, headers=None):
        """Makes a Flask response with a JSON encoded body"""
        resp = make_response(json.dumps(data), code)
        resp.headers.extend(headers or {})
        return resp