from .base import CategorySource, CompanySource

neuralink_sources = CompanySource(
    name="Neuralink",
    categories=[
        CategorySource(
            name="General",
            url="https://neuralink.com/careers/",
        ),
    ],
)
