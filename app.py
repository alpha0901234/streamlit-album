import streamlit as st

print("Album")

st.set_page_config(
    page_title='음식 사진 앨범',
    page_icon='./images/food.png'
)

st.title("Food Album")
st.text(' "여러 종류의 음식 사진으로 앨범을 채워보세요!" ')

types={
    "한식" : "한식",
    "양식": "양식",
    "중식" : "중식",
    "일식" : "일식",
    "후식" : "후식",
    "음료" : "음료",
    "퓨전" : "퓨전",
    "기타": "기타",
    }

initial_pictures = [
    {
    "name" : "돌솥밥",
    "type": ["한식"],
    "year": "2023",
    "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMjhfMjgg%2FMDAxNzAzNzYzODYxMTU3.rexOwF5wbp6gHH-fxsmyEnXXEppywuJAZMRo-zt3Vogg.4TqSv0oBUxYKAyH_txtJsAYdLXN6BjALOMxKZ3P04Sgg.JPEG.ok_everything%2FKakaoTalk_20231228_203821168_12.jpg&type=sc960_832"
    },
    {
    "name" : "스테이크",
    "type": ["양식"],
    "year": "2024",
    "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAyMDlfMjQy%2FMDAxNzA3NDA3MjQ3MjQy.ty1nK6-WGcMqwtQfxLt-C3q6BejeL9E9xc_60TD6Sdkg.0TV2zMTb3EPI7UNFO0Fgi1s34FccDmp1LrbeMRgwPkog.JPEG.huu3051%2FIMG_8207.jpg&type=sc960_832"
    },
    {
    "name" : "딤섬",
    "type": ["중식"],
    "year": "2020",
    "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDEyMDFfOTAg%2FMDAxNjA2Nzk0OTc3NTU1.4JcudeKNHO4rfp7XoC6S3onEfHOG5INiQSNCDrwKoE4g.jHLjlFJQPx0JeYgnGybmdhWQuSDZzYkEt32zZgwr7psg.JPEG.ye_jin42%2FIMG_7508.JPG&type=sc960_832"
    },
    {
    "name" : "초밥",
    "type": ["일식"],
    "year": "2018",
    "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODAyMTNfMTEy%2FMDAxNTE4NTI0NjQ0MjA1.c9eP8tjY8uVDvppgwpD9L082CbX6_lo3GTEIZIkLaJIg.c-Ct47M9dvm3BXdmQ2eUVyCTDqKHtm53GHfGFTijV7Ig.JPEG.mythya0730%2F1235IMG_1778.JPG&type=sc960_832"
    }]

example_picture = {
    "name" : "아이스크림",
    "type": "후식",
    "year": "2021",
    "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA5MDVfMjcy%2FMDAxNjMwODIyNTAwODY4.Ab0vfnqvgDav-H8s0qy7zEvy_7Yn_qifmWkuiWIIGUIg.GgnWZUL88GZOlV-Ty_XxVLKHybM91XQ-JbdWBaaKBEog.JPEG.heeri1212%2FBeautyPlus%25A3%25DF20210905150334799%25A3%25DFsave.jpg&type=sc960_832"
    }

if "pictures" not in st.session_state:
    st.session_state.pictures = initial_pictures

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)

with st.form(key='form'):
    col1, col2, col3= st.columns(3)
    with col1:
        name = st.text_input(
            label="음식 이름",
            value=example_picture["name"] if auto_complete else ""
            )
    with col2:
        type = st.multiselect(
            label="음식 종류",
            options=list(types),
            max_selections = 2,
            default=example_picture["type"] if auto_complete else []
            )
    with col3:
        year = st.text_input(
            label="음식 촬영 연도",
            value=example_picture["year"] if auto_complete else ""
            )

    image_url = st.text_input(
        label="이미지 URL",
        value=example_picture["image_url"] if auto_complete else "")
    submit = st.form_submit_button(label="저장")

    if submit:
        if not name:
            st.error("사진의 이름을 입력해주세요.")
        elif len(type) == 0:
            st.error("사진의 종류를 적어도 한 개 선택해주세요.")
        elif not year:
            st.error("사진의 촬영 연도를 입력해주세요.")
        else:
            st.success("사진을 추가할 수 있습니다.")
            st.session_state.pictures.append({
                "name": name,
                "year": year,
                "type": type,
                "image_url": image_url if image_url else "./images/default.png"
                })

for i in range(0, len(st.session_state.pictures), 4):
    row_pictures = st.session_state.pictures[i:i+4]
    cols = st.columns(4)
    for j in range(len(row_pictures)):
        with cols[j]:
            picture = row_pictures[j]
            with st.expander(label=f"**{i+j+1}. {picture['name']}**", expanded=True):
                st.text("in " + picture['year'])
                st.image(picture["image_url"])
                st.text("(" + "/".join(picture["type"]) + ")")
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked")
                    del st.session_state.pictures[i+j]
                    st.rerun()