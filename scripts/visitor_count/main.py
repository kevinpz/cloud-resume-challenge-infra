"""
Visitor count
"""

import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Init firebase connection
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': os.environ['GCP_PROJECT'],
})


def get_visitor_count():
    """
    Get the number of visitors

    :return: the number of visitor
    """
    database = firestore.client()
    visitor_nb = 0
    # Get the document
    visitor_ref = database.collection(u'cloudresume').document(u'visitor_count')
    doc = visitor_ref.get()
    # If the documents exists
    if doc.exists:
        # Get the last number of visitor
        visitor_nb = doc.to_dict()['count']

    return visitor_nb


def save_task_data(visitor_nb):
    """
    Save the number of visitors to Firestore

    :param visitor_nb: number of visitor
    """
    database = firestore.client()
    visitor_ref = database.collection(u'cloudresume').document(u'visitor_count')

    # Write the new number of visitors
    visitor_ref.set({'count': visitor_nb}, merge=True)


def visitor_count(request):  # pylint: disable=unused-argument
    """

    :param request: the client request
    :return: the current visitor number
    """
    current_visitor = 0
    # visitor_nb = get_visitor_count()
    # current_visitor = str(int(visitor_nb + 1))
    # save_task_data(current_visitor)
    client_data = {
        'currentVisitor': current_visitor
    }

    return client_data
