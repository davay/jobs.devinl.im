from .base import CategorySource, CompanySource

mistral_sources = CompanySource(
    name="Mistral",
    categories=[
        CategorySource(
            name="General",
            url="https://jobs.lever.co/mistral?location=Palo%20Alto",
        ),
    ],
)
