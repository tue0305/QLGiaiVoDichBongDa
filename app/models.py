from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app import admin, db


class Round(db.Model):
    __tablename__ = "vongdau"
    MaVD = Column(Integer, primary_key=True, autoincrement=True)
    TenVD = Column(String(45), nullable=False)

    FKTranDauVongDau = relationship("Match", backref="vongdau", lazy=True)

    # def __str__(self):
    #     return self.name

class Match(db.Model): 
    __tablename__ = "trandau"
    MaTD = Column(Integer, primary_key=True, autoincrement=True) #Column(String(10), primary_key=True)
    DoiNha = Column(String(45), nullable=False)
    DoiKhach = Column(String(45), nullable=False)
    NgayThiDau = Column(Date, nullable=False)
    GioThiDau = Column(Float, nullable=False)
    SanThiDau = Column(String(45), nullable=False)
    
    MaVD = Column(Integer, ForeignKey(Round.MaVD), nullable=False)

    FKBanThangTranDau = relationship("Goal", backref="trandau", lazy=True)

    # def __str__(self):
    #     return self.name

class Team(db.Model): 
    __tablename__ = "doibong"
    MaDB = Column(Integer, primary_key=True, autoincrement=True)#Column(String(10), primary_key=True)
    TenDB = Column(String(50), nullable=False)
    SanNha = Column(String(50), nullable=False)
    SoLuongCauThu = Column(Integer, nullable=False)

    # MaTranDau = Column(String(10), ForeignKey(Match.DoiNha))
    # MaTranDau1 = Column(String(10), ForeignKey(Match.DoiKhach))

    FKCauThuDoiBong = relationship("Player", backref="doibong", lazy=True)

    def __str__(self):
        return self.name

class PlayerType(db.Model): 
    __tablename__ = "loaicauthu"
    MaLoaiCT = Column(Integer, primary_key=True, autoincrement=True)#Column(String(10), primary_key=True)
    TenLoaiCT = Column(String(45), nullable=False)

    FKCauThuLoaiCauThu = relationship("Player", backref="loaicauthu", lazy=True)

    # def __str__(self):
    #     return self.name

class Player(db.Model):
    __tablename__ = "cauthu"
    MaCT = Column(Integer, primary_key=True, autoincrement=True)#Column(String(10), primary_key=True)
    TenCT = Column(String(45), nullable=False)
    NgaySinh = Column(Date, nullable=False)
    GhiChu = Column(String(50), nullable=True)

    MaLoaiCT = Column(Integer, ForeignKey(PlayerType.MaLoaiCT), nullable=False)
    MaDB = Column(Integer, ForeignKey(Team.MaDB), nullable=False)

    FKBanThangCauThu = relationship("Goal", backref="cauthu", lazy=True)

    def __str__(self):
        return self.name

class GoalScored(db.Model): 
    __tablename__ = "loaibanthang"
    MaLoaiBT = Column(Integer, primary_key=True, autoincrement=True)#Column(String(10), primary_key=True)
    TenLoaiBT = Column(String(45), nullable=False)

    FKBanThangLoaiBanThang = relationship("Goal", backref="loaibanthang", lazy=True)

    # def __str__(self):
    #     return self.name

class Goal(db.Model):
    __tablename__ = "banthang"
    MaBT = Column(Integer, primary_key=True, autoincrement=True)#Column(String(10), primary_key=True)
    ThoiDiem = Column(Float, nullable=False)

    MaTD = Column(Integer, ForeignKey(Match.MaTD), nullable=False)
    MaCT = Column(Integer, ForeignKey(Player.MaCT), nullable=False)
    MaLoaiBT = Column(Integer, ForeignKey(GoalScored.MaLoaiBT), nullable=False)

    def __str__(self):
        return self.name

class Regulation(db.Model):
    __tablename__ = "quydinh"
    MaQD = Column(Integer, primary_key=True, autoincrement=True)#Column(Integer, primary_key=True, autoincrement=True)
    TuoiToiThieu = Column(Integer, nullable=False)
    TuoiToiDa = Column(Integer, nullable=False)
    SoCauThuToiThieu = Column(Integer, nullable=False)
    SoCauThuToiDa = Column(Integer, nullable=False)
    SoCauThuNuocNgoaiToiDa = Column(Integer, nullable=False)
    ThoiDiemGhiBanToiDa = Column(Integer, nullable=False)
    DiemSoThang = Column(Integer, nullable=False)
    DiemSoThua = Column(Integer, nullable=False)
    DiemSoHoa = Column(Integer, nullable=False)
    ThuTuUuTienXepHang = Column(Integer, nullable=False)

    def __str__(self):
        return self.name

#-------admin-------

class RoundModelView(ModelView):
    column_display_pk = True

class MatchModelView(ModelView):
    column_display_pk = True

class TeamModelView(ModelView):
    column_display_pk = True

class PlayerTypeModelView(ModelView):
    column_display_pk = True

class PlayerModelView(ModelView):
    column_display_pk = True

class GoalScoredModelView(ModelView):
    column_display_pk = True

class GoalModelView(ModelView):
    column_display_pk = True

class RegulationModelView(ModelView):
    column_display_pk = True

admin.add_view(RoundModelView(Round, db.session))
admin.add_view(MatchModelView(Match, db.session))
admin.add_view(TeamModelView(Team, db.session))
admin.add_view(PlayerTypeModelView(PlayerType, db.session))
admin.add_view(PlayerModelView(Player, db.session))
admin.add_view(GoalScoredModelView(GoalScored, db.session))
admin.add_view(GoalModelView(Goal, db.session))
admin.add_view(RegulationModelView(Regulation, db.session))

#-------endadmin-------