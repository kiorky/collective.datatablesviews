import logging
from zope.i18nmessageid import MessageFactory
MessageFactory = collectivedatatablesviewsMessageFactory = MessageFactory('collective.datatablesviews') 
logger = logging.getLogger('collective.datatablesviews')
def initialize(context):
    """Initializer called when used as a Zope 2 product.""" 
