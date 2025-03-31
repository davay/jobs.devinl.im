import { SourceDTO, JobSearchParamsDTO, JobSearchResponseDTO } from '@/types'

const api = {
  async searchJobs(jobSearchParams: JobSearchParamsDTO): Promise<JobSearchResponseDTO> {
    const res = await fetch('api/search_jobs', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(jobSearchParams),
    })
    const data = await res.json()
    if (!res.ok) {
      return Promise.reject({ status: res.status, data })
    }
    return data
  },

  async getSources(): Promise<SourceDTO[]> {
    const res = await fetch('api/get_sources')
    const data = await res.json()
    if (!res.ok) {
      return Promise.reject({ status: res.status, data })
    }
    return data
  }
}

export default api
