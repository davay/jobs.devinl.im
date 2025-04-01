from .base import CategorySource, CompanySource

amazon_sources = CompanySource(
    name="Amazon",
    categories=[
        CategorySource(
            name="Software Development",
            url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=software-development&country%5B%5D=USA",
        ),
        CategorySource(
            name="Project/Program/Product Management--Technical",
            url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=project-program-product-management-technical&country%5B%5D=USA",
        ),
        CategorySource(
            name="Machine Learning Science",
            url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=machine-learning-science&country%5B%5D=USA",
        ),
        CategorySource(
            name="Data Science",
            url="https://www.amazon.jobs/en/search?sort=recent&category%5B%5D=data-science&country%5B%5D=USA",
        ),
    ],
)
