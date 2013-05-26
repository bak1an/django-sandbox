import no.such.module


class SomeMiddleware(object):
    def process_request(self, request):
        print "Hey, i'm middleware"
