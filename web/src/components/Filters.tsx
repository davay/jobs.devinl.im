import { FilterProps } from '@/types'
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { KeyboardEvent, ChangeEvent, useState } from 'react'
import {
  Card,
  CardContent
} from '@/components/ui/card'
import { X } from "lucide-react"

export default function Filters({ keywords, setKeywords }: FilterProps) {
  const [inputValue, setInputValue] = useState<string>()
  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value)
  }
  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (inputValue && e.key === 'Enter' && inputValue.trim() !== '') {
      if (!keywords.includes(inputValue.trim())) {
        setKeywords([...keywords, inputValue.trim()])
        setInputValue('')
      }
      e.preventDefault()
    }
  }
  const removeKeyword = (keywordToRemove: string) => {
    setKeywords(keywords.filter(keyword => keyword !== keywordToRemove))
  }

  return (
    <div>
      <div className="pb-2">
        <h1 className="font-bold text-lg text-left pl-1 py-2">Keywords</h1>
        <p className="text-left text-sm pl-1 pb-2">This will be used to filter job titles. Multiple keywords are processed with an "OR".</p>
        <Input
          type="text"
          placeholder='E.g., "engineer", "project manager", "ml"'
          value={inputValue}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          className="rounded-lg"
        />
      </div>
      <Card className="h-full py-2">
        <CardContent className="px-2 min-h-10">
          <div className="flex flex-wrap gap-2">
            {keywords.length > 0 ? (
              keywords.map(keyword => (
                <Badge key={keyword} variant="secondary">
                  {keyword}
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => removeKeyword(keyword)}>
                    <X />
                  </Button>
                </Badge>
              ))
            ) : <p className="text-muted-foreground text-sm">Add keywords to begin...</p>
            }
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

