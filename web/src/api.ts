const BASE_URL = "http://localhost:8000"

const api =
{
  async getJobs() {
    const res = await fetch(BASE_URL + '/get_jobs')
    const data = await res.json()
    if (!res.ok) {
      return Promise.reject({ status: res.status, data })
    }
    console.log(data)
    return data
  }
}

export default api
