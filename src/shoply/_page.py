from typing import Any, Callable, Dict, Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")


class Page(Generic[T]):
    """One page of a list: `data` its rows, `page` which page, `pages` how many there are, `total`
    the rows in all, `meta` whatever else the list answers beside its rows. A `for` loop over it
    walks every row from this page on, asking for the next page as it goes.
    """

    def __init__(
        self,
        data: List[T],
        page: int,
        pages: Optional[int],
        total: Optional[int],
        meta: Optional[Dict[str, Any]],
        next: Callable[[int], "Page[T]"],
    ) -> None:
        self.data = data
        self.page = page
        self.pages = pages
        self.total = total
        self.meta = meta
        self._next = next

    def has_next_page(self) -> bool:
        return self.pages is not None and self.page < self.pages

    def next_page(self) -> Optional["Page[T]"]:
        """The page after this one, or None when this is the last."""
        return self._next(self.page + 1) if self.has_next_page() else None

    def __iter__(self) -> Iterator[T]:
        page: Optional[Page[T]] = self
        while page is not None:
            yield from page.data
            page = page.next_page()

    def __repr__(self) -> str:
        return f"<Page {self.page} of {self.pages}, {len(self.data)} rows of {self.total}>"
