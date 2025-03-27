import api from '@/api'
import {
  Card,
  CardContent,
  CardDescription,
  CardTitle
} from '@/components/ui/card'
import { useState, useEffect } from 'react'
import { JobDTO } from '@/types'

export default function Dashboard() {
  const [jobs, setJobs] = useState<JobDTO[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.getJobs()
      .then(jobsData => setJobs(jobsData))
      .catch(err => {
        console.error('Failed to fetch jobs:', err);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <div>
      <h2>Recent Job Postings</h2>

      {/* TODO: spinner */}
      {loading ? <div>TODO</div> :
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {jobs.map((job, index) => (
            <Card key={index}>
              <CardContent>
                {/* TODO: data models */}
                <CardTitle>{job.title}</CardTitle>
                <CardDescription>{job.company}</CardDescription>
                <CardDescription>{job.date}</CardDescription>
              </CardContent>
            </Card>
          ))}
        </div>
      }
    </div>
  )
}
