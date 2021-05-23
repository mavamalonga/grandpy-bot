def get_page_sections(page):
	""" Get page sections"""

	API_ENDPOINT = "https://en.wikipedia.org/w/api.php"

	params = {
		"action": "parse",
		"page": page,
		"prop": "sections",
		"format": "json"
	}

	res = SESSION.get(url=API_ENDPOINT, params=params)
	data = res.json()

	if 'error' in data:
		return parsed_sections = data and data['parse'] and data['parse']['sections']
		sections = []

	for section in parsed_sections:
		if section['toclevel'] == 1:
			sections.append(section['line'])
	return sections

def get_red_links(title):
    """ Get missing links on a page
    """
    params = {
        "action": "query",
        "titles": title,
        "generator": "links",
        "gpllimit": 20,
        "format": "json"
    }

    res = SESSION.get(url=API_ENDPOINT, params=params)
    data = res.json()
    pages = data and data['query'] and data['query']['pages']
    links = []

    for page in pages.values():
        if 'missing' in page:
            links.append(page['title'])

    return links