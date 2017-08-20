
bind = "0.0.0.0:8080"

def parse_query(query_string):
    parsed_query = query_string.split('&')
    return '\n'.join(parsed_query)

def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    try:
        data = parse_query(environ['QUERY_STRING'])
    except Exception as error:
        print error
        status = '500 Internal Server Error'
    start_response(status, header)
    return [ data ]
