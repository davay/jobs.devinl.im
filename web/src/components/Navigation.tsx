import { Link, useLocation } from 'react-router-dom'
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"
import { cn } from "@/lib/utils"
import { Github } from "lucide-react"

export default function Navigation() {
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Dashboard' },
    { path: '/sources', label: 'Sources' },
    { path: '/filters', label: 'Filters' },
  ]

  return (
    <div className="p-4 w-full top-0 bg-white border rounded-md flex justify-between items-center">
      <NavigationMenu>
        <NavigationMenuList>
          {navItems.map(item => (
            <NavigationMenuItem key={item.path}>
              <Link
                to={item.path}
                className={cn(navigationMenuTriggerStyle(), location.pathname === item.path ? "bg-accent text-accent-foreground" : "bg-background")}
              >
                {item.label}
              </Link>
            </NavigationMenuItem>
          ))}
        </NavigationMenuList>
      </NavigationMenu>

      <a
        href="https://github.com/davay/jobs.devinl.im"
        target="_blank"
        rel="noopener noreferrer"
        className="flex items-center hover:text-gray-700"
      >
        <Github size={24} />
      </a>

    </div>
  )
}
