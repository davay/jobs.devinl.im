from .base import CategorySource, CompanySource

openai_sources = CompanySource(
    name="OpenAI",
    categories=[
        CategorySource(
            name="Applied AI",
            url="https://openai.com/careers/search/?l=e8062547-b090-4206-8f1e-7329e0014e98%2Cbbd9f7fe-aae5-476a-9108-f25aea8f6cd2%2C16c48b76-8036-4fe3-a18f-e9d357395713%2C07ed9191-5bc6-421b-9883-f1ac2e276ad7&c=e1e973fe-6f0a-475f-9361-a9b6c095d869%2Cf002fe09-4cec-46b0-8add-8bf9ff438a62%2Cab2b9da4-24a4-47df-8bed-1ed5a39c7036",
        ),
        CategorySource(
            name="Scaling",
            url="https://openai.com/careers/search/?l=e8062547-b090-4206-8f1e-7329e0014e98%2Cbbd9f7fe-aae5-476a-9108-f25aea8f6cd2%2C16c48b76-8036-4fe3-a18f-e9d357395713%2C07ed9191-5bc6-421b-9883-f1ac2e276ad7&c=7cba3ac0-2b6e-4d52-ad38-e39a5f61c73f%2C2808218a-d9fc-426e-9c4c-9e575b3842c8%2Caee065f0-5fa5-437d-9506-67c186cbfbbd%2C0df0672c-86c0-46ee-b3dd-3cf63adb5b08%2C8cb35b37-f31f-4167-84ca-ba789cf36142%2C795ae415-f19a-41c9-8acd-b1b8c08c4896",
        ),
        CategorySource(
            name="Product Management",
            url="https://openai.com/careers/search/?l=e8062547-b090-4206-8f1e-7329e0014e98%2Cbbd9f7fe-aae5-476a-9108-f25aea8f6cd2%2C16c48b76-8036-4fe3-a18f-e9d357395713%2C07ed9191-5bc6-421b-9883-f1ac2e276ad7&c=db3c67d7-3646-4555-925b-40f30ab09f28",
        ),
        CategorySource(
            name="Technical Program Management",
            url="https://openai.com/careers/search/?l=e8062547-b090-4206-8f1e-7329e0014e98%2Cbbd9f7fe-aae5-476a-9108-f25aea8f6cd2%2C16c48b76-8036-4fe3-a18f-e9d357395713%2C07ed9191-5bc6-421b-9883-f1ac2e276ad7&c=47b777e7-af51-46a6-86ad-55d3da27b879",
        ),
    ],
)
