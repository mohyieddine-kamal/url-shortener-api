from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from auth import require_api_key
from database import get_db
from models import URL
from schemas import URLCreate, URLOut
from services.shortener import generate_short_code

router = APIRouter(dependencies=[Depends(require_api_key)])
public_router = APIRouter()


@router.post("/shorten", response_model=URLOut, status_code=status.HTTP_201_CREATED)
def create_short_url(payload: URLCreate, db: Session = Depends(get_db)):
    while True:
        code = generate_short_code()
        existe_deja = db.query(URL).filter_by(short_code=code).first()
        if existe_deja is None:
            break

    nouvelle_url = URL(short_code=code, original_url=str(payload.original_url))
    db.add(nouvelle_url)
    db.commit()
    db.refresh(nouvelle_url)

    return nouvelle_url


@public_router.get("/{code}")
def redirect_to_original(code: str, db: Session = Depends(get_db)):
    url_entry = db.query(URL).filter_by(short_code=code).first()

    if url_entry is None:
        raise HTTPException(status_code=404, detail="Code introuvable")

    url_entry.click_count += 1
    db.commit()

    return RedirectResponse(url=url_entry.original_url)