export interface JobSearchResultDTO {
  title: string
  company: string
  category: string
  url: string
  date: string
  last_refreshed: string
}

export interface JobSearchResponseDTO {
  results: JobSearchResultDTO[]
  total_pages: number
}

export interface SourceDTO {
  company_name: string
  category_id: number
  category_name: string
  url: string
  last_refreshed?: string
}

export interface JobSearchParamsDTO {
  keywords: string[]
  page: number
  limit: number
}

export interface DashboardProps {
  keywords: string[]
}

export interface DashboardPaginationProps {
  page: number
  setPage: React.Dispatch<React.SetStateAction<number>>
  totalPages: number
}

export interface FilterProps {
  keywords: string[];
  setKeywords: React.Dispatch<React.SetStateAction<string[]>>
}
