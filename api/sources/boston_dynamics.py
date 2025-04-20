from .base import CategorySource, CompanySource

boston_dynamics_sources = CompanySource(
    name="Boston Dynamics",
    categories=[
        CategorySource(
            name="General",
            url="https://bostondynamics.com/careers/#jobs",
        ),
    ],
)
