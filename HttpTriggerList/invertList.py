import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    param = req.params.get('param').split(",")
    if not param:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            param = req_body.get('param')
            
    inverted_param = param[::-1]

    if inverted_param:
        return func.HttpResponse(f"{inverted_param}")
    else:
        return func.HttpResponse(
             "Please enter a valid value",
             status_code=400
        )
