

def get_element_via_path(json_obj, path, ignore_nodes=[]):
    """
    path = 'key1/0/key2'
    Can be used to get a deeply nested element or node in a JSON data tree
    returns is_found, element
    ignore_nodes defines for which elements in path not to send a notification
    """
    def get_element(json_obj, path):
        path_items = path.strip('/').split("/")
        first_item = path_items.pop(0)

        try:
            if first_item.isdigit():
                json_obj = json_obj[int(first_item)]
            else:
                json_obj = json_obj[first_item]
        except (AttributeError, KeyError) as err:
            if first_item not in ignore_nodes:
                print(f"Node fetching error: {first_item} missing in {full_path}")
            return None

        if path_items:
            path = "/".join(path_items)
            return get_element(json_obj, path)
        else:
            return json_obj
    
    full_path = path    # we define full path here which will be used in error handling
    return get_element(json_obj, path)
