# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.preview.understand.service.intent.field import FieldList
from twilio.rest.preview.understand.service.intent.sample import SampleList


class IntentList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid):
        """
        Initialize the IntentList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.preview.understand.service.intent.IntentList
        :rtype: twilio.rest.preview.understand.service.intent.IntentList
        """
        super(IntentList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid}
        self._uri = '/Services/{service_sid}/Intents'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams IntentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.service.intent.IntentInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'])

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists IntentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.service.intent.IntentInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of IntentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size})

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return IntentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IntentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return IntentPage(self._version, response, self._solution)

    def create(self, unique_name, friendly_name=values.unset):
        """
        Create a new IntentInstance

        :param unicode unique_name: The unique_name
        :param unicode friendly_name: The friendly_name

        :returns: Newly created IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentInstance
        """
        data = values.of({'UniqueName': unique_name, 'FriendlyName': friendly_name})

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return IntentInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def get(self, sid):
        """
        Constructs a IntentContext

        :param sid: The sid

        :returns: twilio.rest.preview.understand.service.intent.IntentContext
        :rtype: twilio.rest.preview.understand.service.intent.IntentContext
        """
        return IntentContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a IntentContext

        :param sid: The sid

        :returns: twilio.rest.preview.understand.service.intent.IntentContext
        :rtype: twilio.rest.preview.understand.service.intent.IntentContext
        """
        return IntentContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.IntentList>'


class IntentPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the IntentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.preview.understand.service.intent.IntentPage
        :rtype: twilio.rest.preview.understand.service.intent.IntentPage
        """
        super(IntentPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IntentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.service.intent.IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentInstance
        """
        return IntentInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.IntentPage>'


class IntentContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the IntentContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.preview.understand.service.intent.IntentContext
        :rtype: twilio.rest.preview.understand.service.intent.IntentContext
        """
        super(IntentContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid}
        self._uri = '/Services/{service_sid}/Intents/{sid}'.format(**self._solution)

        # Dependents
        self._fields = None
        self._samples = None

    def fetch(self):
        """
        Fetch a IntentInstance

        :returns: Fetched IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return IntentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset, unique_name=values.unset):
        """
        Update the IntentInstance

        :param unicode friendly_name: The friendly_name
        :param unicode unique_name: The unique_name

        :returns: Updated IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentInstance
        """
        data = values.of({'FriendlyName': friendly_name, 'UniqueName': unique_name})

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return IntentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the IntentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def fields(self):
        """
        Access the fields

        :returns: twilio.rest.preview.understand.service.intent.field.FieldList
        :rtype: twilio.rest.preview.understand.service.intent.field.FieldList
        """
        if self._fields is None:
            self._fields = FieldList(
                self._version,
                service_sid=self._solution['service_sid'],
                intent_sid=self._solution['sid'],
            )
        return self._fields

    @property
    def samples(self):
        """
        Access the samples

        :returns: twilio.rest.preview.understand.service.intent.sample.SampleList
        :rtype: twilio.rest.preview.understand.service.intent.sample.SampleList
        """
        if self._samples is None:
            self._samples = SampleList(
                self._version,
                service_sid=self._solution['service_sid'],
                intent_sid=self._solution['sid'],
            )
        return self._samples

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.IntentContext {}>'.format(context)


class IntentInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the IntentInstance

        :returns: twilio.rest.preview.understand.service.intent.IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentInstance
        """
        super(IntentInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'links': payload['links'],
            'service_sid': payload['service_sid'],
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid']}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: IntentContext for this IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentContext
        """
        if self._context is None:
            self._context = IntentContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: The unique_name
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a IntentInstance

        :returns: Fetched IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, unique_name=values.unset):
        """
        Update the IntentInstance

        :param unicode friendly_name: The friendly_name
        :param unicode unique_name: The unique_name

        :returns: Updated IntentInstance
        :rtype: twilio.rest.preview.understand.service.intent.IntentInstance
        """
        return self._proxy.update(friendly_name=friendly_name, unique_name=unique_name)

    def delete(self):
        """
        Deletes the IntentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def fields(self):
        """
        Access the fields

        :returns: twilio.rest.preview.understand.service.intent.field.FieldList
        :rtype: twilio.rest.preview.understand.service.intent.field.FieldList
        """
        return self._proxy.fields

    @property
    def samples(self):
        """
        Access the samples

        :returns: twilio.rest.preview.understand.service.intent.sample.SampleList
        :rtype: twilio.rest.preview.understand.service.intent.sample.SampleList
        """
        return self._proxy.samples

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.IntentInstance {}>'.format(context)
