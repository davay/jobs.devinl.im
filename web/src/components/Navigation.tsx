import { Link, useLocation } from 'react-router-dom'
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"
import { cn } from "@/lib/utils"
import { Github, FileText } from "lucide-react"

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

      <div className="flex items-center gap-4">
        <a
          href="https://devinl.im/project/2025/04/01/jobs/"
          className="flex items-center gap-1 text-sm font-bold hover:text-gray-700"
        >
          <FileText size={20} />
          <span className="hidden md:inline">Blog</span>
        </a>

        <a
          href="https://github.com/davay/jobs.devinl.im"
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center hover:text-gray-700"
        >
          <Github size={24} />
        </a>
      </div>
    </div>
  )
}
