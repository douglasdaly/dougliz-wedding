# -*- coding: utf-8 -*-
"""
Wedding information database storage model.
"""
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class WeddingInfo(Base):
    """
    Wedding information database storage.
    """
    __tablename__ = 'wedding_info'

    id = sa.Column(sa.Integer, primary_key=True)

    # People
    bride_id = sa.Column(sa.Integer, sa.ForeignKey("people.id"))
    bride = relationship(
        "Person", foreign_keys=[bride_id]
    )
    groom_id = sa.Column(sa.Integer, sa.ForeignKey("people.id"))
    groom = relationship(
        "Person", foreign_keys=[groom_id]
    )

    # Events
    engagement_party_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    engagement_party = relationship(
        "Event", foreign_keys=[engagement_party_id]
    )
    welcome_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    welcome = relationship(
        "Event", foreign_keys=[welcome_id]
    )
    rehearsal_dinner_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    rehearsal_dinner = relationship(
        "Event", foreign_keys=[rehearsal_dinner_id]
    )
    wedding_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    wedding = relationship(
        "Event", foreign_keys=[wedding_id]
    )
    reception_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    reception = relationship(
        "Event", foreign_keys=[reception_id]
    )
    brunch_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    brunch = relationship(
        "Event", foreign_keys=[brunch_id]
    )
