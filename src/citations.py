# Philip Bailey
# 29 Jan 2020
# Script to generate markdown file listing of citations within a Zotero library
# https://pyzotero.readthedocs.io/en/latest/
# -------------------------------------------------------------
import os
import argparse
from pyzotero import zotero


def generate_citations(output_path, boiler_plate):
    """Call the Zotero API and retrieve all citations in a library.
    Format the citations and write them to a markdown file at the 
    specified output path.

    Arguments:
        output_path {str} -- File path where to write the markdown formatted citations.
        boiler_plate {str} -- Optional file path of markdown file to inject into output before citations.
    """

    if 'LIBRARY' not in os.environ:
        raise Exception('Missing LIBRARY identifier in .env environment file.')

    if 'API_KEY' not in os.environ:
        raise Exception('Missing Zotero API_KEY in .env environment file.')

    zot = zotero.Zotero(os.environ['LIBRARY'], 'group', os.environ['API_KEY'])
    items = zot.top(limit=50)
    formatted_citations = []
    for item in items:

        if item['data']['itemType'] == 'attachment':
            continue

        authors = ', '.join(['{}, {}'.format(author['lastName'], author['firstName']) for author in item['data']['creators']])
        date = item['meta']['parsedDate'].split('-')[0]

        if 'url' in item['data'] and len(item['data']['url']) > 0:
            title = '[{}]({})'.format(item['data']['title'], item['data']['url'])
        else:
            title = item['data']['title']

        pub = ''
        if 'publicationTitle' in item['data']:
            pub = item['data']['publicationTitle']
        else:
            pub = item['data']['publisher']

        doi = ''
        if 'DOI' in item['data']:
            doi = 'DOI: [{0}]({0})'.format(item['data']['DOI'])

        citation = '{} {}. {}. {}. {}'.format(
            authors,
            date,
            title,
            pub,
            doi)

        formatted_citations.append(citation)

    header = '---\ntitle: Publications\n---\n\n'
    if boiler_plate and os.path.isfile(boiler_plate):
        with open(boiler_plate, mode='r') as bp:
            header = bp.read()

    with open(output_path, 'w+') as f:
        f.write(header)
        [f.write(c + '\n\n') for c in formatted_citations]

    print('Process complete.', len(formatted_citations), 'citations written to', output_path)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('output_path', help='Output file path where citations markdown list will be written', type=str)
    parser.add_argument('--boiler_plate', help='(Optional) existing markdown file to inject before citations', type=str, default='')
    args = parser.parse_args()

    generate_citations(args.output_path, args.boiler_plate)


if __name__ == '__main__':
    main()
