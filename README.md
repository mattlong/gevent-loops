# gevent-loops

This is a collection of custom gevent loop classes meant to override `gevent.core.loop`. The original motivation was to prevent a big ugly stack trace from being printed to stdout whenever a websocket client disconnects from a Gunicorn server.

## Installation

Available from PyPI: <http://pypi.python.org/pypi/gevent-loops/>. pip is the recommended installation method:

    pip install gevent-loops

## Usage

As described in the gevent docs: The event loops are now pluggable. The `GEVENT_LOOP` enviroment variable can specify the alternative class to use (the default is gevent.core.loop).

    export GEVENT_LOOP='gevent_loops.loops.QuietLoop'
    # start your gevent-based server however you otherwise would

That's all!

## Is it any good?

Yes.

## License

([The MIT License](LICENSE))

Copyright 2014 Matt Long
