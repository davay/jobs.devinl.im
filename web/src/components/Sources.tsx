import api from '@/api'
import {
  Card,
  CardHeader,
  CardDescription,
  CardTitle
} from '@/components/ui/card'
import { useState, useEffect } from 'react'
import { SourceDTO } from '@/types'

export default function Sources() {
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
      <h1 className="font-bold text-lg text-left pl-1 py-2">Tracked Sources</h1>
      <p className="text-left text-sm pl-1 pb-2">A source's category may not be comparable between companies. For example, Microsoft categorizes into "professions" (broad categories) while Apple groups by teams (so program manager jobs can be found inside its Software category).</p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {sources.map((source, index) => (
          <a href={source.url} target="_blank">
            <Card key={index} className="h-full">
              <CardHeader>
                <CardTitle>{source.company_name}</CardTitle>
                <CardDescription>{source.category_name}</CardDescription>
                <div className="h-20 overflow-y-auto">
                  <CardDescription className="break-all">{source.url}</CardDescription>
                </div>
              </CardHeader>
            </Card>
          </a>
        ))}
      </div>
    </div>
  )
}

