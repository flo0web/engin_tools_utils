from urllib import parse


def fetch_item_data(item_node, data_handlers):
    review_data = dict()

    for field, pattern in data_handlers.items():
        field_node_list = pattern['selector'](item_node)

        if len(field_node_list) == 0:
            if 'default' in pattern:
                review_data[field] = pattern['default']
            else:
                review_data[field] = None
            continue

        if 'attr' in pattern:
            field_value = [node.get(pattern['attr']) for node in field_node_list]
        else:
            field_value = [node.text_content() for node in field_node_list]

        if len(field_node_list) == 1:
            field_value = field_value[0]

        if 'post_process' in pattern and field_value is not None:
            for process in pattern['post_process']:
                field_value = process(field_value)

        review_data[field] = field_value

    return review_data


def fetch_list_item_data(doc, item_selector, data_handlers):
    item_node_list = item_selector(doc)

    result = []
    for item_node in item_node_list:
        review_data = fetch_item_data(item_node, data_handlers)
        result.append(review_data)

    return result


def fetch_urls(doc, selector, base_url):
    page_node_lst = selector(doc)

    results = []
    for page_node in page_node_lst:
        page_url = page_node.get('href')
        full_url = parse.urljoin(base_url, page_url)

        results.append(full_url)

    return results
