import tkinter as tk
from tkinter import messagebox, simpledialog

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.reviews = []
        self.ratings = []
        self.pass_score = 0
        self.points = 0

    def add_review(self, review):
        self.reviews.append(review)

    def add_rating(self, rating):
        self.ratings.append(rating)

    def set_pass_score(self, score):
        self.pass_score = score

    def set_points(self, points):
        self.points = points

    def get_book_info(self):
        info = f"제목: {self.title}\n저자: {self.author}\n장르: {self.genre}\n통과 점수: {self.pass_score}\n포인트: {self.points}\n"
        return info

    def calculate_average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        else:
            return 0.0

class Community:
    def __init__(self):
        self.books = []
        self.current_user = None

    def add_book(self, book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda book: book.title)

    def write_review_and_rate(self, reviewer, book_title):
        for book in self.books:
            if book.title == book_title:
                review = simpledialog.askstring("후기 작성", "도서 후기를 작성하세요:")
                rating = simpledialog.askinteger("평점 메기기", "도서 평점을 매겨주세요 (1~5):", minvalue=1, maxvalue=5)
                book.add_review(review)
                book.add_rating(rating)
                messagebox.showinfo("작성 완료", "후기 작성 및 평점 메기기가 완료되었습니다.")
                break

    def calculate_average_rating(self):
        total_ratings = []
        for book in self.books:
            total_ratings.extend(book.ratings)
        if total_ratings:
            return sum(total_ratings) / len(total_ratings)
        else:
            return 0.0
        
    def sort_books(self):
        self.books.sort(key=lambda book: book.title)

    def search_books(self, keyword, search_type):
        if search_type == "제목":
            results = list(filter(lambda book: keyword.lower() in book.title.lower(), self.books))
        elif search_type == "저자":
            results = list(filter(lambda book: keyword.lower() in book.author.lower(), self.books))
        elif search_type == "장르":
            results = list(filter(lambda book: keyword.lower() in book.genre.lower(), self.books))
        else:
            results = []
        return results

    def register_user(self, username, password):
        if self.check_username_available(username):
            user = User(username, password)
            self.users.append(user)
            return True
        return False

    def check_username_available(self, username):
        for user in self.users:
            if user.username == username:
                return False
        return True
    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                return True
        return False

    def logout_user(self):
        self.current_user = None



# 도서 커뮤니티 생성
community = Community()
community.users = [User("user1", "password1"), User("user2", "password2")]  # 예시 사용자 생성

# 가입 함수
def register():
    username = simpledialog.askstring("가입", "사용자 이름을 입력하세요:")
    password = simpledialog.askstring("가입", "비밀번호를 입력하세요:", show='*')
    if community.register_user(username, password):
        messagebox.showinfo("가입 성공", "가입에 성공하였습니다. 이제 로그인해주세요.")
        disable_functionality()  # 가입 전에는 기능 비활성화
    else:
        messagebox.showwarning("가입 실패", "사용자 이름이 이미 사용 중입니다.")

# 로그인 함수
def login():
    username = simpledialog.askstring("로그인", "사용자 이름을 입력하세요:")
    password = simpledialog.askstring("로그인", "비밀번호를 입력하세요:", show='*')
    if community.authenticate_user(username, password):
        messagebox.showinfo("로그인 성공", "로그인에 성공하였습니다.")
        enable_functionality()  # 로그인 후에는 기능 활성화
    else:
        messagebox.showwarning("로그인 실패", "사용자 인증에 실패하였습니다.")
        disable_functionality()  # 로그인 실패 시 기능 비활성화

# 로그아웃 함수
def logout():
    community.logout_user()
    disable_functionality()  # 로그아웃 후에는 기능 비활성화
    messagebox.showinfo("로그아웃", "로그아웃되었습니다.")

# 로그인 성공 시 활성화할 기능들
def enable_functionality():
    write_review_button['state'] = 'normal'
    start_challenge_button['state'] = 'normal'
    logout_button['state'] = 'normal'
    register_button['state'] = 'disabled'
    login_button['state'] = 'disabled'
    add_book_button['state'] = 'normal'
    


# 로그아웃 시 비활성화할 기능들
def disable_functionality():
    write_review_button['state'] = 'disabled'
    start_challenge_button['state'] = 'disabled'
    logout_button['state'] = 'disabled'
    register_button['state'] = 'normal'
    login_button['state'] = 'normal'
    add_book_button['state'] = 'disabled'


# GUI 생성
window = tk.Tk()
window.title("도서 커뮤니티")
window.geometry("600x650")

# 예시 도서 추가
book1 = Book("위대한 개츠비", "F. 스콧 피츠제럴드", "서양문학(인문학)")
book1.set_pass_score(55)
book1.set_points(25)
community.add_book(book1)
book2 = Book("82년생 김지영", "조남주", "동양문학(인문학)")
book2.set_pass_score(65)
book2.set_points(25)
community.add_book(book2)
book3 = Book("걸리버 여행기", "조나단 스위프트", "서양문학(인문학)")
book3.set_pass_score(50)
book3.set_points(25)
community.add_book(book3)
book4 = Book("무례한 사람에게 웃으며 대처하는 법", "정문정", "인문학 일반(인문학)")
book4.set_pass_score(65)
book4.set_points(35)
community.add_book(book4)
book5 = Book("노인과 바다", "어니스트 헤밍웨이", "서양문학(인문학)")
book5.set_pass_score(50)
book5.set_points(25)
community.add_book(book5)
book6 = Book("나미야 잡화점의 기적", "히가시노 게이고", "동양문학(인문학)")
book6.set_pass_score(65)
book6.set_points(25)
community.add_book(book6)
book7 = Book("살인자의 기억법", "김영하", "동양문학(인문학)")
book7.set_pass_score(65)
book7.set_points(25)
community.add_book(book7)
book8 = Book("언어의 온도", "이기주", "동양문학(인문학)")
book8.set_pass_score(65)
book8.set_points(25)
community.add_book(book8)
book9 = Book("자존감 수업", "윤홍균", "인문학 일반(인문학)")
book9.set_pass_score(65)
book9.set_points(35)
community.add_book(book9)
book10 = Book("어린 왕자", "셍텍쥐페리", "동화")
book10.set_pass_score(75)
book10.set_points(15)
community.add_book(book10)
book11 = Book("죽은 시인의 사회", "톰 슐만", "서양문학(인문학)")
book11.set_pass_score(65)
book11.set_points(25)
community.add_book(book11)
book12 = Book("적을 만들지 않는 대화법", "샘 혼", "인문학 일반(인문학)")
book12.set_pass_score(65)
book12.set_points(35)
community.add_book(book12)
book13 = Book("선량한 차별주의자", "김지혜", "사회과학(인문학)")
book13.set_pass_score(65)
book13.set_points(30)
community.add_book(book13)
book14 = Book("레미제라블", "빅토르 위고", "서양문학(인문학)")
book14.set_pass_score(50)
book14.set_points(25)
community.add_book(book14)
book15 = Book("데미안", "헤름만 헤세", "서양문학(인문학)")
book15.set_pass_score(65)
book15.set_points(25)
community.add_book(book15)
book16 = Book("난장이가 쏘아올린 작은 공", "조세희", "동양문학(인문학)")
book16.set_pass_score(55)
book16.set_points(25)
community.add_book(book16)
book17 = Book("말의 품격", "이기주", "동양문학(인문학)")
book17.set_pass_score(65)
book17.set_points(25)
community.add_book(book17)
book18 = Book("인간실격", "다자이 오사무", "동양문학(인문학)")
book18.set_pass_score(65)
book18.set_points(25)
community.add_book(book18)
book19 = Book("(오은영의)화해", "오은영", "인문학 일반(인문학)")
book19.set_pass_score(70)
book19.set_points(35)
community.add_book(book19)
book20 = Book("달러구트 꿈 백화점 [1] : 주문하신 꿈은 매진입니다", "이미예", "동양문학(인문학)")
book20.set_pass_score(70)
book20.set_points(25)
community.add_book(book20)
book21 = Book("왜 세계의 절반은 굶주리는가", "장 지글러", "사회과학(인문학)")
book21.set_pass_score(65)
book21.set_points(30)
community.add_book(book21)
book22 = Book("감시와 처벌 (감옥의 역사)", "미셀 푸코", "사회과학(인문학)")
book22.set_pass_score(40)
book22.set_points(30)
community.add_book(book22)
book23 = Book("스무살에 알았더란면 좋았을 것들", "티나 실리그", "사회과학(인문학)")
book23.set_pass_score(65)
book23.set_points(30)
community.add_book(book23)
book24 = Book("불편한 편의점 : 김호연 장편소설", "김호연", "동양문학(인문학)")
book24.set_pass_score(70)
book24.set_points(25)
community.add_book(book24)
book25 = Book("동물농장", "오웰, 조지", "서양문학(인문학)")
book25.set_pass_score(60)
book25.set_points(15)
community.add_book(book25)
book26 = Book('긴긴밤',"루리","동화")
book26.set_pass_score(70)
book26.set_points(15)
community.add_book(book26)
book27 = Book("이반 일리치의 죽음","레프 톨스토이","서양문학")
book27.set_pass_score(50)
book27.set_points(15)
community.add_book(book27)
book28 = Book("나는 까칠하게 살기로 했다","양창순","인문학")
book28.set_pass_score(65)
book28.set_points(35)
community.add_book(book28)
book29 = Book("나는 내가 죽었다고 생각했습니다","질 볼트 테일러","기술과학")
book29.set_pass_score(65)
book29.set_points(30)
community.add_book(book29)
book30 = Book("정의란 무엇인가","마이클 샌델","인문학")
book30.set_pass_score(55)
book30.set_points(35)
community.add_book(book30)
book31 = Book("변신(Die Verwandlung).시골의사","프란츠 카프카","서양문학")
book31.set_pass_score(50)
book31.set_points(25)
community.add_book(book31)
book32 = Book("외환관리실무=Foreign exchange transaction pratice","이유춘","기타")
book32.set_pass_score(70)
book32.set_points(20)
community.add_book(book32)
book33 = Book("플라스틱 없는 삶","윌 맥컬럼","기술과학")
book33.set_pass_score(65)
book33.set_points(30)
community.add_book(book33)
book34 = Book("의사들이 들려주는 미세먼지와 건강 이야기","대한직업환경의학화","기술과학")
book34.set_pass_score(65)
book34.set_points(30)
community.add_book(book34)
book35 = Book("미움받을 용기1,2","기시미 이치로","인문학")
book35.set_pass_score(60)
book35.set_points(35)
community.add_book(book35)
book36 = Book("정재승의 과학 콘서트(복잡한 세상 명쾌한 과학)","정재승","순수과학")
book36.set_pass_score(40)
book36.set_points(30)
community.add_book(book36)
book37 = Book("카오스(새로운 과학의 출현)","제임스 글릭","순수과학")
book37.set_pass_score(40)
book37.set_points(30)
community.add_book(book37)
book38 = Book("1984","조지 오웰","서양문학")
book38.set_pass_score(65)
book38.set_points(25)
community.add_book(book38)
book39 = Book("메밀꽃 필 무렵","이효석","동양문학")
book39.set_pass_score(45)
book39.set_points(25)
community.add_book(book39)
book40 = Book("책을 삼키는 가장 완벽한 방법 : 읽어도 기억에 안남는 시람들을 위한 독서법","김세연","인문학")
book40.set_pass_score(55)
book40.set_points(35)
community.add_book(book40)
book41 = Book("오만과 편견(Pride and Prejudice)","제인 오스틴","서양문학")
book41.set_pass_score(55)
book41.set_points(25)
community.add_book(book41)
book42 = Book("날개","이상","동양문학")
book42.set_pass_score(40)
book42.set_points(25)
community.add_book(book42)
book43 = Book("요리 본늠(불 요리 그리고 진화)","리처드 랭엄","사회과학")
book43.set_pass_score(40)
book43.set_points(30)
community.add_book(book43)
book44 = Book("기업의 시대","CCTV 다큐 제작팀","사회과학")
book44.set_pass_score(45)
book44.set_points(30)
community.add_book(book44)
book45 = Book("엄마를 부탁해","신경숙","동양문학")
book45.set_pass_score(60)
book45.set_points(25)
community.add_book(book45)
book46 = Book("종의 기원","찰스 다윈","순수과학")
book46.set_pass_score(40)
book46.set_points(30)
community.add_book(book46)
book47 = Book("처음 만나는 뇌과학 이야기","양은우","기술과학")
book47.set_pass_score(80)
book47.set_points(30)
community.add_book(book47)
book48 = Book("마틴 셀리그만의 긍정심리학","마틴 셀리그만","인문학")
book48.set_pass_score(50)
book48.set_points(35)
community.add_book(book48)
book49 = Book("참회록","레프 톨스토이","기타")
book49.set_pass_score(40)
book49.set_points(15)
community.add_book(book49)
book50 = Book("연금술사","파울로 코엘료","서양문학")
book50.set_pass_score(60)
book50.set_points(25)
community.add_book(book50)

def show_book_info():
    selected_book = book_listbox.get(tk.ACTIVE)
    for book in community.books:
        if book.title == selected_book:
            info = f"제목: {book.title}\n저자: {book.author}\n장르: {book.genre}\n통과 점수: {book.pass_score}\n포인트: {book.points}\n"
            messagebox.showinfo("도서 정보", info)
            break

def search_books():
    keyword = search_entry.get()
    search_type = search_var.get()
    results = community.search_books(keyword, search_type)
    book_listbox.delete(0, tk.END)
    if results:
        for book in results:
            book_listbox.insert(tk.END, book.title)
    else:
        messagebox.showinfo("검색 결과", "일치하는 도서가 없습니다.")

def write_review_and_rate():
    selected_book = book_listbox.get(tk.ACTIVE)
    community.write_review_and_rate("사용자1", selected_book)

def calculate_community_average_rating():
    avg_rating = community.calculate_average_rating()
    messagebox.showinfo("커뮤니티 평균 평점", f"커뮤니티 전체 도서의 평균 평점: {avg_rating:.2f}")

# 가입 버튼
register_button = tk.Button(window, text="가입", command=register)
register_button.pack(pady=5)


# 로그인 버튼
login_button = tk.Button(window, text="로그인", command=login)
login_button.pack(pady=5)

# 로그아웃 버튼
logout_button = tk.Button(window, text="로그아웃", command=logout, state=tk.DISABLED)
logout_button.pack(pady=5)


# 도서 목록
book_frame = tk.Frame(window)
book_frame.pack(pady=10)

book_label = tk.Label(book_frame, text="도서 목록:")
book_label.pack()

book_listbox = tk.Listbox(book_frame, width=50)
book_listbox.pack()

for book in community.books:
    book_listbox.insert(tk.END, book.title)

# 도서 정보 버튼
info_button = tk.Button(window, text="도서 정보", command=show_book_info)
info_button.pack(pady=5)

# 후기 작성 버튼
write_review_button = tk.Button(window, text="후기 작성", command=write_review_and_rate)
write_review_button.pack(pady=5)

def view_reviews():
    selected_book = book_listbox.get(tk.ACTIVE)
    for book in community.books:
        if book.title == selected_book:
            reviews = "\n".join(book.reviews)
            messagebox.showinfo("후기 보기", f"{book.title} 도서의 후기:\n{reviews}")
            break

# 후기 보기 버튼
view_reviews_button = tk.Button(window, text="후기 보기", command=view_reviews)
view_reviews_button.pack(pady=5)

def start_challenge():
    title = simpledialog.askstring("독서 챌린지", "도서 제목을 입력하세요:")
    page_count = simpledialog.askinteger("독서 챌린지", "책 페이지 수를 입력하세요:")
    pages_per_day = simpledialog.askinteger("독서 챌린지", "하루에 읽을 페이지 수를 입력하세요:")

    for book in community.books:
        if book.title == title:
            days_to_complete = page_count / pages_per_day
            messagebox.showinfo("독서 챌린지 결과", f"{title} 도서를 완독하는데 {days_to_complete:.1f}일이 걸립니다.")
            break
    else:
        messagebox.showinfo("독서 챌린지 실패", "일치하는 도서가 없습니다.")


# 독서 챌린지 버튼
start_challenge_button = tk.Button(window, text="독서 챌린지", command=start_challenge)
start_challenge_button.pack(pady=5)


def show_quote():
    messagebox.showinfo("명언 인용구", "명언 인용구: '책은 마음을 풍요롭게 하는 양식이다.'")

# 명언 인용구 버튼
quote_button = tk.Button(window, text="명언 인용구", command=show_quote)
quote_button.pack(pady=5)


def add_book():
    title = simpledialog.askstring("도서 추가", "도서 제목을 입력하세요:")
    author = simpledialog.askstring("도서 추가", "도서 저자를 입력하세요:")
    genre = simpledialog.askstring("도서 추가", "도서 장르를 입력하세요:")
    pass_score = simpledialog.askinteger("도서 추가", "통과 점수를 입력하세요:")
    points = simpledialog.askinteger("도서 추가", "포인트를 입력하세요:")
    new_book = Book(title, author, genre)
    new_book.set_pass_score(pass_score)
    new_book.set_points(points)
    community.add_book(new_book)
    book_listbox.insert(tk.END, new_book.title)
    messagebox.showinfo("도서 추가", "도서가 성공적으로 추가되었습니다.")

# 도서 추가 버튼
add_book_button = tk.Button(window, text="도서 추가", command=add_book)
add_book_button.pack(pady=5)

# 검색
search_frame = tk.Frame(window)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="검색:")
search_label.grid(row=0, column=0)

search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1)

search_var = tk.StringVar()
search_var.set("제목")

search_type_dropdown = tk.OptionMenu(search_frame, search_var, "제목", "저자", "장르")
search_type_dropdown.grid(row=0, column=2)

search_button = tk.Button(search_frame, text="검색", command=search_books)
search_button.grid(row=0, column=3, padx=10)

# 커뮤니티 평균 평점
avg_rating_button = tk.Button(window, text="커뮤니티 평균 평점", command=calculate_community_average_rating)
avg_rating_button.pack(pady=5)

# 첫 시작 버튼 비활성화
disable_functionality()

window.mainloop()
