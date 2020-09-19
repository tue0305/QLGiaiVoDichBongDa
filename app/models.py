from flask import redirect, url_for
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user, logout_user
from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship

from app import admin, db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    userName = Column(String(45), nullable=False)
    passWord = Column(String(100), nullable=False)
    email = Column(String(45), nullable=False)
    birthDate = Column(Date)
    address = Column(String(45))
    role = Column(String(45), default="Admin")
    active = Column(Boolean, default=True)


class Tournament(db.Model):
    __tablename__ = "giaidau"
    maGD = Column(Integer, primary_key=True, autoincrement=True)
    tenGD = Column(String(45), nullable=False)
    ngayBatDau = Column(Date, nullable=False)
    ngayKetThuc = Column(Date, nullable=False)
    avatar = Column(String(200), default="https://img3.thuthuatphanmem.vn/uploads/2019/10/01/hinh-logo-bong-da_103805580.jpg")

    FK_GiaiDau_TranDauDoiBong = relationship("Tournament_Team", backref="giaidau", lazy=True)#

    def __str__(self):
        return self.tenGD


class Round(db.Model):
    __tablename__ = "vongdau"
    maVD = Column(Integer, primary_key=True, autoincrement=True)
    tenVD = Column(String(45), nullable=False)

    FK_VongDau_TranDau = relationship("Match", backref="vongdau", lazy=True)

    def __str__(self):
        return self.tenVD


class Team(db.Model): 
    __tablename__ = "doibong"
    maDB = Column(Integer, primary_key=True, autoincrement=True)
    tenDB = Column(String(45), nullable=False)
    sanNha = Column(String(45), nullable=False)
    soLuongCauThu = Column(Integer, nullable=False)
    avatar = Column(String(200), default="https://img3.thuthuatphanmem.vn/uploads/2019/10/01/mau-logo-bong-da-don-gian_103806674.png")

    FK_DoiBong_CauThu = relationship("Player", backref="doibong", lazy=True)

    FK_DoiBong_TranDauDoiBong = relationship("Tournament_Team", backref="doibong", lazy=True)#

    def __str__(self):
        return self.tenDB


class Tournament_Team(db.Model):
    __tablename__ = "giaidauDoibong"
    maDB = Column(Integer, ForeignKey(Team.maDB), primary_key=True)
    maGD = Column(Integer, ForeignKey(Tournament.maGD), primary_key=True)


class Match(db.Model): 
    __tablename__ = "trandau"
    maTD = Column(Integer, primary_key=True, autoincrement=True)
    ngayThiDau = Column(Date, nullable=False)
    gioThiDau = Column(Float, nullable=False)
    sanThiDau = Column(String(45), nullable=False)

    tranDau = Column(Integer, ForeignKey(Team.maDB), nullable=False)
    tranDau1 = Column(Integer, ForeignKey(Team.maDB), nullable=False)
    doiNha = relationship("Team", foreign_keys=[tranDau])
    doiKhach = relationship("Team", foreign_keys=[tranDau1])

    maVD = Column(Integer, ForeignKey(Round.maVD), nullable=False)
    maGD = Column(Integer, ForeignKey(Tournament.maGD), nullable=False)
    
    FK_TranDau_BanThang = relationship("Goal", backref="trandau", lazy=True)

    # def __str__(self):
    #     return 

class PlayerType(db.Model): 
    __tablename__ = "loaicauthu"
    maLoaiCT = Column(Integer, primary_key=True, autoincrement=True)
    tenLoaiCT = Column(String(45), nullable=False)

    FK_LoaiCauThu_CauThu = relationship("Player", backref="loaicauthu", lazy=True)

    def __str__(self):
        return self.tenLoaiCT


class Player(db.Model):
    __tablename__ = "cauthu"
    maCT = Column(Integer, primary_key=True, autoincrement=True)
    tenCT = Column(String(45), nullable=False)
    ngaySinh = Column(Date, nullable=False)
    ghiChu = Column(String(100), nullable=True)
    avatar = Column(String(200), default="https://free.vector6.com/wp-content/uploads/2020/06/T6-U30-lvmuq2-Vector-Bong-Da-012.jpg")

    maLoaiCT = Column(Integer, ForeignKey(PlayerType.maLoaiCT), nullable=False)
    maDB = Column(Integer, ForeignKey(Team.maDB), nullable=False)
    
    FKBanThangCauThu = relationship("Goal", backref="cauthu", lazy=True)

    def __str__(self):
        return self.tenCT


class GoalScored(db.Model): 
    __tablename__ = "loaibanthang"
    maLoaiBT = Column(Integer, primary_key=True, autoincrement=True)
    tenLoaiBT = Column(String(45), nullable=False)

    FK_LoaiBanThang_BanThang = relationship("Goal", backref="loaibanthang", lazy=True)

    def __str__(self):
        return self.tenLoaiBT


class Goal(db.Model):
    __tablename__ = "banthang"
    maBT = Column(Integer, primary_key=True, autoincrement=True)
    thoiDiem = Column(Float, nullable=False)

    maTD = Column(Integer, ForeignKey(Match.maTD), nullable=False)
    maCT = Column(Integer, ForeignKey(Player.maCT), nullable=False)
    maLoaiBT = Column(Integer, ForeignKey(GoalScored.maLoaiBT), nullable=False)


class Regulation(db.Model):
    __tablename__ = "quydinh"
    maQD = Column(Integer, primary_key=True, autoincrement=True)
    tuoiToiThieu = Column(Integer, nullable=False)
    tuoiToiDa = Column(Integer, nullable=False)
    soCauThuToiThieu = Column(Integer, nullable=False)
    soCauThuToiDa = Column(Integer, nullable=False)
    soCauThuNuocNgoaiToiDa = Column(Integer, nullable=False)
    thoiDiemGhiBanToiDa = Column(Integer, nullable=False)
    diemSoThang = Column(Integer, nullable=False)
    diemSoThua = Column(Integer, nullable=False)
    diemSoHoa = Column(Integer, nullable=False)
    thuTuUuTienXepHang = Column(Integer, nullable=False)

#-------admin-------

class TournamentModelView(ModelView):
    column_display_pk = True
    
    def is_accessible(self):
        return current_user.is_authenticated

class RoundModelView(ModelView):
    column_display_pk = True
    
    def is_accessible(self):
        return current_user.is_authenticated

class TeamModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

class MatchModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

class PlayerTypeModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

class PlayerModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

class GoalScoredModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

class GoalModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

class RegulationModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

class UserModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

#======= view =======

class AboutUsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/about-us.html')
    def is_accessible(self):
        return True

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect(url_for('login_users'))
    def is_accessible(self):
        return current_user.is_authenticated
#======= endview =======

admin.add_view(TournamentModelView(Tournament, db.session))
admin.add_view(RoundModelView(Round, db.session))
admin.add_view(TeamModelView(Team, db.session))
admin.add_view(MatchModelView(Match, db.session))
admin.add_view(PlayerTypeModelView(PlayerType, db.session))
admin.add_view(PlayerModelView(Player, db.session))
admin.add_view(GoalScoredModelView(GoalScored, db.session))
admin.add_view(GoalModelView(Goal, db.session))
admin.add_view(RegulationModelView(Regulation, db.session))
admin.add_view(UserModelView(User, db.session))

admin.add_view(ModelView(Tournament_Team, db.session))#

admin.add_view(AboutUsView(name='About us'))
admin.add_view(LogoutView(name='Logout'))
#------- endadmin -------