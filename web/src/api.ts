import { JobDTO, SourceDTO } from '@/types'

const BASE_URL = "https://localhost:8000"

const api =
{
  async getJobs(): Promise<JobDTO[]> {
    const res = await fetch(BASE_URL + '/get_jobs')
    const data = await res.json()
    if (!res.ok) {
      return Promise.reject({ status: res.status, data })
    }
    return data
  },

  async getSources(): Promise<SourceDTO[]> {
    const res = await fetch(BASE_URL + '/get_sources')
    const data = await res.json()
    if (!res.ok) {
      return Promise.reject({ status: res.status, data })
    }
    return data
  }
}

export default api
