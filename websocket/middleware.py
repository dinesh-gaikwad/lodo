from urllib.parse import parse_qs

class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):

        query_string = scope.get("query_string", b"")

        query_params = parse_qs(
            query_string.decode()
        )

        token = query_params.get("token")

        scope["token"] = token[0] if token else None

        print("Socket Token:", scope["token"])

        return await self.inner(scope, receive, send)

class SocketLoggerMiddleware:

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):

        client = scope.get("client")

        print(f"Socket Connected: {client}")

        return await self.inner(scope, receive, send)

class RateLimitMiddleware:

    def __init__(self, inner):
        self.inner = inner
        self.request_limit = 100

    async def __call__(self, scope, receive, send):

        scope["rate_limit"] = self.request_limit

        return await self.inner(scope, receive, send)

def middleware_stack(inner):

    return TokenAuthMiddleware(
        SocketLoggerMiddleware(
            RateLimitMiddleware(inner)
        )
    )

print("WebSocket Middleware Loaded")
