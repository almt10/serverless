import os

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    path = os.environ['Http_Path']
    pathArr = path.split("/")
    pageName = pathArr[1]
    
    dirname = os.path.dirname(__file__)
    page = os.path.join(dirname, 'html', pageName + '.html')

    with(open(page, 'r')) as file:
        html = file.read()

    return html