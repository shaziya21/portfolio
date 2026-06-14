from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.auth import get_current_user
from backend.database import get_db
from backend.models import Experience, User
from backend.schemas import ExperienceCreate, ExperienceOut, ExperienceUpdate

router = APIRouter(prefix="/api/experiences", tags=["experiences"])


@router.get("", response_model=list[ExperienceOut])
def list_experiences(db: Session = Depends(get_db)):
    return (
        db.query(Experience)
        .order_by(Experience.order_index.desc(), Experience.id.desc())
        .all()
    )


@router.post("", response_model=ExperienceOut, status_code=status.HTTP_201_CREATED)
def create_experience(
    payload: ExperienceCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    max_order = db.query(Experience.order_index).order_by(Experience.order_index.desc()).first()
    next_order = (max_order[0] + 1) if max_order else 0

    experience = Experience(**payload.model_dump(), order_index=next_order)
    db.add(experience)
    db.commit()
    db.refresh(experience)
    return experience


@router.put("/{experience_id}", response_model=ExperienceOut)
def update_experience(
    experience_id: int,
    payload: ExperienceUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(experience, field, value)

    db.commit()
    db.refresh(experience)
    return experience


@router.delete("/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")

    db.delete(experience)
    db.commit()
