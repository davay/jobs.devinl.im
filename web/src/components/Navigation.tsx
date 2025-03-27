import { useNavigate, useLocation } from 'react-router-dom'
import { Button } from "@/components/ui/button"

export default function Navigation() {
  const navigate = useNavigate()
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Dashboard' },
    { path: '/sources', label: 'Sources' },
    { path: '/notification', label: 'Notification' }
  ]

  return (
    <div className="flex flex-row gap-4">
      {navItems.map(item =>
        <Button
          key={item.path}
          onClick={() => navigate(item.path)}
          variant={`${location.pathname === item.path ? 'outline' : 'secondary'}`}
        >
          {item.label}
        </Button>
      )}
    </div>
  )
}
