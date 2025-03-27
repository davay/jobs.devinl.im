import { useNavigate, useLocation } from 'react-router-dom'

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
        <button
          key={item.path}
          onClick={() => navigate(item.path)}
          className={`px-4 py-2 rounded-md ${location.pathname === item.path ? 'bg-blue-400' : 'bg-gray-400'}`}
        >
          {item.label}
        </button>
      )}
    </div>
  )
}
