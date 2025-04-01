import api from '@/api'
import {
  Card,
  CardContent,
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
      <p className="text-left text-sm pl-1 pb-2">A source's category may not be comparable between companies. For example, while Microsoft groups into "professions" (broad categories), Apple groups by teams (so program manager jobs can be found inside its "Software and Services" category).</p>
      <p className="text-left text-sm pl-1 pb-2">
        Note: Where possible, all sources are exclusively filtered to jobs within the U.S. (excluding some smaller companies, but majority of their jobs are within the U.S. anyway).</p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {sources.map((source, index) => (
          <a key={index} href={source.url} target="_blank">
            <Card className="h-full">
              <CardHeader>
                <CardTitle>{source.company_name}</CardTitle>
                <CardDescription>{source.category_name}</CardDescription>
                <div className="h-20 overflow-y-auto">
                  <CardDescription className="break-all">{source.url}</CardDescription>
                </div>
              </CardHeader>
              <CardContent>
                <CardDescription>
                  Last refreshed: {source.last_refreshed}
                </CardDescription>
              </CardContent>
            </Card>
          </a>
        ))}
      </div>
    </div>
  )
}

