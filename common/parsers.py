from common import const


class ParserException(Exception):
    """When we fail to parse data"""


def shopify_order(data, shop_url):
    """
    It's always a good idea to map the Shopify order to a data structure that you decide what it looks like
    The reason is simple, you should only try to collect and persist data that you know will be used for your business.
    Feel free to extend this structure, the Shopify order event can be [found here](https://shopify.dev/api/admin/rest/reference/events/webhook)
    """
    return_data = {
        const.ORDER_SHOP_UNIQUE_ID: shop_url,
        const.ORDER_ID: str(data["id"]),
        "order": {
            "created_at": data["created_at"],
            "total_price": data["total_price"],
            "total_weight": data["total_weight"],
            "currency": data["currency"],
            "financial_status": data["financial_status"],
            "order_number": data["order_number"],
            "order_status_url": data["order_status_url"],
            "line_items": data["line_items"],
        }


    }
    #if data.get("billing_address"):
        #return_data["order"]["billing_address"] = {
                #"city": data["billing_address"]["city"],
                #"country": data["billing_address"]["country"],
                #"country_code": data["billing_address"]["country_code"],
        #}
    #if data.get("line_items"):
        #return_data
    if data.get("shipping_address"):
        return_data["order"]["shipping_address"] = {
                "city": data["shipping_address"]["city"],
                "country": data["shipping_address"]["country"],
                "country_code": data["shipping_address"]["country_code"],
                "NAME": data["shipping_address"]["name"],
        }


    return return_data


def shopify_fulfillment(data, shop_url):
    return_data = {
        const.ORDER_SHOP_UNIQUE_ID: shop_url,

        "fulfillment": {
            "id": data["id"],
            "line_items": data["line_items"],
            "destination": data["destination"],
        }
    }

    if data.get("name"):
        print("HEJEHEHEHJEJ")

    return return_data

def shopify_order_fulfillment(data, shop_url):
    return_data = {
        const.ORDER_SHOP_UNIQUE_ID: shop_url,

        "order": {
            "id": data["id"],
            "line_items": data["line_items"],
        }
}

    return return_data


