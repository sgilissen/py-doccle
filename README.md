# py-doccle
Retrieve documents from Doccle with an easy to use interface
## Example usage
```python
# Import the library
from doccle import doccle

# Create a new connector object. Make sure to safely store and retrieve your credentials (don't hardcode them!)
docs = doccle.Connector('<your-doccle-username>', '<your-doccle-password>')

# Get a list of the 5 latest documents available in your Doccle account that are marked as new
# Arguments are optional. When left empty, all documents will be listed.
docs.get_documents(only_new=True, max_docs=2)
# This will yield the following dictionary (limited to 1 for documentation purposes):
{
    'documents': [
        {
            'sender': '<Name of the sender>',
            'name': '<document name in Doccle>',
            'publish_date': '<Date that the document has been published in Doccle>', 
            'document_type': '<Type of document. For example, an invoice', 
            'file_url': '<File URL>', 
            'file_name': '<Filename as saved in Doccle>', 
            'mime_type': '<MIME type, for example application/pdf>', 
            'payment_info': {
                'amount_to_pay': '<Amount to pay as stated on the invoice, if applicable>',
                'sender_bic': '<BIC of the sender, if applicable>',
                'sender_iban': '<IBAN of the sender, if applicable>',
                'payment_reference': '<Payment reference on the invoice, if applicable>',
                'payment_status': '<Payment status of the invoice, if applicable>'
            }
        }
    ]
}
```