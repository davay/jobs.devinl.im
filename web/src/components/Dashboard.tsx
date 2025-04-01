import api from '@/api'
import {
  Card,
  CardContent,
  CardHeader,
  CardDescription,
  CardTitle
} from '@/components/ui/card'
import { useState, useEffect } from 'react'
import { parseISO, format } from 'date-fns'
import { JobSearchResultDTO, JobSearchResponseDTO, JobSearchParamsDTO, DashboardProps } from '@/types'
import DashboardPagination from '@/components/DashboardPagination'

export default function Dashboard({ keywords }: DashboardProps) {
  const [page, setPage] = useState<number>(0)
  const [jobs, setJobs] = useState<JobSearchResultDTO[]>([])
  const [totalPages, setTotalPages] = useState<number>(0)
  const limit = 12 // try multiples of 6, to keep even # of rows in all layouts

  useEffect(() => {
    const jobSearchParams: JobSearchParamsDTO = {
      keywords: keywords,
      page: page,
      limit: limit
    };

    api.searchJobs(jobSearchParams)
      .then((response: JobSearchResponseDTO) => {
        setJobs(response.results);
        setTotalPages(response.total_pages);
      })
      .catch(err => {
        console.error('Failed to fetch jobs:', err);
      })
  }, [keywords, page]);

  const formatReadableDate = (dateString: string) => {
    try {
      const date = parseISO(dateString);
      return format(date, 'MMMM d, yyyy');
    } catch (error) {
      console.error('Error formatting date:', error);
      return "Unspecified";
    }
  };


  return (
    <div className="flex flex-col min-h-screen">
      <div className="flex-grow">
        <h1 className="font-bold text-lg text-left pl-1 py-2">Recent Job Postings</h1>
        <p className="text-left text-sm pl-1 pb-2">All jobs are pulled directly from company sites within the last 24 hours (randomized). Clicking on a card brings you to the page where the job was found, not to the job itself.</p>
        <p className="text-left text-sm pl-1 pb-2">Note: If the job posting doesn't have a date, it will be placed behind all others with a date.</p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {jobs.map((job, index) => (
            <a key={index} href={job.url} target="_blank">
              <Card key={index} className="h-full">
                <CardHeader>
                  <CardTitle>{job.title}</CardTitle>
                  <CardDescription>{job.company} | {job.category}</CardDescription>
                  <CardDescription>Posted on: {formatReadableDate(job.date)}</CardDescription>
                </CardHeader>
                <CardContent>
                  <CardDescription>Last refreshed: {job.last_refreshed}</CardDescription>
                </CardContent>
              </Card>
            </a>
          ))}
        </div>
      </div>
      <div className="mt-auto pt-8">
        <DashboardPagination page={page} setPage={setPage} totalPages={totalPages} />
      </div>
    </div>
  )
}
