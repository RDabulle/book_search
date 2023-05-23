class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def search_by_title(self, keyword):
        if keyword in self.title:
            return True
        return False

    def search_by_author(self, keyword):
        if keyword in self.author:
            return True
        return False

    def search_by_publisher(self, keyword):
        if keyword in self.publisher:
            return True
        return False

# 도서 생성
book1 = Book("파이썬 프로그래밍", "John Smith", "출판사A")
book2 = Book("자바 기초", "Emily Johnson", "출판사B")

# 도서 검색 함수
def search_books(books, keyword, search_type):
    result = []
    for book in books:
        if search_type == "title":
            if book.search_by_title(keyword):
                result.append(book)
        elif search_type == "author":
            if book.search_by_author(keyword):
                result.append(book)
        elif search_type == "publisher":
            if book.search_by_publisher(keyword):
                result.append(book)
    return result

# 도서 목록
books = [book1, book2]

# 도서 검색
search_keyword = input("검색어를 입력하세요: ")
search_type = input("검색 유형을 선택하세요 (title/author/publisher): ")

results = search_books(books, search_keyword, search_type)

# 검색 결과 출력
if results:
    print("검색 결과:")
    for book in results:
        print(f"제목: {book.title}, 저자: {book.author}, 출판사: {book.publisher}")
else:
    print("검색 결과가 없습니다.")