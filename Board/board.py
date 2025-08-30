from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# ==== 도메인 로직 (전역 변수 대신 클래스 인스턴스 사용) ====
class Board:
    def __init__(self):
        self.posts: List[dict] = []
        self.seq: int = 0

    def next_id(self) -> int:
        self.seq += 1
        return self.seq

    def all(self) -> List[dict]:
        return sorted(self.posts, key=lambda x: x["id"])

    def get(self, pid: int) -> Optional[dict]:
        return next((p for p in self.posts if p["id"] == pid), None)

    def create(self, title: str, content: str) -> dict:
        post = {
            "id": self.next_id(),
            "title": title,
            "content": content,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.posts.append(post)
        return post

    def update(self, pid: int, title: str, content: str) -> Optional[dict]:
        p = self.get(pid)
        if p:
            p["title"] = title
            p["content"] = content
        return p

    def delete(self, pid: int) -> bool:
        before = len(self.posts)
        self.posts = [p for p in self.posts if p["id"] != pid]
        return len(self.posts) < before


board = Board()  # 앱 시작 시 한 번만 생성


# ==== 웹 페이지 라우트 ====
@app.get("/", response_class=HTMLResponse)
def home():
    return RedirectResponse(url="/posts", status_code=302)


@app.get("/posts", response_class=HTMLResponse)
def list_posts(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "posts": board.all()}
    )


@app.get("/posts/new", response_class=HTMLResponse)
def new_post(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {"request": request, "mode": "create", "post": {"title": "", "content": ""}, "error": None}
    )


@app.post("/posts", response_class=HTMLResponse)
def create_post(
    request: Request,
    title: str = Form(""),
    content: str = Form("")
):
    title = (title or "").strip()
    content = (content or "").strip()
    if not title or not content:
        return templates.TemplateResponse(
            "form.html",
            {"request": request, "mode": "create", "post": {"title": title, "content": content}, "error": "제목/내용은 비울 수 없습니다."},
            status_code=400
        )
    post = board.create(title, content)
    return RedirectResponse(url=f"/posts/{post['id']}", status_code=303)


@app.get("/posts/{post_id}", response_class=HTMLResponse)
def show_post(request: Request, post_id: int):
    post = board.get(post_id)
    if not post:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return templates.TemplateResponse("show.html", {"request": request, "post": post})


@app.get("/posts/{post_id}/edit", response_class=HTMLResponse)
def edit_post(request: Request, post_id: int):
    post = board.get(post_id)
    if not post:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return templates.TemplateResponse("form.html", {"request": request, "mode": "edit", "post": post, "error": None})


@app.post("/posts/{post_id}", response_class=HTMLResponse)
def update_post(
    request: Request,
    post_id: int,
    title: str = Form(""),
    content: str = Form("")
):
    title = (title or "").strip()
    content = (content or "").strip()
    if not title or not content:
        return templates.TemplateResponse(
            "form.html",
            {"request": request, "mode": "edit", "post": {"id": post_id, "title": title, "content": content}, "error": "제목/내용은 비울 수 없습니다."},
            status_code=400
        )

    updated = board.update(post_id, title, content)
    if not updated:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

    return RedirectResponse(url=f"/posts/{post_id}", status_code=303)


@app.post("/posts/{post_id}/delete", response_class=HTMLResponse)
def delete_post(post_id: int):
    ok = board.delete(post_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url="/posts", status_code=303)


# ==== 간단 API (JSON) 예시 ====
from fastapi.responses import JSONResponse

@app.get("/api/posts")
def api_list():
    return JSONResponse(board.all(), media_type="application/json; charset=utf-8")

@app.get("/api/posts/{post_id}")
def api_show(post_id: int):
    post = board.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")
    return JSONResponse(post, media_type="application/json; charset=utf-8")
