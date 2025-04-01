from .base import CategorySource, CompanySource

microsoft_sources = CompanySource(
    name="Microsoft",
    categories=[
        CategorySource(
            name="Software Engineering",
            url="https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&p=Software%20Engineering&l=en_us&pg=1&pgSz=20&o=Recent&flt=true",
        ),
        CategorySource(
            name="Research, Applied, & Data Sciences",
            url="https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&p=Research%2C%20Applied%2C%20%26%20Data%20Sciences&l=en_us&pg=1&pgSz=20&o=Recent&flt=true",
        ),
        CategorySource(
            name="Program Management",
            url="https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&p=Program%20Management&l=en_us&pg=1&pgSz=20&o=Recent&flt=true",
        ),
    ],
)
