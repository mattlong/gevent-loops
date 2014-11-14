from gevent_loops.loops import BaseLoop


class QuietLoop(BaseLoop):
    logger_name = 'gevent.error'

    def __init__(self, *args, **kwargs):
        super(QuietLoop, self).__init__(*args, **kwargs)
        import logging
        self._logger = logging.getLogger(self.logger_name)

    # based on gevent.hub.Hub.handle_error
    def handle_error(self, context, type, value, tb):
        import socket
        from gevent.hub import Hub

        if not issubclass(type, Hub.NOT_ERROR):
            if isinstance(value, socket.error) and value.errno == 32:
                # broken pipe
                self._logger.debug(value)
            else:
                self.print_exception(context, type, value, tb)
                #logger.error('', exc_info=(type, value, tb))

        if context is None or issubclass(type, Hub.SYSTEM_ERROR):
            # self.error_handler will be an instance of gevent.hub.Hub
            self.error_handler.handle_system_error(type, value)
