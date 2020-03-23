Intro
=====

Transmission comes with an `RPC server`_ that follows an `RPC protocol specification`_.

When it receives a request, the server performs the requested action and sends back a response.

RPC format
----------

To illustrate the form of request and response messages, the following parts contain some pseudo-JSON schema.

Request
*******

A request requires ``method`` be specified, ``arguments`` and ``tag`` are optional.

``tag`` can be provided for matching requests and responses.

When the server responds, it includes the same ``tag`` that was provided in the request:

.. code-block:: none

    {
        "method": str
        "arguments": Dict[str, object]
        "tag": int
    }

Response
********

Likewise, ``result`` is the only required part.

.. code-block:: none

    {
        "result": str ("success" on success otherwise an error message)
        "arguments": Dict[str, object]
        "tag": int
    }

.. _`RPC server`: https://en.wikipedia.org/wiki/Remote_procedure_call
.. _`RPC protocol specification`: https://github.com/transmission/transmission/wiki/RPC-Protocol-Specification
