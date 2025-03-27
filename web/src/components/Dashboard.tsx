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

  useEffect(() => {
    api.getJobs()
      .then(jobsData => setJobs(jobsData))
      .catch(err => {
        console.error('Failed to fetch jobs:', err);
      })
  }, []);

  return (
    <div>
      <h1 className="py-2">Recent Job Postings</h1>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {jobs.map((job, index) => (
          <Card key={index} className="h-30">
            <CardContent className="m-auto">
              <CardTitle>{job.title}</CardTitle>
              <CardDescription>{job.company}</CardDescription>
              <CardDescription>{job.date}</CardDescription>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}
