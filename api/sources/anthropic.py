from .base import CategorySource, CompanySource

anthropic_sources = CompanySource(
    name="Anthropic",
    categories=[
        CategorySource(
            name="Technical Program Management",
            url="https://www.anthropic.com/jobs?team=4050634008",
        ),
        CategorySource(
            name="Software Engineering - Product",
            url="https://www.anthropic.com/jobs?team=4050633008",
        ),
        CategorySource(
            name="Product Management, Support, & Operations",
            url="https://www.anthropic.com/jobs?team=4002057008",
        ),
        CategorySource(
            name="Software Engineering - Infrastructure",
            url="https://www.anthropic.com/jobs?team=4019632008",
        ),
    ],
)
