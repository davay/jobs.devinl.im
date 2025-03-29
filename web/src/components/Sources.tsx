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
        console.error('Failed to fetch sources:', err);
      })
  }, []);

  return (
    <div>
      <h1 className="py-2">Tracked Sources</h1>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {sources.map((source, index) => (
          <a href={source.url} target="_blank">
            <Card key={index} className="h-48">
              <CardContent className="p-2 flex flex-col h-full">
                <CardTitle>{source.company_name}</CardTitle>
                <CardDescription>{source.category_name}</CardDescription>
                <div className="pt-2 mt-auto break-all overflow-hidden">{source.url}</div>
              </CardContent>
            </Card>
          </a>
        ))}
      </div>
    </div>
  )
}

