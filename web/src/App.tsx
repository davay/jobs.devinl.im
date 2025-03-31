import './App.css'

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navigation from '@/components/Navigation'
import Dashboard from '@/components/Dashboard'
import Sources from '@/components/Sources'
import Filters from '@/components/Filters'
import { useState } from 'react'
import { getFromStorage } from '@/lib/utils'


function App() {
  const [keywords, setKeywords] = useState<string[]>(() =>
    getFromStorage<string[]>('keywords', [])
  );
  const routes = [
    { path: '/', element: <Dashboard keywords={keywords} /> },
    { path: '/sources', element: <Sources /> },
    { path: '/filters', element: <Filters keywords={keywords} setKeywords={setKeywords} /> },
  ]

  return (
    <div>
      <BrowserRouter>
        <div className="min-h-screen flex flex-col items-center">
          <div className="w-[75vw] max-w-[1200px]">
            <Navigation />
            <div className="pt-4">
              <Routes>
                {routes.map(route =>
                  <Route key={route.path} path={route.path} element={route.element} />
                )}
              </Routes>
            </div>
          </div>
        </div>
      </BrowserRouter>
    </div>
  )
}

export default App
