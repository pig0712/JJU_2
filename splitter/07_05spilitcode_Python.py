from langchain_text_splitters import HTMLHeaderTextSplitter

html_string = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>전주대학교 인공지능학과 소개</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #003366;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav {
            background-color: #f2f2f2;
            padding: 10px;
            text-align: center;
        }
        nav a {
            margin: 0 15px;
            text-decoration: none;
            color: #003366;
            font-weight: bold;
        }
        .container {
            padding: 20px;
        }
        section {
            margin-bottom: 40px;
        }
        footer {
            background-color: #003366;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>전주대학교 인공지능학과</h1>
        <p>미래를 이끄는 인공지능 전문가 양성</p>
    </header>

    <nav>
        <a href="#overview">학과 소개</a>
        <a href="#curriculum">교육 과정</a>
        <a href="#faculty">교수진</a>
        <a href="#research">연구 분야</a>
        <a href="#contact">문의하기</a>
    </nav>

    <div class="container">
        <section id="overview">
            <h2>학과 소개</h2>
            <p>전주대학교 인공지능학과는 최신 인공지능 기술과 이론을 바탕으로 창의적이고 문제 해결 능력을 갖춘 인재를 양성하는 것을 목표로 합니다. 학생들은 머신러닝, 딥러닝, 데이터 분석 등 다양한 분야에서 전문 지식을 습득하며, 실제 프로젝트를 통해 실무 경험을 쌓을 수 있습니다.</p>
        </section>

        <section id="curriculum">
            <h2>교육 과정</h2>
            <ul>
                <li>기초 프로그래밍</li>
                <li>데이터 구조 및 알고리즘</li>
                <li>머신러닝</li>
                <li>딥러닝</li>
                <li>자연어 처리</li>
                <li>컴퓨터 비전</li>
                <li>빅데이터 분석</li>
                <li>인공지능 프로젝트</li>
            </ul>
        </section>

        <section id="faculty">
            <h2>교수진</h2>
            <ul>
                <li>홍길동 교수 - 머신러닝 전문가</li>
                <li>김영희 교수 - 딥러닝 및 자연어 처리 연구</li>
                <li>이철수 교수 - 데이터 분석 및 빅데이터 연구</li>
                <li>박지수 교수 - 컴퓨터 비전 및 이미지 처리</li>
            </ul>
        </section>

        <section id="research">
            <h2>연구 분야</h2>
            <p>전주대학교 인공지능학과는 다음과 같은 주요 연구 분야를 중심으로 연구 활동을 전개하고 있습니다:</p>
            <ul>
                <li>머신러닝 알고리즘 개발</li>
                <li>딥러닝 모델 최적화</li>
                <li>자연어 처리 및 음성 인식</li>
                <li>컴퓨터 비전 및 이미지 분석</li>
                <li>빅데이터 분석 및 처리</li>
                <li>인공지능 응용 시스템</li>
            </ul>
        </section>

        <section id="contact">
            <h2>문의하기</h2>
            <p>전주대학교 인공지능학과에 대한 문의는 아래 연락처를 통해 가능합니다:</p>
            <ul>
                <li>전화: 063-123-4567</li>
                <li>이메일: ai@jeonju.ac.kr</li>
                <li>주소: 전라북도 전주시 덕진구 전주대학로 99</li>
            </ul>
        </section>
    </div>

    <footer>
        <p>&copy; 2024 전주대학교 인공지능학과. All rights reserved.</p>
    </footer>
</body>
</html>
"""


headers_to_split_on = [
    ("h1", "Header 1"),  # 분할할 헤더 태그와 해당 헤더의 이름을 지정합니다.
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

# 지정된 헤더를 기준으로 HTML 텍스트를 분할하는 HTMLHeaderTextSplitter 객체를 생성합니다.
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
# HTML 문자열을 분할하여 결과를 html_header_splits 변수에 저장합니다.
html_header_splits = html_splitter.split_text(html_string)
# 분할된 결과를 출력합니다.
for header in html_header_splits:
    print(f"{header.page_content}")
    print(f"{header.metadata}", end="\n=====================\n")