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
    <div className="flex flex-row">
      {navItems.map(item =>
        <button
          key={item.path}
          onClick={() => navigate(item.path)}
          className={`${location.pathname === item.path ? 'bg-red-500' : 'bg-gray-500'}`}
        >
          {item.label}
        </button>
      )}
    </div>
  )
}
