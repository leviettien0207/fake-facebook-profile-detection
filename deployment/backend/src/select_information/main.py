from flask import request

from share.utils import make_response
from share.check.check_link import check_link_fb
from share.get_information import get_information
 
# from share.validate import validator
# from .schema import RequestSchema

@make_response()
# @validator(RequestSchema)

def select_information():
    data_input = request.get_json()
    link = data_input.get("InputLink")
    check_link_fb(link)
    name, avatar = get_information(link)
    percent_clone = 30
    percent_not_clone = 100 - percent_clone
    output_all= {}
    output_all.update({"Name": name})
    output_all.update({"Avatar": avatar})
    output_all.update({"InputLink": link})
    message = "Theo như phân tích thì tỉ lệ account này clone là:" + str(percent_clone) + "%, không phải clone là:" + str(percent_not_clone) + "%"
    output_all.update({"Message": message})
    output_all.update({"Percent": percent_clone})
    
    return output_all