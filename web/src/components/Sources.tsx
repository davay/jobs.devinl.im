import api from '@/api'
import {
  Card,
  CardContent,
  CardDescription,
  CardTitle
} from '@/components/ui/card'
import { useState, useEffect } from 'react'
import { SourceDTO } from '@/types'

export default function Dashboard() {
  const [sources, setSources] = useState<SourceDTO[]>([])

  useEffect(() => {
    api.getSources()
      .then(sourceData => setSources(sourceData))
      .catch(err => {
        console.error('Failed to fetch jobs:', err);
      })
  }, []);

  return (
    <div>
      <h1 className="py-2">Tracked Sources</h1>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {sources.map((source, index) => (
          <Card key={index}>
            <CardContent>
              <CardTitle>{source.company_name}</CardTitle>
              <CardDescription>{source.category_name}</CardDescription>
              <CardDescription>{source.url}</CardDescription>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}

