from .base import CategorySource, CompanySource

huggingface_sources = CompanySource(
    name="HuggingFace",
    categories=[
        CategorySource(
            name="General",
            url="https://apply.workable.com/huggingface/",
        ),
    ],
)
