from .base import CategorySource, CompanySource

jane_street_sources = CompanySource(
    name="Jane Street",
    categories=[
        CategorySource(
            name="New Grad",
            url="https://www.janestreet.com/join-jane-street/open-roles/?type=full-time-new-grad&location=new-york",
        ),
        CategorySource(
            name="Trading, Research, and Machine Learning",
            url="https://www.janestreet.com/join-jane-street/open-roles/?type=experienced-candidates&location=new-york&department=trading-research-and-machine-learning",
        ),
        CategorySource(
            name="Technology",
            url="https://www.janestreet.com/join-jane-street/open-roles/?type=experienced-candidates&location=new-york&department=technology",
        ),
    ],
)
