"""
    File name: doccle.py
    Author: Steve Gilissen
    Date created: 12/10/2022
    Date last modified: 12/10/2022
    Python Version: 3.6+
"""
import warnings
import requests
from requests.auth import HTTPBasicAuth


class Connector:
    def __init__(self, username='', password=''):
        self.base_url = 'https://secure.doccle.be/doccle-euui/rest/v2/'
        self.auth = HTTPBasicAuth(username, password)
        self.session = requests.Session()

    def get_documents(self, only_new=False, max_docs=0):
        """
        Fetches the list of documents and returns a dictionary with all relevant info
        :param only_new: Boolean: Only fetch the new documents
        :param max_docs: Maximum number of documents to download. 0 = no limitation.
        :return: Dictionary of documents or None
        """
        page_size_str = ''
        if max_docs > 0:
            page_size_str = f'&pageSize={max_docs}'

        if only_new:
            url = self.base_url + 'documents/new?lang=en&order=DESC&page=1&sort=date' + page_size_str
        else:
            url = self.base_url + 'documents?lang=en&order=DESC&page=1&sort=date' + page_size_str

        data = self.session.get(url, auth=self.auth).json()

        try:
            docs = []
            for count, doc in enumerate(data['documents']):
                if doc['senderDocumentType'] == 'Invoice':
                    payment_info = {
                        'amount_to_pay': doc['payment']['amountToPay'],
                        'sender_bic': doc['payment']['bic'],
                        'sender_iban': doc['payment']['iban'],
                        'payment_reference': doc['payment']['reference'],
                        'payment_status': doc['payment']['status']
                    }
                else:
                    payment_info = {}

                doc_dict = {
                    'sender': doc['sender']['label'],
                    'name': doc['name'],
                    'publish_date': doc['publishDate'],
                    'document_type': doc['senderDocumentType'],
                    'file_url': doc['contentUrl'],
                    'file_name': doc['fileName'],
                    'mime_type': doc['fileMimeType'],
                    'payment_info': payment_info
                }
                docs.append(doc_dict)
            return {'documents': docs}
        except (requests.exceptions.RequestException, ConnectionResetError) as err:
            warnings.warn(err)
            return None

    def download_document(self, document_uri):
        """
        Downloads the document and returns it as bytes
        :param document_uri: String: The URI string for the document
        :return: Document content as bytes or None
        """
        try:
            full_doc_url = self.base_url + 'documents/' + document_uri + '/content'
            data = self.session.get(full_doc_url)
            return data.content
        except (requests.exceptions.RequestException, ConnectionResetError) as err:
            warnings.warn(err)
            return None
