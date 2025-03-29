import './App.css'

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navigation from '@/components/Navigation'
import Dashboard from '@/components/Dashboard'
import Sources from '@/components/Sources'
import Notification from '@/components/Notification'

const routes = [
  { path: '/', element: <Dashboard /> },
  { path: '/sources', element: <Sources /> },
  { path: '/notification', element: <Notification /> }
]

function App() {

  return (
    <div>
      <BrowserRouter>
        <div className="min-h-screen flex flex-col items-center">
          <div className="w-[75vw]">
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
