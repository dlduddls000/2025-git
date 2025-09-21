# main.py

# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
# from sqlalchemy.orm import sessionmaker, declarative_base
# import datetime
# import os

# # FastAPI 앱 인스턴스 생성
# app = FastAPI()

# # ----------------- 데이터베이스 설정 -----------------
# # 실제 데이터베이스 연결 정보로 교체하세요.
# DATABASE_URL = "postgresql://postgres:1128@localhost:5432/postgres"

# engine = create_engine(DATABASE_URL)
# Base = declarative_base()

# class EmploymentContract(Base):
#     __tablename__ = "employment_contracts"
#     id = Column(Integer, primary_key=True, index=True)
#     employer_name = Column(String)
#     employee_name = Column(String)
#     contract_content = Column(Text)
#     created_at = Column(DateTime, default=datetime.datetime.now)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # ----------------- AI 역할 가짜(Mock) 함수 (테스트용) -----------------
# def mock_generate_contract() -> str:
#     return """
# 제목: 근로계약서 초안
# 사용자: 김철수
# 근로자: 홍길동

# 제1조 (목적)
# 본 계약은 사용자와 근로자 간의 근로 조건에 관한 사항을 정함을 목적으로 한다.

# 제2조 (업무 장소 및 내용)
# 근무 장소: 서울시 강남구 테헤란로 123
# 담당 업무: 백엔드 개발 및 유지보수

# 제3조 (근로시간)
# 1. 근무 시간: 오전 9시 00분부터 오후 6시 00분까지 (휴게시간 1시간 포함)
# 2. 휴게 시간: 오후 12시 00분부터 오후 1시 00분까지
# 3. 주휴일: 매주 토요일, 일요일

# 제4조 (임금)
# 1. 임금 형태: 월급
# 2. 월 임금: 3,000,000원 (삼백만 원)
# 3. 지급일: 매월 25일

# 제5조 (계약 기간)
# 계약 기간은 2025년 10월 1일부터 2026년 9월 30일까지로 한다.
# """

# # ----------------- API 요청 및 응답 모델 -----------------
# class ChatRequest(BaseModel):
#     message: str

# class ContractResponse(BaseModel):
#     title: str
#     content: str

# # ----------------- API 엔드포인트 -----------------

# @app.get("/")
# def read_root():
#     return {"message": "근로계약서 챗봇 백엔드 서버입니다."}

# @app.post("/generate_contract/", response_model=ContractResponse)
# def generate_contract(request: ChatRequest, db: SessionLocal = Depends(get_db)):
#     try:
#         ai_output = mock_generate_contract()
#         lines = ai_output.strip().split('\n')
#         title = lines[0].replace('제목:', '').strip()

#         employer_name = lines[1].replace('사용자:', '').strip()
#         employee_name = lines[2].replace('근로자:', '').strip()

#         content = '\n'.join(lines[4:]).strip()

#         new_contract = EmploymentContract(
#             employer_name=employer_name,
#             employee_name=employee_name,
#             contract_content=content
#         )

#         db.add(new_contract)
#         db.commit()
#         db.refresh(new_contract)

#         return ContractResponse(title=title, content=content)

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))