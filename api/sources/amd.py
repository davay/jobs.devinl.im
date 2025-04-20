from .base import CategorySource, CompanySource

amd_sources = CompanySource(
    name="AMD",
    categories=[
        CategorySource(
            name="Engineering",
            url="https://careers.amd.com/careers-home/jobs?country=United%20States&page=1&sortBy=posted_date&descending=true&limit=25&categories=Engineering",
        ),
    ],
)
