from pyramid.static import static_view


def includeme(config):
    # Process settings to remove storage wording.

    # Expose capability.
    config.add_api_capability(
        "admin",
        version="1.3.0",
        description="Serves the admin console.",
        url="https://github.com/Kinto/kinto-admin/",
    )

    static = static_view('kinto.plugins.admin:static', use_subpath=True)
    config.add_route('catchall_static', '/admin/*subpath')
    config.add_view(static, route_name="catchall_static")
