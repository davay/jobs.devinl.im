## Design Choices

- URL is only in category.
    - Some companies don't split by categories, especially smaller ones. In these cases, a default "general" category is used.
- Job doesn't have a URL because I can't get the parsing reliable enough.
    - Clicking on them leads to the category/company page.

## DB Tables 

- Company: 
    - id | PK
    - name

- Category:
    - id | PK
    - company_id | FK
    - name
    - url 

- Job:
    - id | PK
    - category_id | FK
    - title 
    - date 
