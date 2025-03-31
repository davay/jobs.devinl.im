import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,

  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"

import { DashboardPaginationProps } from "@/types"

export default function DashboardPagination({ page, setPage, totalPages }: DashboardPaginationProps) {
  // page starts from 0, but display from 1
  const displayPage = page + 1;

  return (
    <Pagination>
      <PaginationContent>
        <PaginationItem>
          <PaginationPrevious
            onClick={() => page > 0 && setPage(page - 1)}
          />
        </PaginationItem>

        {/* always show first page */}
        <PaginationItem>
          <PaginationLink
            isActive={displayPage === 1}
            onClick={() => setPage(0)}
          >
            1
          </PaginationLink>
        </PaginationItem>

        {/* current page */}
        {(displayPage !== 1 && displayPage !== totalPages) ? (
          <PaginationItem>
            <PaginationLink isActive={true}>
              {displayPage}
            </PaginationLink>
          </PaginationItem>
        ) : (displayPage !== totalPages && displayPage + 1 !== totalPages) && <PaginationEllipsis />}

        {/* always show last page */}
        {totalPages > 1 && (
          <PaginationItem>
            <PaginationLink
              isActive={displayPage === totalPages}
              onClick={() => setPage(totalPages - 1)}
            >
              {totalPages}
            </PaginationLink>
          </PaginationItem>
        )}

        <PaginationItem>
          <PaginationNext
            onClick={() => displayPage < totalPages && setPage(page + 1)}
          />
        </PaginationItem>
      </PaginationContent>
    </Pagination>
  );
}
