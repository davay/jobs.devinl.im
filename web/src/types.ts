export interface JobDTO {
  title: string
  company: string
  category: string
  url: string
  date: string
  retrieval_date: string
}

export interface SourceDTO {
  company_name: string
  category_id: number
  category_name: string
  url: string
}

export interface JobSearchParamsDTO {
  keywords: string[]
  page: number
  limit: number
}

export interface DashboardProps {
  keywords: string[]
}
