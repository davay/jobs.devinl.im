import { JobDTO, SourceDTO } from '@/types'

const api =
{
  async getJobs(): Promise<JobDTO[]> {
    const res = await fetch('api/get_jobs')
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
